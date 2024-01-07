pre-commit
==========

[Return to top README.md](../../../README.md)

# Installation

[Docs](https://pre-commit.com/)

```bash
pip install pre-commit
```

validate with

```
pre-commit --version
```

# Usage

Create a `.pre-commit-config.yaml` file underneath the parent directory. Populate this file with all the pre-commit hooks of interest. Can get a sample set of hooks by running

```bash
pre-commit sample-config
```

then copying and pasting the returned text into `.pre-commit-config.yaml`

[Supported hooks](https://pre-commit.com/hooks.html)

Next, in order to add the desired hooks into the `.git` hook structure, run

```bash
pre-commit install
```

At this point, whenever you run `git commit` the hooks will be run first. If you would like to run the hooks on their own, run

```bash
pre-commit run --all-files
```

This can be useful if you want to run the hooks without actually making a new `git commit`

If in the future you add more hooks to `.pre-commit-config.yaml`, you don't have to re-run `pre-commit install`.

# `pre-commit autoupdate`

The versions of each repo used for a hook must be stated explicitly within `.pre-commit-config.yaml` which implies needing to manually update these values over time. However, you can update these values automatically by running

```bash
pre-commit autoupdate
```

# pre-commit PyTest

It is possible, though [not recommended](https://github.com/pre-commit/pre-commit/issues/761#issuecomment-394167542), to run PyTest as a pre-commit hook.

# Suggested Settings

[link](https://towardsdatascience.com/4-pre-commit-plugins-to-automate-code-reviewing-and-formatting-in-python-c80c6d2e9f5)

Added a sample `.pre-commit-config.yaml` to under the parent directory
