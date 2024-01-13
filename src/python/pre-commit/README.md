pre-commit
==========

[Return to top README.md](../../../README.md)

# Installation

[Docs](https://pre-commit.com/)

```bash
pip install pre-commit
```

validate with

```bash
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

[Guide](https://stackoverflow.com/questions/61032281/exclude-some-files-on-running-black-using-pre-commit) to exclude specific folders from being checked during run of `pre-commit`

# `pre-commit autoupdate`

The versions of each repo used for a hook must be stated explicitly within `.pre-commit-config.yaml` which implies needing to manually update these values over time. However, you can update these values automatically by running

```bash
pre-commit autoupdate
```

# `mypy`

[Cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) for `mypy`

# pre-commit PyTest

It is possible, though [not recommended](https://github.com/pre-commit/pre-commit/issues/761#issuecomment-394167542), to run PyTest as a pre-commit hook. If you want to do it anyway, [here ](https://stackoverflow.com/questions/64011304/running-pytest-as-a-pre-commit-hook-no-such-file-or-directory-issue)are some example configurations.

# Suggested Settings

[link](https://towardsdatascience.com/4-pre-commit-plugins-to-automate-code-reviewing-and-formatting-in-python-c80c6d2e9f5)

Added a sample `.pre-commit-config.yaml` to under the parent directory

# Code Format (old)

guide for using `black` and `flake8` and `isort` in a `pyproject.toml`, also talks about using a `.pre-commit-config.yaml` file.

`black` [guide](https://medium.com/@josephlyu.sj/python-auto-formatter-autopep8-vs-black-and-some-practical-tips-e71adb24aee1)

Code formatting shortcut in VSCode **Alt+Shift+f** or look for `Format Document` in the command pallette

Gonna go with `black`, [guide](https://black.readthedocs.io/en/stable/getting_started.html). Add it to `requirements.txt`

Run `black` by running

```bash
black <source_file_or_directory>
```

This worked right away. However I'm not a fan of using double-quotes instead of single quotes, so one option is to pass `--skip-string-normalization` in the command line or to insert it into the settings, [guide](https://sbarnea.com/lint/black/). `-S` for short

`flake8` [guide](https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/python/linting/flake8.html)

Run `flake8` by running

```bash
flake8
```

Configure how flake8 runs by having a `setup.cfg` file, for example,

```ini
[flake8]
exclude =
    .git,
    __pycache__,
    env,
max-line-length = 88
```

This prevents `flake8` from looking at files we are not interested in adding to a code repo. This also changes the maximum line length to align with `black`

# docstrings

[guide](https://www.programiz.com/python-programming/docstrings)

[guide](https://stackoverflow.com/questions/3898572/what-are-the-most-common-python-docstring-formats) to popular docstring formats
