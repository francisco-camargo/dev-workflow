AWS CLI
=======

[Return to top README.md](../../../README.md)

# Docker Image

[link](https://hub.docker.com/r/amazon/aws-cli)

# Install AWS CLI

[AWS CLI getting started docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

verify installation with

```bash
aws --version
```

## `config` file

Use the aws [configure wizard](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-token-auto-sso) to setup the `config` file

```bash
aws configure sso
```

Another [guide](https://dev.to/slsbytheodo/understand-the-aws-sso-login-configuration-4am7)

You will be asked about SSO info; a name for the sso-session (your choice of name), region (I think it's the region of the AWS account), and registration scopes (this I have left blank and it autofills to `sso:account:access`).

With info entered, the terminal should automatically try to open the SSO authorization page in your browser. If succesful you should see the terminal show you a code that matches what is shown in the browser, if so, click to grant access.

Next you will be asked about which AWS account to use and which role to use, so select accordingly. If you only have one account/role, they will be chosen automatically.

Next you will be asked about region, provide the region that correspond to the VPC you want to use (the region where the resources of interest are... I think). When asked about output format, you can leave it blank. Provide a CLI profile name when asked.

Running the wizard will create the folder

```bash
~/.aws
```

Additionally, the wizard will have populated this directory with a `config` file which contains the info you provided to `aws configure sso`. However, a `credentials `file has not yet been created. I have been able to `git clone` without needing to set up a `credentials` file.

[Docs](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html) on file location

## `credentials` file

The credentials info will be shown to us in the SSO page:

![1704309386385](image/README/1704309386385.png)

Click on "Command line or programmatic access"

"Option 2" let's you copy the necessary credentials information which can than me pasted into the `~/.aws/credentials` file

![1704317178807](image/README/1704317178807.png)

I don't understand when this information is needed... I have commented out these values from within my `credentials` file and yet working with a CodeCommit repo seems to work fine

# SSO Log In

To login

```bash
aws sso login
```

If you would like to use a particular profile, use the `--profile` option and provide whatever CLI profile name you'd like to use

To know which profile you are using, run

```bash
aws sts get-caller-identity
```

There is also

```bash
aws configure list
```

There is also

```bash
aws configure list-profiles
```

# CodeCommit

After installing `git`, install `git-remote-codecommit`

[Guide](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html)

```bash
pip install git-remote-codecommit
```

To clone from CodeCommit, be sure to have been logged into SSO and now try

```bash
git clone codecommit::<region>://<cli profile>@<repo name>
```

which will thus require the corresponding `<cli profile>` to be defined within `config`. Be sure that the CLI profile I want to use has `region` set to the region of the code repo I want to clone, or

```bash
git clone codecommit::<region>://<repo name>
```

which I think uses the default AWS CLI profile, so just means that the default profile has to have all the info needed
