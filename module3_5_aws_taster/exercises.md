# Module 3.5 — Exercises

You do the console and CLI steps. The guide explains why before each one.

## S1 — account and cost
1. In your own words: what is an AWS account, a region, and an Availability Zone?
2. Create a free-tier account if you do not have one. Pick one region and write it down.
3. Create a budget alarm (a few USD) that emails you. Do this before any Lambda or bucket.

## S2 — IAM and CLI
4. Create an IAM user for the CLI. Attach a policy that is narrower than AdministratorAccess once you know the actions you need. Until then, note why admin is a temporary lab risk, not a habit.
5. `aws configure --profile hello-aws`. Confirm `aws sts get-caller-identity --profile hello-aws` prints your account, not an error.
6. Keys live in `~/.aws/credentials` on your machine. Confirm they are not inside this git repo.

## S3–S4 — Lambda
7. Write a function that returns a small JSON list of devices (hostname, site). Deploy it. Open the Function URL. You should get JSON, not an error page.
8. Change one hostname, redeploy, curl again. The URL stays the same. The body changes.

## S5–S6 — CloudFormation
9. Write a template with one private S3 bucket. `aws cloudformation deploy` creates a stack.
10. Change a tag in the template and deploy again. The stack updates. It does not create a second bucket.
11. Delete the stack when you are finished with the lab.

## Recall
After each session the coach writes `anki_session<N>.txt` from what you actually did.
