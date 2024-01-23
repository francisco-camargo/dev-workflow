Vim
===

[Return to top README.md](../../README.md)

# Install Vim on Linux

Commands to install Vim to be used within the terminal

```bash
sudo apt update
sudo apt install vim
```

# Vim on VSCode

If you use VSCode you can also use Vim via the **Vim** extension, and you can learn Vim via the **Learn Vim** extension. The **Learn Vim** [book](https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/dedication/), and [reference](https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/cheatsheet) of Vim commands.

[Guide](https://hoitz.medium.com/improved-vim-setup-in-visual-studio-code-bc579501b80c) on how to customize Vim keybindings within VSCode.

# Vim Commands

## Normal Mode

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
* [Copy and paste guide](https://phoenixnap.com/kb/cut-copy-paste-vim)
  * Copy
    * Everything to the right: `y$`
    * (Almost) everything to the left: `y^`
    * Entire line: `yy`
    * Word with its trailing whitespace: `yaw`
    * Word without its trailing whitespace: `yiw`
    * `yfx`
    * `ytx`
  * Paste
    * `P`
    * `"0p` paste last yanked string, instead of paste last cut string
  * Cut
    * Current line: `dd`
    * Everything to the right: `d$`

## Visual Mode

This is the mode used to highlight text, [guide](https://phoenixnap.com/kb/cut-copy-paste-vim).

* Highlight current word: `viw`
