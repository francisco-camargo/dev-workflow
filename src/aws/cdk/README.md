AWS Cloud Development Kit (CDK)
===============================

[Return to top README.md](../../../README.md)

TODO: try to do this within a Docker Container

# Install CDK

[AWS Getting Started Guide](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

* [Option A](https://miguelacallesmba.medium.com/using-docker-for-aws-cdk-development-7054086deb3d)
* [Option B](https://aws.plainenglish.io/run-aws-cdk-in-a-docker-container-bcb307ccf232)
* [Option C](https://medium.com/dataengineerbr/creating-a-local-environment-to-develop-on-aws-cdk-with-docker-and-vscode-f26569d30870), [repo](https://github.com/contino/docker-aws-cdk)

# Initialize

To initialize an Application, go to the desired parent directory for the project and run

```bash
cdk init app --language=python
```

There are other language options.

This will initialize this folder as a `git` repository.

Is this ran properly, a `.venv` environment folder will have been created unto which you can install any packages of interest. To activate, try

```bash
. .venv/bin/activate
```

Additionally, several other files are made including

* `.git`
* `.gitignore`
* `.venv`
* `README.md`
* `app.py`
* `cdk.json`
* `requirements-dev.txt`
* `requirements.txt`
* `source.bat`
* `tests`
* A folder with the same name as the parent directory which contains a stack python script

The `requirements.txt` file contains

* `aws-cdk-lib`
* `constructs`

The `requirements-dev.txt` file contains `pytest`

# `app.py`

The app will invoke any Stacks of interest

```python
#!/usr/bin/env python3
import os

import aws_cdk as cdk

from project_name.project_name_stack import ProjectStack
# This is the custom stack definition


app = cdk.App()
ProjectStack(app, "ProjectStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
```

# Constructs

A Stack is made up of Constructs, here are references for a few

* [Role](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_iam/Role.html)
* [Function](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda/Function.html)
* [Bucket](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_s3/Bucket.html)

# Synthesize and Deploy

Run

```bash
cdk bootstrap
```

The cdk bootstrap command will deploy a CloudFormation stack named CDKToolkit to the AWS account using the credentials you configured in a previous lab step. The stack consists of an S3 staging bucket that is used for storing any assets used in your CDK application.

To synthesize a CloudFormation template, run

```bash
cdk synth
```

This will create a new folder, `cdk.out`

To deploy, run

```bash
cdk deploy
```

Once complete you will be given a Stack ARN
