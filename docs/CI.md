# CI Pipelines

To complement your submission, you are welcome to add a CI pipeline using GitHub actions.

## Purpose

Continous Integration (CI) pipelines promote collaboration, automation, and quality assurance in software development. They help teams deliver software faster, with fewer bugs, and greater confidence in the stability of their codebase.

- Typically include automated tests, code style enforcement, that validate the functionality and quality of software. Running these tests as part of the CI process provides rapid feedback to help catch bugs and regressions early, allowing developers to address issues promptly and maintain software stability.
- CI pipelines enforce a standardization proces for code integration and testing across the development team or organization. By establishing consistent practices and automating repetitive tasks, CI pipelines ensure code changes are handled uniformly, regardless of individual developer preferences or expertise. This standardization promoses collaboration, improves code quality, and reduces the risk of errors cause by manual processes.
- CI pipelines can be extended to include Continous Deployment (CD), where successfully integrated and tested code changes are automatically deployed to production or staging environments. CD pipelines enable rapid and reliable software deployment, reducing the time between deployment and delivery to the end user, enabling teams to continously deliver code. CD will not be used for this repo, but it is something you will encounter on established projects.

## Requirements

- CI pipeline is added under `.github/workflows`
- File is named with the following format: `{name-of-project}-ci.yml`, for example `hello-world-ci.yml`
- All pipelines must use GitHub actions
- Pipeline runs on the following condition:
```
on:
  push:
    paths:
      - 'submissions/{name-of-project}/**'
  pull_request:
    branches:
      - main
```
- The pipelines are efficient
    - Use only one version for environments and languages
    - Only test what you need to test to ensure your contribution works as intended
