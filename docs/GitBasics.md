# Git Basics

Git is a version control system that helps in tracking changes in files, coordinating work between multiple people, and working on different versions of files. It is a command-line tool that can be used to manage and track changes in code and other files.

## Setup Commands

- `git config` sets up your email address and name so changes can be attributed to you.

```bash
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

## Basic Commands

- `git init` creates a new repository for you to start tracking changes in your code.
    
    ```bash
    $ git init my-project
    ```
    
- `git clone` creates a local copy of a remote repository, allowing you to work on the code locally.
    
    ```bash
    $ git clone <https://github.com/user/repo.git>
    ```
    
- `git add` adds changes to the staging area so that they can be committed to the repository.
    
    ```bash
    $ git add README.md
    ```
    
- `git commit` saves the changes you have made to the repository, along with a commit message describing the changes.
    - `git commit -am` adds and commits changes with a message in one step.
    
    ```bash
    $ git commit -m "Add README.md"
    ```
    
- `git status` shows the current status of the repository, including any changes that have been made since the last commit.
    
    ```bash
    $ git status
    ```
    
- `git log` displays the commit history of the repository, including the author, date, and commit message for each commit.
    
    ```bash
    $ git log
    ```
    
- `git push` pushes the changes you have made to a remote repository, such as one hosted on a Git hosting service like GitHub or GitLab.
    
    ```bash
    $ git push origin
    ```
    
- `git pull` fetches changes from a remote repository and merges them with your local repository.
    
    ```bash
    $ git pull origin
    ```
    

## Setting up a new project example

To set up a new coding project and add a [README.md](http://readme.md/) to a GitHub repository and push it, follow these steps:

1. Create a new project directory on your local machine.
    
    ```bash
    $ mkdir my-project
    ```
    
2. Navigate to the new project directory.
    
    ```bash
    $ cd my-project
    ```
    
3. Initialize the directory as a Git repository.
    
    ```bash
    $ git init
    ```
    
4. Create a new [README.md](http://readme.md/) file in the project directory.
    
    ```bash
    $ touch README.md
    ```
    
5. Add some content to the [README.md](http://readme.md/) file.
    
    ```bash
    $ echo "Hello world" >> README.md
    ```
    
6. Add the [README.md](http://readme.md/) file to the staging area.
    
    ```bash
    $ git add README.md
    ```
    
7. Commit the changes to the repository with a commit message.
    
    ```bash
    $ git commit -m "Add README.md"
    ```
    
8. Create a new repository on GitHub.
9. Add the remote repository URL as a remote in your local repository.
    
    ```bash
    $ git remote add origin <https://github.com/user/repo.git>
    ```
    
10. Push the local repository to the remote repository on GitHub.
    
    ```bash
    $ git push -u origin main
    ```
