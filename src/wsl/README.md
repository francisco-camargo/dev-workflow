WSL
===

[Return to top README.md](../../README.md)

[List of commands](https://learn.microsoft.com/en-us/windows/wsl/basic-commands)

To check what distributions of WSL are installed

```bash
wsl --list --verbose
```

Expect to see Ubuntu on the list. If not... go install it. If you have Docker installed, that may add two distributions.

To set a default distribution

```bash
wsl --set-default <distribution name>
```

To launch a specific distribution

```bash
wsl --distribution <distribution name>
```

Can use optional `--user` option

Once you run this and a WSL terminal opens up, you may not be in the home directory, so may be good idea to run
```bash
cd ~
```
