# VSCode

[Return to top README.md](../../README.md)

Using Sync via my personal GitHub account to sync my VSCode settings across machines.

I use the **Dark+** color theme.

## (Optional) Install VSCode for WSL

[Guide](https://code.visualstudio.com/docs/remote/wsl)
Needed to have installed VSCode in the Windows side. In the Ubuntu terminal, go to the folder in which we want to work and start-up VSCode:

`code .`

There is some first-time automatic set-up but once VSCode is open, at the bottom left I see that in green it says `WSL: Ubuntu-20.04`

Alternatively: To have VSCode looking at Ubuntu go to the bottom left and click on the green box then in the pop-up at the top select `New WSL Window using Distro...`. Now when we open a terminal we should see that it is a bash terminal and we have access to the python we just installed

## VSCode Extensions

* Python
* PyLance
* (Optional) Vim
* (Optional) Learn Vim
* (Optional) Typora
  * I use the Native code block theme
* (Optional) vscode-pdf
* (Optional) Code Spell Checker
  * While cursor is on a word of interest, hit **Ctrl+.** to show spell checking options
* Docker
* Remote - SSH

## Open Settings

Open up the command pallette (**Ctrl+Shift+p**) and then choose from:

* `Preferences: Open Keyboard Shortcuts`
* `Preferences: Open Settings (UI)`
  * To then open up `settings.json` look for the `Open Settings (JSON)` button in the top right:

![1670895956782](image/README/1670895956782.png)

## VSCode Shortcuts

[Reference](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf) of VSCode shortcuts

Command palette
**Ctrl+Shift+p**

Open file
**Ctrl+p**

Tab windows: VSCode tabs can put placed into vertical slots. To place the current tab into a certain slot, use **Ctrl+Alt+#** where **#** can be 1, 2, etc. To switch **between** tabs within the same slot, use **Ctrl+Tab**. To switch between tabs, use **Ctrl+#**.

Switch between terminal and editor:
**Ctrl+`**

Debug console:
**Ctrl+Shift+y**

In the Settings page, look for Line Number; I like to use relative line numbers because it makes it easier to navigate with Vim.

## Using VSCode Remotely

[Guide](https://medium.com/@christyjacob4/using-vscode-remotely-on-an-ec2-instance-7822c4032cff)
