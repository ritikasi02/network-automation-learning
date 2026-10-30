# Hello-AWS Taster

A first hands-on taste of AWS: build one private S3 bucket and one Lambda two
ways — by hand in the console (the UI way) and as code with CloudFormation (the
IaC way) — then deliberately break it and watch it recover.

**Region:** Asia Pacific (Sydney), `ap-southeast-2`. The region is **not** in the
template; it comes from my CLI profile `hello-aws`.
**Auth:** `aws login --profile hello-aws` (a temporary ~12h browser session, an
assumed role). **No long-lived access keys** anywhere, nothing secret in git.

## What I built
I logged in with my GitHub-based AWS account and confirmed my region (Sydney).
Then:
1. **S3** — created a bucket, blocked all public access, uploaded one object (a PDF).
2. **Lambda** — wrote a Python function that tells the caller, based on a filename
   in the URL, whether that file is "found". It reads a key/value out of the event
   (`queryStringParameters`); if the name is missing it returns an error instead of
   inventing a value. I tested it with the console **Test** button, then exposed it
   with a **Function URL** and passed `?name=...`.
3. **CloudFormation** — rebuilt an S3 bucket the IaC way: a YAML template managed by
   a **stack**. I created it, updated it, broke it, recovered it, and deleted it.

## Console path (the UI way)
- **S3:** search "S3" → Create bucket → name it (globally unique, lowercase) →
  leave **Block Public Access ON** → Create. Buckets are **private by default** and
  encrypted at rest automatically. An object's URL is just an **address, not
  permission**: a signed-out stranger gets `AccessDenied`; as the signed-in owner I
  could download it fine.
- **Lambda:** search "Lambda" → Create function → write the Python in
  `lambda_function.py` → the handler setting is `lambda_function.lambda_handler` →
  create a **Test** event (JSON I type) → Test runs the code and shows what it
  returns; it never touches S3 unless the code tells it to.

### Key Lambda ideas I learned
- `lambda_handler(event, context)`: **event** = the JSON input (shape depends on the
  trigger), **context** = facts about this run. Billed per run, 15-min limit,
  "cold start" = slower first run while AWS builds the environment.
- The **event shape depends on the trigger**. From a Function URL (HTTP), the query
  value arrives **nested**: `event["queryStringParameters"]["name"]`, not top-level
  `event["name"]`. That is why `?name=beach.jpg` first returned 400 until I read the
  nested key.
- **Don't invent data:** a missing key → return **400**, never a made-up placeholder,
  so the function fails loud instead of acting on fake input.
- For an HTTP trigger, `statusCode` is a **value the server reads** and turns into the
  real HTTP status; it is not a check the browser computes.

### Function URL caveat
A Function URL is a dedicated public HTTPS address bound to one function. I used
**AuthType NONE = public to the internet** — acceptable ONLY because this function
just echoes a filename and touches no data. Never NONE for anything that reads data
or spends money. API Gateway is the real choice for a full API.

## Automation path (CloudFormation, `bucket.yaml`)
Define the bucket/resources and properties in a YAML template, then run it via the
AWS CLI. What happens under the hood:
1. `cd` into the folder with `bucket.yaml`.
2. Run `aws cloudformation deploy ... --profile hello-aws`.
3. The CLI reads the YAML and sends an **HTTPS request to the CloudFormation API**
   (using the region + temporary session from my profile).
4. CloudFormation validates the template, builds a **change set** (the plan), then
   calls the **S3 API** to create the resource.
5. The **stack** (`hello-aws-bucket`) creates and manages the resource and remembers
   its state.

### Template vs stack (the mental model)
- **Template** (`bucket.yaml`) = the wish-list/blueprint (text, no state).
- **Stack** (`hello-aws-bucket`) = the live resources + the state AWS remembers.
- Three names: **logical ID** (`ReportsBucket`, my nickname), **physical name**
  (`ritika-s3bucket-20262026`, the real bucket, must be lowercase/unique),
  **Type** (`AWS::S3::Bucket`, AWS's fixed vocabulary — Properties like `BucketName`
  and `PublicAccessBlockConfiguration` come from that Type's schema).
- **Idempotent:** redeploying an unchanged template prints **"No changes to deploy"**
  and does nothing (same as Terraform; opposite of a blind `aws s3 mb` script).

### The break-and-fix I did (uppercase name → rollback)
I changed `BucketName` to have an uppercase letter and deployed. Because the name is
an **immutable** property, CloudFormation tried a **replacement** (create new, then
delete old). The **S3 API rejected** the uppercase name → `UPDATE_FAILED` →
automatic `UPDATE_ROLLBACK`. The failed replacement attempt was deleted and my
**original lowercase bucket survived untouched**. Fixing the name back to lowercase
and redeploying gave "No changes to deploy" — already healthy. (Contrast: changing a
**tag** was an in-place update, same bucket, no replacement.)

### Teardown
I deleted **through the stack**, not by hand:
`aws cloudformation delete-stack ...`. This deletes the real bucket AND the stack's
state record, so there's no **drift**. Rule: whatever created a resource should
destroy it (same as `terraform destroy`). (A non-empty bucket would throw
`DELETE_FAILED`; mine was empty, so it deleted cleanly.)

## Commands I use often
```bash
# reauthenticate (session lasts ~12h)
aws login --profile hello-aws
aws sts get-caller-identity --profile hello-aws   # who am I / is my session valid

# CloudFormation lifecycle
aws cloudformation deploy --template-file bucket.yaml \
  --stack-name hello-aws-bucket --profile hello-aws
aws cloudformation describe-stacks --stack-name hello-aws-bucket --profile hello-aws
aws cloudformation delete-stack  --stack-name hello-aws-bucket --profile hello-aws
```

## AUTOCOR v2.0 ties
- **2.0 IaC** — declarative templates, stacks, state, idempotency, rollback.
- **1.6 REST/CLI** — the CLI makes HTTPS API calls; Function URL = HTTP trigger.
- **3.6 Secure coding** — no hardcoded keys, temporary session, least privilege.
- **3.3 Diagnose from output** — reading stack events to find the root cause.
