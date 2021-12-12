# How to contribute

When contributing to this repository, you are recommended to discuss the change
you wish to make via an issue, email, or any other method with the owners of
this repository before the implementation

Note that we have a [code of conduct](./CODE_OF_CONDUCT.md) - please adhere to
it during all your interactions with the contributors.

## Commits

 - Make sure each commit is incremental - i.e. it adds value to the codebase
 - Commits should pass all tests - use `make test-suite` to run tests locally
 - Intermediate or test commits should not be a part of PR's/production branch
 - Rebase to update development branches instead of merge

## Dependencies

 - It is **strongly recommended** to get in touch with project owners before
    introducing new dependencies
 - Ensure project does not contain unused dependencies - run `go mod tidy` to
    remove unused dependencies
 - Avoid importing packages for minor stuff - Go isn't Javascript
 - Prefer to use the standard library where possible

## Project Setup

It is **strongly recommended** to raise an issue before making changes to the
project setup - i.e. changes to Makefile, pre-commit or GolangCI configs,
dockerfile, workflows, etc - these changes can potentially affect all
contributors and need to be discussed in-detail

## General

 1. If there is an already existing issue, make sure it's assigned to you when
      you start working on it
 2. Raise an issue if there isn't one already
 3. The points above can be ignored for minor stuff - you don't need to raise
      an issue to correct a typo - use common sense
