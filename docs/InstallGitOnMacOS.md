# How to Install Git on MacOS

Git is a version control system used by developers to manage source code. If you're a MacOS user, you can easily install Git on your system using either Homebrew or the official Git installer. This guide will walk you through both methods.

## Installing Git Using Homebrew

1. If you don't already have Homebrew installed, open Terminal and run the following command:

```bash
/bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh>)"
```

1. Once Homebrew is installed, run the following command to install Git:

```bash
brew install git
```

1. Wait for the installation to complete. You can verify that Git was installed correctly by running the following command:

```bash
git --version
```

## Installing Git Using the Official Git Installer

1. Go to the [Git website](https://git-scm.com/downloads) and download the latest version of Git for MacOS.
2. Double-click the downloaded file to open the Git installer.
3. Follow the prompts in the installer to complete the installation.
4. Once the installation is complete, open Terminal and run the following command to verify that Git was installed correctly:

```bash
git --version
```

That's it! You now have Git installed on your MacOS system, and you can start using it to manage your source code.
