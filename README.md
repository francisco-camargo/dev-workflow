Development Workflow
====================

***Guide to setting up and using a machine for code development***

Francisco Camargo

# Abstract

This repo collects the details necessary to set up my dev workflow on a new machine.

Old: I want to learn to use Ubuntu to develop. Will do this both via the Windows Subsystem for Linux (WSL)  on one machine and from a machine with Ubuntu installed as the OS.

I also want to learn to use VSCode in conjunction with using Ubuntu.

To clone this repo:

```bash
git clone https://github.com/francisco-camargo/dev_workflow.git
```

# Terminal
To print out a tree view of the current directory use the `tree` command

# Markdown
[link](src/markdown/README.md)

# git
[link](src/git/README.md)

# Data Versioning

DVC (Data Version Control)
Guild.ai

# VSCode
[link](src/vscode/README.md)

# Vim

## (Optional) Install Vim on Linux

Commands to install Vim to be used within the terminal

```bash
sudo apt update
sudo apt install vim
```

## Vim on VSCode

If you use VSCode you can also use Vim via the **Vim** extension, and you can learn Vim via the **Learn Vim** extension. The **Learn Vim** [book](https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/dedication/), and [reference](https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/cheatsheet) of Vim commands.

[Guide](https://hoitz.medium.com/improved-vim-setup-in-visual-studio-code-bc579501b80c) on how to customize Vim keybindings within VSCode.

## Vim Commands

### Normal Mode

* Get into command mode: `esc`
* Enter Insert mode: `i`
* Enter Insert mode one character ahead: `a`
* Enter Visual mode: `v`
* Enter Command mode: `:`
* Moving the cursor
  * Move up: `k`
  * Move down: `j`
  * Move left: `h`
  * Move right: `l`
* New line
  * Below and enter insert mode: `o`
  * Above and enter insert mode: `O`
* Search and replace

[Guide](https://phoenixnap.com/kb/cut-copy-paste-vim)

* Copy
  * Everything to the right: `y$`
  * (Almost) everything to the left: `y^`
  * Entire line: `yy`
  * Word with its trailing whitespace: `yaw`
  * Word without its trailing whitespace: `yiw`
  * `yfx`
  * `ytx`
* Past
  * `P`
* Cut
  * Current line: `dd`
  * Everything to the right: `d$`

### Visual Mode

This is the mode used to highlight text, [guide](https://phoenixnap.com/kb/cut-copy-paste-vim).

* Highlight current word: `viw`

# Python

## Install Python on Windows

[Link](https://www.python.org/downloads/) to download Python.

During installation, be sure to add Python to PATH:

![1670921358303](image/README/1670921358303.png)

Check the version of Python. Note that it can have different aliases, e.g. `python`, `py`, `python3` etc.

```bash
python --version
>>> Python 3.11.0
```

If you use VSCode, be sure that the desired Python Interpreter is used: from the Command Pallette search for `Python: Select Interpreter`. Can check the bottom right of the window:

![1670921755378](image/README/1670921755378.png)

## Install Python on Ubuntu

We do want to install python within WSL: [guide](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/)

give an [alias](https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3?newreg=a3ae2d11b44641baba3120c0f6ca6111)
`alias python = python3.10`

## Python Code Environment

Download and install Python from [link](https://www.python.org/downloads/)

To create an environment via the terminal, use
`python -m venv env`

To activate environment, use
`env/Scripts/activate`

To update `pip`, use
`python -m pip install --upgrade pip`

To install libraries, use
`pip install -r requirements.txt`

To deactivate an active environment, use
`deactivate`

## Importing local code from other directories

Assume you have the following folder structure:

```shell
parent
	scriptE.py
	folder1
		scriptA.py
		scriptB.py
		folder3
			scriptF.py
	folder2
		scriptC.py
		scriptD.py
```

If you are in `scriptA.py` and

* want `scriptB.py`, use `import scriptB`
* want `scriptF.py`, use `import folder3.scriptF`
* want `scriptE.py`, you _must_ use the `from` syntax; `from ..scriptE.py import *`
* want `scriptC.py`, use `from ..folder2.scriptC`
  Note that this was tested using VSCode.

## Code Format

guide for using `black` and `flake8` and `isort` in a `pyproject.toml`, also talks about using a `.pre-commit-config.yaml` file.

`black` [guide](https://medium.com/@josephlyu.sj/python-auto-formatter-autopep8-vs-black-and-some-practical-tips-e71adb24aee1)

Code formatting shortcut in VSCode **Alt+Shift+f** or look for `Format Document` in the command pallette

Gonna go with `black`, [guide](https://black.readthedocs.io/en/stable/getting_started.html). Add it to `requirements.txt`
Run `black` by running

```bash
black {source_file_or_directory}...
```

This worked right away. However I'm not a fan of using double-quotes instead of single quotes, so one option is to pass `--skip-string-normalization` in the command line or to insert it into the settings, [guide](https://sbarnea.com/lint/black/)

* linting
* flake8

## docstrings

[guide](https://www.programiz.com/python-programming/docstrings)
[guide](https://stackoverflow.com/questions/3898572/what-are-the-most-common-python-docstring-formats) to popular docstring formats

## Running Python code in VSCode

To use the IPython terminal, install IPython
```bash
pip install ipython
```

Then in the VSCode terminal run

```bash
ipython
```

need to load (once) the `%autoreload` extension, [guide](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html),

```Python
%load_ext autoreload
```

now can use `%autoreload`

```Python
%autoreload
%run main.py
```

I was able to run both of these lines together in the VSCode terminal by using **Ctrl+o** in the terminal to have multiple lines of input.

This will have the same effect as clicking **Run** within Spyder on whatever Python file Spyder has open. This also has the benefit of seeing changes to the code while still in IPython, which is not working when using the "import main" approach.

(old) and then within the IPython terminal that has now been instantiated, import the module you want to use

```Python
import main; main.main()
```

## Using `setup.py`

The [documentation](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html) for `black` suggests that we can use a `pyproject.toml` file to replace both `setup.py` and `setup.cfg` files.

![1670897817471](image/README/1670897817471.png)

## Packaging

Learn how to package code, there are several options, so first want to just look at all of them before picking one to run with

[Guide](https://stackoverflow.com/questions/1471994/what-is-setup-py)

[Guide](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#configuring-your-project)

[Guide](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/), in it, they say: nowadays the use of setup.py is discouraged in favour of pyproject.toml together with setup.cfg. Find out how to use those [here](https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/).

Poetry also does a similar thin? [webpage](https://python-poetry.org/) Sounds like poetry also does dependance management, so maybe use it instead of `venv`? [Poetry intro](https://youtu.be/0f3moPe_bhk) from ArjanCodes, who seems happy with it. Sounds like it can help with package publishing.

What the heck is a wheel?

## Plotting

I can plot out-of-the box to a pop-up window in VSCode if I use Run, but if I use ipython to run the code, I can't seem to be able to get the plots.

In `./src/plotting.py` I placed sample code for a plotting function that handles the aesthetics well. It Accounts for; uncertainty bands, `.eps` formatting, size of plot for two column paper, and several other minor details.

## Data Validation
[Pydantic](https://www.youtube.com/watch?v=zN4VCb0LbQI)

## Pandas

### Data Types for DataFrames
[Guide](https://youtu.be/-tU7fuUiq7w)
[Guide](https://towardsdatascience.com/validate-your-pandas-dataframe-with-pandera-2995910e564)

### `df.apply()`

[df.apply()](https://www.geeksforgeeks.org/apply-function-to-every-row-in-a-pandas-dataframe/)

### `SettingWithCopyWarning`

[Guide](https://realpython.com/pandas-settingwithcopywarning/), simple explanation on how to deal with this. First line of defence: use `.loc` and `.iloc`

```Python
df.loc[idx_label, col_label] = some_new_value
```

I think `idx_label` then just needs to be an element found within `df.index()`.

Alternatively, you could use a mask. By example:

```Python
mask = df[column_label]==some_value
```

This returns a mask of boolean values to pick out rows. Now use this mask instead of `idx_label`

```Python
df.loc[mask, col_label] = some_new_value
```

## SciKit-Learn

Want to be able to use sklearn without having to switch back and forth between numpy arrays and dataframes. Use [sklearn-pandas](https://github.com/scikit-learn-contrib/sklearn-pandas). I have successfully used this in `make_features.py` within the `dsc_roadmap` project; import `DataFrameMapper` and use it in conjunction with the sklearn `SimpleImputer`.

### ShuffleSplit
[StackOverflow](https://stackoverflow.com/questions/34731421/whats-the-difference-between-kfold-and-shufflesplit-cv#:~:text=As%20your%20data%20set%20grows,ShuffleSplit%20is%20an%20attractive%20option.) on why ShuffleSplit is useful when training data grows large

## Experimental Setup

[Guide](https://hydra.cc/docs/intro/) into how to use Hydra to help run experiments using Python.
[Video](https://youtu.be/tEsPyYnzt8s) intro
[Video](https://www.youtube.com/watch?v=bNGu8A6F3-8), mentions integration with mlflow around 20min mark, talks about parallelization (26min mark)
[Video](https://www.youtube.com/watch?v=3gk9CvMOdzE) for hydra-zen

## Model based testing

There is the `hypothesis` python package. [Docs](https://hypothesis.readthedocs.io/en/latest/), [demonstration](https://youtu.be/-S3BFkNn0rQ)

# LaTeX
[latex](src/latex/README.md)

# (Optional) Using WSL

## Install WSL

[Check](https://www.zdnet.com/article/windows-10-tip-find-out-if-your-pc-can-run-hyper-v/) if your PC can run Hyper-V
[Guide](https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10)

## Install Ubuntu in WSL

Go to the Microsoft Store and install Ubuntu 20.04 (or whatever version you want).

## Where is this repo once it is cloned?

Where is this repo in my local? I can get to it from the Ubuntu terminal using

`cd dev_workflow`

or

`cd /home/francisco/dev_workflow`

In Windows I can find it at

`\\wsl$\Ubuntu-20.04\home\francisco\dev_workflow`

## Terminal Shortcuts

* New terminal tab: **ctrl+shift+t**
* New terminal window: **ctrl+alt+t**
* Switch to a specific tab: **alt+[tab #]**
* Close current tab (or window): **ctrl+shift+w**
* Copy: **ctrl+shift+c**
* Paste: **ctrl+shift+v**
* But how to I highlight text? What to do the equivalent of the Windows **ctrl+shift**+[arrow]

## Ubuntu Shell commands

* Make a directory: `mkdir [directoryname]`
* New file: `touch [filename.extension]`
* Check contents of file (?): `cat [filepath]`

## Testing

### TSLgenerator
The [TSLgenerator](https://github.com/alexorso/tslgenerator) tool helps convert domain boundaries of a problem into a suite of unit tests.

Example source code file that dictates CLI for this application on [MacOs](https://github.com/alexorso/tslgenerator/blob/c04cda8578251a6035f9a160c896f1f91b6dde85/MacOSX/main.c#L60).

Example of running the application on Windows:
![image](https://github.com/francisco-camargo/dev_workflow/assets/86134108/2f951974-f608-4bc5-aff8-571fc233fd2f)


