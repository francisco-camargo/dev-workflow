# Learn to Develop on Ubuntu

## Goal

I want to learn to use Ubuntu to develop. Will do this both via the Windows Subsystem for Linux (WSL)  on one machine and from a machine with Ubuntu installed as the OS.

I also want to learn to use VSCode in conjuction with using Ubuntu.

## Clone repo

`$ git clone https://github.com/francisco-camargo/learn_ubuntu.git`

## Install WSL

Where is this repo in my local? I can get to it from the Ubuntu terminal using

`$ cd learn_ubuntu`

or

`$ cd /home/francisco/learn_ubuntu`

In Windows I can find it as 

`\\wsl$\Ubuntu-20.04\home\francisco\learn_ubuntu`

### Install WSL
[Check](https://www.zdnet.com/article/windows-10-tip-find-out-if-your-pc-can-run-hyper-v/) if your PC can run Hyper-V
[Guide](https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10)

### Install Ubuntu in WSL
Go to the Mircrosoft Store and install Ubuntu 20.04 (or whatever version you want).

## Terminal Shortcuts
* New terminal tab: `ctrl`+`shift`+`t`
* New terminal window: `ctrl`+`alt`+`t`
* Switch to a specific tab: `alt` + # of tab
* Close current tab (or window): `ctrl`+`shift`+`w`
* Copy: `ctrl`+`shift`+`c`
* Paste: `ctrl`+`shift`+`v`
* But how to I highlight text? What to do the equivalent of the Windows `ctrl`+`shift`+[arrow]

## Ubuntu Shell commands
* Make a directory: `$ mkdir [directoryname]`
* New file: `$ touch [filename.extension]`
* Check contents of file (?): `$ cat [filepath]`

## Vim

### Install Vim

Commands to install Vim to be used within the terminal

```
$ sudo apt update
$ sudo apt install vim
```

### Vim Commands

#### Normal Move

* Get into command mode: `esc`
* Insert mode: `i`
* Move up: `k`
* Move down: `j`
* Move left: `h`
* Move right: `l`

* New line below and enter insert mode: `o`
* New line above and enter insert mode: `O`

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
    * `p`
    * `P`
* Cut
    * Current line: `dd`
    * Everything to the right: `d$`

#### Visual Mode
[Guide](https://phoenixnap.com/kb/cut-copy-paste-vim)

### Use GitHub
Want to have this repo in GitHub and use a personal access token (PAT). I have set up a PAT in GitHub. It seems that in order to make use of it I need to clone the repo using HTTPS.

Will create one PAT per computer.

### Using git

#### git credentials
However, I did need to set my GitHub information:
```
$ git config --global user.name "name"
$ git config --global user.email "email@email.com"
```

Here I will use the GitHub "noreply" email which can be found in personal settings on GitHub, [guide](https://stackoverflow.com/a/51097104/9205210). For the password use a PAT. I don't want to have to enter my username and password (PAT) everytime, so follow this [guide](https://www.freecodecamp.org/news/how-to-fix-git-always-asking-for-user-credentials/) or maybe [this](https://www.techiediaries.com/git/stop-git-always-asking-for-username-and-password-when-using-https/) guide and essentially run the following commands:

```
$ git config --global credential.helper store
$ git config --global credential.helper cache
```

#### git diff
View of unstaged changes
```
$ git diff [filepath]
```

View staged changes
```
$ git diff --cached [filepath]
```

#### Change commit messege
To change the messege of the last commit
```
$ git commit --amend
```

#### git squash
[Guide](https://www.git-tower.com/learn/git/faq/git-squash) to using `rebase` to squash commits together. With several commits made, we can combine them into a single commit using `rebase`. For example, let's squash together the last 3 commits by running 

```
$ git rebase -i HEAD~3
```

This will bring up a text editor where we choose what to do with the last 3 commits. In this case we want to `pick` or `p` the oldest commit (which will be the top one) and `squash` or `s` all the rest. Once we save this, we will be asked to provide a comment for the new commit. The text that given to start with will contain all the comments from the commits that are getting combined. Whatever remains as uncommented will be used as the commit messege.

The part I don't like about this is that I have to squash commits that are local, if any of the squash commits have been pushed  to the remote repo, this won't work. If there was a way to squash commits in the remote repo I'd be able to totally clean things up, but then again, it may be for the best that the history in the remote repo can't so easily be rewritten.

The guide also describes how to "squash and merge" during pull requests in GitHub. I used this but I don't like it because after using this merge option the Network doesn't indicate that a merge was done: the branches in the network remain seperate.

### Install VSCode for WSL
[Guide](https://code.visualstudio.com/docs/remote/wsl)
Needed to have installed VSCode in the Windows side. In the Ubuntu terminal, go to the folder in which we want to work and start-up VSCode:

`$ code .` 

There is some first-time automatic set-up but once VSCode is open, at the bottom left I see that in green it says `WSL: Ubuntu-20.04`

Alternatively: To have VSCode looking at Ubuntu go to the bottom left and click on the green box then in the pop-up at the top select `New WSL Window using Distro...`. Now when we open a terminal we should see that it is a bash terminal and we have access to the python we just installed

### VSCode Extensions

* Vim
* Python
* PyLance?

### Install Python
We do want to install python within WSL: [guide](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/)

```
$ python3.10 --version
Python 3.10.X
```

give an [alias](https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3?newreg=a3ae2d11b44641baba3120c0f6ca6111)

`$ alias python = python3.10`
