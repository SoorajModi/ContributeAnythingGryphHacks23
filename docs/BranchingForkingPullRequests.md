# Git branching, forking, and pull requests

## Branching

### Description

Git branching allows developers to work on different features or fixes without affecting the main codebase. Branches are created from the main branch (sometimes called 'master') and can be merged back into the main branch once the changes are complete.

This feature is particularly useful when multiple developers are working on the same codebase, as it allows them to work separately without interfering with each other's work.

### Diagram

```
  A -- B -- C -- D -- H  (main)
         \\          /
          E -- F -- G    (feature)
```

In diagram, `feature` branch has been merged into `main` after completing the work on the new feature. The merged commit is labeled as `H`.

### Commands

To create a new branch in Git, use the following command:

```
git branch [branch-name]
```

To switch to a different branch, use:

```
git checkout [branch-name]
```

To merge a branch into the main branch, use:

```
git merge [branch-name]
```

## Forking

Forking is the process of creating a copy of a repository (usually on a different account) to make changes independently. Forking is often used when a developer wants to contribute to an open-source project but doesn't have write access to the original repository.

To fork a repository on GitHub, click on the 'Fork' button on the repository's page. This will create a copy of the repository under your account, which you can then clone to your local machine and make changes to.

## Pull Requests

A pull request (or PR) is a way to propose changes to a codebase. Pull requests are used in open-source projects, where developers contribute code to a project that they don't have write access to. 

To create a pull request, make changes to a branch (either your own or a forked branch), commit the changes, and push the changes to the repository. Then, on GitHub, navigate to the repository and click on the 'New pull request' button. Select the branch that you want to merge into the main branch and create the pull request.

Pull requests are reviewed by the repository owner or a designated reviewer, who can accept or reject the changes. Once the changes are accepted, they are merged into the main codebase.