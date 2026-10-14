# Module 3.5 Theory Guide — AWS Taster

Read the section for the session you are in. This module is foundations first:
what the cloud is, who is responsible for what, how you are billed, then IAM.
Lambda and one CloudFormation bucket come at the end, after identity works.
Module 4.5 is the real AWS block (VPC, compute, storage, boto3, the compliance
project). Terraform is Module 6.5.

The AUTOCOR exam does not require AWS. It tests the patterns: call an API,
declare infrastructure, handle identity and secrets. We learn those patterns
on AWS because that is the cloud you are targeting for the job.

---

## 1. What you have been doing, and what changes

In Module 3 your Python was a **client**. It sent HTTP to CML and received
JSON. CML already existed. You did not create the lab server.

AWS is a set of APIs that **create and run things**: storage, functions,
networks, identity. The console is a website in front of those APIs. The CLI
and boto3 are other clients of the same APIs. CloudFormation is a client that
reads a template and calls the APIs until the real resources match the file.

Real use for a network engineer, not a toy:

- A Lambda runs every night, calls Catalyst Center, and writes a compliance
  JSON report to S3. Nobody SSHs to a Linux box to cron a script.
- A CloudFormation (or Terraform) file is how the S3 bucket, the schedule,
  and the permissions are created the same way in a lab account and later in
  a company account. Clicking in the console does not travel with you.

That nightly report is Module 4.5's project. This module does not start there.
It starts with the account, the bill, and IAM, which every later service sits on.

---

## 2. Account, region, Availability Zone

**Account.** An AWS account is the billing and permission boundary. Everything
you create is inside one account, and the bill for those things comes to that
account. A company has many accounts (lab, prod, security) so a lab experiment
cannot spend production's money or read production's data. You will use one
free-tier account. Treat it as a lab account.

**Region.** A region is a geographic cluster of data centers: `us-east-1`
(N. Virginia), `ap-south-1` (Mumbai), `eu-west-1` (Ireland). A resource lives
in one region unless you deliberately copy it. An S3 bucket in `ap-south-1`
is not visible to a CLI pointed at `us-east-1`. This is the cloud version of
"which data center did you build it in?" Stay in one region for the whole
module.

This lab uses **Sign up for AWS (new)**: GitHub is the login, and AWS assigns
the project region from the contact country. India is placed in Asia Pacific
(Sydney), `ap-southeast-2`. That signup cannot switch the project to
`us-east-1`. Billing pages still open in `us-east-1` because the bill is
account-wide, not a resource living in Virginia. The region that matters for
Lambda and S3 is the one on the project, Sydney.

**Availability Zone (AZ).** A region contains several isolated data centers
(`us-east-1a`, `us-east-1b`). You do not place this module's Lambda or bucket
into an AZ by hand. You need the word because interviewers ask "what is a
region vs an AZ?" Region = metro area of AWS. AZ = one data center (or a
tight group) inside that metro, with independent power and network. You put
copies of an app in two AZs so one building can fail.

**Rule of thumb:** account = who pays and who is allowed. Region = where the
resource physically lives. AZ = which data center inside that region.

---

## 3. The bill is part of the design

AWS charges for what exists and for what runs, often per hour or per request.
Free tier covers a small Lambda and a small S3 bucket. It does not cover
"I left a large thing running." People get surprise bills from resources they
forgot, in a region they forgot they selected.

Before you create a Lambda or a bucket, you create a **budget alarm**: "email
me if this month's forecast crosses a few dollars." That is the cloud version
of a syslog alarm for cost. We do it on day one, while the account is empty,
so the alarm exists before the first mistake.

You will also learn to **delete** what you create (`aws cloudformation delete-stack`,
or delete the Lambda). Creating without a delete path is how lab accounts
rot.

---

## 4. IAM — who is allowed to call the API

CML checked a username and password, then gave you a bearer token. AWS checks
**IAM**. Four words:

| Word | What it is | Network analogy |
|---|---|---|
| **User** | A person or a script identity you create. Has long-term access keys if you create them. | A local account on a device. |
| **Role** | An identity that something **assumes** for a while. Lambda runs as a role. No password stored in the function. | A task account a process uses, not a human login. |
| **Policy** | A JSON document: which actions, on which resources, allow or deny. | An ACL: permit this traffic, deny the rest. |
| **Least privilege** | The policy allows only the actions this job needs. | Don't put `permit ip any any` on every interface. |

A Lambda that only needs to read one S3 bucket should not have
`AdministratorAccess`. AdministratorAccess is the cloud version of logging in
as a user who can reconfigure every router. It is how a leaked key becomes a
full account takeover, and how a bug deletes things you did not mean to touch.

**Access keys** are the long-lived secret for an IAM user (`AKIA...` plus a
secret). They are the AWS form of the Meraki API key: whoever has them is
that user, until you disable the key. They do not go in git, in a screenshot,
or in a Python file.

This lab does **not** create access keys. The GitHub login is already the
owner. The CLI command `aws login` opens a browser, you approve that same
login, and the CLI keeps a temporary session (about 12 hours) under a named
profile. That is the same idea as the CML bearer token. A file named
`~/.aws/credentials` may already exist on the machine from something older.
Leave it alone. Use the profile `hello-aws`, region `ap-southeast-2`.

Later, Lambda runs as a **role**, not as your GitHub login. The role is the
identity for a program. Your login is the identity for you.

> **Interview line:** "I don't put AWS keys in source. Humans or CI get
> short-lived credentials or a role. A policy names the actions and the
> resources. Admin on day one is how lab keys become incidents."

---

## 5. Console, CLI, SDK, template

Four ways to talk to the same APIs:

| Way | What it is | When you use it |
|---|---|---|
| **Console** | The website. | First time you see a service. Easy to mis-click. Hard to repeat. |
| **CLI** | `aws s3 ls`, `aws lambda invoke`. | Your terminal. Scriptable. What this module uses to deploy. |
| **SDK (boto3)** | Python library. Same calls as the CLI. | Module 4.5, inside Lambda and scripts. |
| **CloudFormation** | YAML that says what should exist. | When the resource must be repeatable and deletable as a stack. |

The CLI and boto3 are **imperative**: you issue commands, and each command
does something now. Run "create bucket" twice and the second run fails
because the bucket already exists, or you create a second one if you changed
the name.

CloudFormation is **declarative**: the file is the desired end state. You
deploy the same file twice. The second time AWS compares the file to what
exists and changes only the difference. That is the same idea Terraform calls
plan/apply. Module 6.5 will feel familiar because of this week.

---

## 6. Three pieces, before any lab

Almost every small cloud app is three pieces. Learn the pieces on their own.
The network-automation project is only one use of them.

| Piece | AWS name | Everyday job |
|---|---|---|
| A place to put files | **S3** | The hard disk |
| Code that runs when something happens | **Lambda** | The worker |
| The "something happened" message | an **event** | The doorbell |

A normal computer is on all day, has a disk, and you log in and run a program.
In this style of cloud you do not keep that computer. You rent the disk (S3)
and you rent a short run of your function (Lambda). Something else rings the
doorbell (the event). AWS owns the machines underneath. You never SSH to them.

**EC2**, which we meet properly in Module 4.5, is the other choice: a virtual
computer that stays on, with its own disk, that you patch. A website that
must answer every second often uses one. A job that should run only when a
file arrives, or once a night, is a waste of an always-on computer. That job
is Lambda.

### S3

S3 is file storage. Amazon calls a file an **object** and a folder-of-files a
**bucket**. A photo site does not save the jpeg on the web server's disk. The
upload goes into a bucket. If that server dies, the pictures are still there,
because S3 keeps copies in more than one Availability Zone inside your region
(Sydney, for this project).

You do not SSH to a bucket. You use the S3 pages in the console, or an API
call: put a file, get a file, list files. A bucket name must be unique among
**all** AWS accounts in the world, so `photos` is taken and a name like
`ritika-lab-reports-2026` might be free. The name is not a secret. The files
inside are.

A bucket should stay private. "Public" means anyone who can guess the URL can
download the file. That is the teammate mistake from the shared-responsibility
conversation. Our lab bucket keeps **Block public access** on. The object URL
is only an address. Opened in a browser that is not signed in to AWS, the PDF
returns `AccessDenied`. The same file opens from the console because that
request is your login. Do not clear Block public access to "fix" the denial.

Outside networking, S3 holds photos, invoices, backups, logs, and video. The
compliance report we mentioned earlier is the same idea: one JSON file in a
bucket, named `reports/2026-10-05.json`.

### Lambda

Lambda is a function AWS runs for you, then stops. You give it Python. You
do not install Linux, you do not leave a computer on overnight, and you are
billed for the seconds the function actually runs.

Outside networking, the usual jobs are small and triggered:

- A customer uploads a photo to S3. Lambda makes a thumbnail.
- A customer places an order. Lambda sends the receipt email.
- A web form is submitted. Lambda checks the fields and saves them.

Lambda is a bad place for a database that must stay up, or a program that
runs for hours. One run is limited to 15 minutes. The first call after the
function has been idle can be slower, because AWS is creating the environment.
That pause is a **cold start**. It is not a bug in the Python.

### What an event is

An **event** is the JSON description of "this just happened," handed to your
function as its input. The function does not sit in a loop asking "did
anything happen?" Something invokes it and passes the event.

HTTP is **one** kind of event, not the definition of Lambda. I chose it for
the lab because Module 3 was HTTP, so you can call a URL and see the answer.
AWS does not require it. You turn on a **Function URL** if you want AWS to
attach an HTTPS address to the function. A browser or `curl` hits that
address. The event your Python receives is that request, rewritten as JSON:
method, path, headers, body. Your return value becomes the HTTP response.
You are the server. AWS is the thing that woke you.

Other events you will meet, each a different doorbell:

- **You press Test** in the Lambda console and paste JSON. You are pretending
  to be the doorbell. This is how you see a function run before it has a URL.
- **S3** invokes the function because a file was created. The event names the
  bucket and the file. This is the thumbnail case.
- **EventBridge** invokes the function because a clock fired, or because some
  other AWS service announced a change. EventBridge does not store files and
  does not run your Python. It is the alarm clock and the switchboard. "Every
  night at 02:00, call this function" is an EventBridge schedule. The old
  name was CloudWatch Events. Same job.

The nightly Catalyst Center report is that last one: EventBridge wakes
Lambda, Lambda calls the controller, Lambda writes one object into S3. We
do not build that this week. The HTTP lab is only so you can watch a
function run.

### Console first, automation after

The console is the website. The top search box is how you move. Type `S3`
and open the service: a list of buckets, empty at the start. Type `Lambda`
and open the service: a list of functions, empty at the start. Check the
browser URL for `ap-southeast-2` before you create anything. A service page
opened in another region is an empty room, not a missing account.

Clicking **Create bucket** or **Create function** calls the same API the CLI
calls. We will click once, after this picture is clear, so you have seen the
object with your eyes. CloudFormation, later, is a file that describes the
bucket so the click can be repeated and undone. The file is not a new kind
of storage. It is a way to say "this bucket should exist" without using the
mouse.

---

## 7. What we will create, after the picture is clear

One private S3 bucket, seen first in the console, then described in a
CloudFormation template so a second deploy updates it instead of making a
duplicate. One Lambda function that returns a tiny JSON list. Its event, for
this lab only, is HTTP via a Function URL. The function does not read the
bucket yet, so it does not need permission to. EventBridge is not part of
this taster. It is the clock we add in Module 4.5 when the function should
run at night.

---

## 8. What "done" looks like for an interviewer

You can say, with a repo behind it:

- You have an AWS account and a budget alarm.
- You can explain user, role, and policy, and you did not grant admin for a
  function that reads one file.
- A Lambda Function URL returns device JSON.
- A CloudFormation stack created a private S3 bucket, and you can update and
  delete that stack from the template.
- Keys were never in git.

That is the taster. Module 4.5 is where the function calls a real network API
on a schedule and stores the result in the bucket.
