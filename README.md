# Learn to Develop with Ubuntu

## Goal

I want to learn to use Ubuntu to develop. Will do this both via the Windows Subsystem for Linux (WSL)  on one machine and from a machine with Ubuntu installed as the OS.

I also want to learn to use VSCode in conjuction with using Ubuntu.

## Clone repo

`$ git clone https://github.com/francisco-camargo/learn_ubuntu.git`


## Getting Started

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

### Install Vim

Commands to install Vim to be used within the terminal

```
$ sudo apt update
$ sudo apt install vim
```

### Install Python
We do want to install python within WSL: [guide](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/)

```
$ python3.10 --version
Python 3.10.X
```

give an [alias](https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3?newreg=a3ae2d11b44641baba3120c0f6ca6111)

`$ alias python = python3.10`

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
#### git squash
[Guide](https://www.git-tower.com/learn/git/faq/git-squash) to using `rebase` to squash commits together. Also describes how to "squash and merge" during pull requests.

Trying to just use "squash and merge" for pull requests. Note sure how commit messeges with appear.

dev commit 2

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
