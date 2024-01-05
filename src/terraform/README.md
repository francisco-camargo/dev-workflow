Terraform
=========

[Return to top README.md](../../README.md)

# Installation

[Docs](https://developer.hashicorp.com/terraform/tutorials)

[AWS Docs](https://developer.hashicorp.com/terraform/tutorials/aws-get-started)

## Manual Install on Windows

Download and unzip the `terraform` binary. Decided where to store it, eg.

```bash
C:\terraform\terraform\terraform.exe
```

Now we need to edit the `Path` environment variable to add the absolute path of the directory that contains the executable, eg.

```bash
C:\terraform\terraform\
```

to verify

```bash
terraform --version
```