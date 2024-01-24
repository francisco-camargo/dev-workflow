Docker
======

[Return to top README.md](../../README.md)

# Install Docker on Ubuntu

[Guide](https://docs.docker.com/engine/install/ubuntu/#installation-methods), suggests Docker Desktop which includes the Docker GUI

[Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/) installation, which then points to:

[Docker Desktop for Ubuntu](https://docs.docker.com/desktop/install/ubuntu/) installation. From this page, download the DEB package.

Then, set up [Docker's Package Repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) by following the provided command line instructions.

To then verify that Docker Engine was successfully installed, run
```bash
sudo docker run hello-world
```

Then return to the Docker Desktop for Ubuntu installation instructions.

# Launch Docker Desktop
To start Docker Desktop for Linux, search Docker Desktop on the Applications menu and open it.

Or instead, from the terminal, run
```bash
systemctl --user start docker-desktop
```

# Sign in into Docker Desktop
If you are unable to sign in into Docker Desktop for Linux, it may be because you much [enable `pass`](https://docs.docker.com/desktop/get-started/#signing-in-with-docker-desktop-for-linux)