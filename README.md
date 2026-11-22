# Zappngo

An entire Django application deployment in one command. Uses
[pico_django.py](https://github.com/readevalprint/mini-django/blob/master/pico_django.py) for the tiniest Django
project (settings, URLs and view in one file) and [Zappa](https://github.com/zappa/Zappa) to run it serverless on
AWS Lambda behind API Gateway.

`GET /` says `Hello, World!` and `GET /Pete` says `Hello, Pete!`.

## Prerequisites

- Python 3.13 (it must match the `python3.13` Lambda runtime in `zappa_settings.json`, because Zappa packages
  the virtualenv it runs in).
- An AWS account and a [credentials file](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html). The
  profile you use needs permission to create the deployment's IAM role, Lambda function, API Gateway and S3
  bucket (Zappa's [minimum policy](https://github.com/zappa/Zappa#custom-aws-iam-roles-and-policies-for-deployment)
  lists them).

## Deploy

1. Check `zappa_settings.json`: `aws_region` (default `eu-west-2`), `profile_name` (default `default`) and
   `s3_bucket`, which must be unique across AWS, so change `zappngo-dev` to your own.
2. Install and deploy:

   ```
   python3.13 -m venv .venv
   . .venv/bin/activate
   pip install -r requirements.txt
   zappa deploy dev
   ```

Later changes: `zappa update dev`. Remove everything: `zappa undeploy dev`.

## Settings

| Variable | Default | |
| --- | --- | --- |
| `ALLOWED_HOSTS` | `*` | Comma separated. The API Gateway host name is only known after the first deploy, so any host is allowed until you narrow it (set it under `environment_variables` in the stage). |
| `DJANGO_SECRET_KEY` | random per start | Nothing here signs or stores anything, so no key is needed; set one if the app ever uses sessions or signing. |

**This is a demo. It has no authentication and no rate limiting; do not run anything important on it.**
