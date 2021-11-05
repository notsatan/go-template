## go-template

<div align="center">

![Build status](https://img.shields.io/github/workflow/status/notsatan/go-template/Black?style=for-the-badge&logo=github)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-green?style=for-the-badge&logo=dependabot)
![MIT License](https://img.shields.io/github/license/notsatan/go-template?color=red&style=for-the-badge)
![Pre-Commit Enabled](https://img.shields.io/badge/Pre--Commit-Enabled-blue?style=for-the-badge&logo=pre-commit)
![Go v1.16+](https://img.shields.io/badge/Go-%20v1.16-black?style=for-the-badge&logo=go)
![Makefile Included](https://img.shields.io/badge/Makefile-Supported%20🚀-red?style=for-the-badge&logo=probot)

A bleeding-edge Go project generator for your next project :wink:

</div>

## TL;DR

```
cookiecutter gh:notsatan/go-template
```

***OR***

```
cookiecutter https:github.com/notsatan/go-template
```

And you're good to go! Jump to the [setup](#microscope-setup-instructions) section directly for quick setup instructions ;)

## :boom: Features

This is a battries-included [cookiecutter :cookie:](https://github.com/cookiecutter/cookiecutter) template to get you started with the essentials you'll need for your next Go project ;)

### Development

 - Supports `Go v1.16` and `Go v1.17`
 - Automated code formatting with [gofmt](https://pkg.go.dev/cmd/gofmt) and [gofumpt](https://github.com/mvdan/gofumpt)
 - Sort imports with [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports) and [gci](https://github.com/daixiang0/gci)
 - Ready to use [pre-commit](https://pre-commit.com/) setup, complete with a ton of hooks already configured in [`.pre-commit-config.yaml`](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.pre-commit-config.yaml)
 - Security checks with [gosec](https://github.com/securego/gosec), code duplication checks with [dupl](https://github.com/mibk/dupl), magic number checks with [go-mnd](https://github.com/tommy-muehle/go-mnd)
 - Pre-configured [`.editorconfig`](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.editorconfig), [`.dockerignore`](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.dockerignore) and [`.gitignore`](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.gitignore) - you won't have to bother with trivialities
 - Enforce better programming practices with [go-critic](https://github.com/go-critic/go-critic), [gocyclo](https://github.com/fzipp/gocyclo), [gocognit](https://github.com/uudashr/gocognit) and [stylecheck](https://github.com/dominikh/go-tools/tree/master/stylecheck)
 - Code linting with [golangci-lint](https://golangci-lint.run/), complete with a ready-to-run [`.golangci.yml`](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.golangci.yml) configuration file
 - Easy setup with [`Makefile`](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/Makefile) - run linters, check for codestyle, run tests and generate coverage reports - all with a single command
 - Multiple test modes supported by the Makefile - allowing you run tests as frequently as you need, without having to run long tests (>20 sec) *everytime* (ugh).


### Deployment

 - Github Actions with predefined [workflows](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.github/workflows) including CI/CD, release drafter and *optional* code coverage with [Codecov](http://codecov.com)
 - A simple [Dockerfile](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/docker/Dockerfile) with [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build) to containerize your apps while ensuring smallest possible image sizes
 - Always up-to-date dependencies with [@Dependabot](https://dependabot.com/) - enabled by default, remove [`dependabot.yml`](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.github/dependabot.yml)  to disable!
 - A simple [shell script](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/build-script.sh) to generate distributable binaries for multiple OS/architectures with checksums for verification
 - Automated release management with [Release Drafter](https://github.com/marketplace/actions/release-drafter), pre-configured to handle the default Github labels (and more) through [`release-drafter.yml`](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.github/release-drafter.yml)

### Community

 - Ready to use [pull request](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.github/PULL_REQUEST_TEMPLATE.md) and [issue](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.github/ISSUE_TEMPLATE) templates out of the box
 - Files such as `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` will be generated automatically.
 - [Semantic Versions](https://semver.org) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter)

## :microscope: Setup Instructions

### Installation

To start using the template, install the latest version of [`Cookiecutter`](https://cookiecutter.readthedocs.io/) (make sure you have Python and `pip` installed)

```sh
pip install -U cookiecutter
```

<br>
Once you have cookiecutter installed, move over to the directory where you want to generate your project and run

```sh
cookiecutter gh:notsatan/go-template
```

Alternatively, you can achieve the same results with the command

```sh
cookiecutter https://github.com/notsatan/go-template/
```

### Input Variables

Cookiecutter will ask you to fill some variables that will be used to generate your project from this template. This section lists all the input variables, their default values, and what they are used for

> Quick Note: Cookiecutter needs all inputs to have a default value. Many of the defaults for the setup resort to this repository (for example, the module path points to this Github repository, license owner name refers to me, etc)
>
> These defaults **must** be filled with actual values during the setup!
<br>

| Parameter                  | Default Value                     | Explanation                                                                                                                                                                                                          |
| -------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `project_name`             | go-template                       | Name of the project. A directory of this name will be created in the working directory containing the generated project                                                                                              |
| `project_description`      | Based on `project_name`           | A small description of the project, used to generate `GNU` license file, and default readme                                                                                                                          |
| `go_module_path`           | *github.com/notsatan/go-template* | Complete Go module path for the generated project, use Github path to enable Github specific features                                                                                                                |
| `license_owner`            | *notsatan*                        | Used in `LICENSE` and other files. Can be the name of a person or an organization.                                                                                                                                   |
| `contact_email`            | `""`                              | Email to get in touch with project stakeholders. `CODE_OF_CONDUCT.md` and `SECURITY.md` will be removed if empty. [<sup><sub>Why is this needed?</sub></sup>](#why-is-my-email-id-needed)                            |
| `github_specific_features` | **y**                             | Yes or No (`y` or `n`). Dictates if Github-specific features should be included in the project (issue templates, pipeline, etc). [<sup><sub>More Info</sup></sub>](#what-does-the-github_specific_features-field-do) |
| `use_codecov`              | **y**                             | Yes or No (`y` or `n`). Decides if [Codecov](http://codecov.com) is to be used in the project or not. [<sup><sub>Setting up codecov</sup></sub>](#how-to-integrate-codecov-for-automated-code-analysis)              |
| `use_precommit`            | **y**                             | Yes or No (`y` or `n`). Decides if [*pre-commit*](https://pre-commit.com) configs should be included with the generated templates                                                                                    |
| `go_version`               | `1.17`                            | The version of Go to use in the project. Can be either `1.16` or `1.17`                                                                                                                                              |
| `license`                  | `MIT`                             | The license you want to use in the generated project. One of `MIT`, `BSD-3`, `GNU GPL v3.0` and `Apache Software License 2.0`                                                                                        |

All input values entered while setting up the Cookiecutter template will be saved in `cookiecutter-config-file.yml` you can refer to them in the generated project if needed :wink:

### Post Installation

When Cookiecutter completes generating your project, move into the project directory. Let the Makefile install and setup the resources needed for the project to run locally, use

```sh
make local-setup
```

Once the Makefile command is done with the setup, be sure to install [GolangCI-Lint](https://golangci-lint.run/usage) (this won't be handled by the Makefile command). GolangCI is used to run a bunch of linters on your code, when integrated with the pre-commit config file, this would ensure multiple linters are automatically run on your codebase with every commit - and optionally every push to the `remote` if you have enabled the `linter` action

Head over to the [GolangCI-Lint website](https://golangci-lint.run/usage/install/) for installation instructions. And that's it. You should have your own project up and running by now :)

## :dart: What's Next

Start playing around with the generated template :')

If you're a beginner with Go, I would like to recommend some articles, blogs and other resources that helped me learn Go - these will (*hopefully*) be of some help to you

 - [Go Official Docs](https://golang.org/doc/): For Go, the official documentation is an excellent place to start learning. Highly recommened resource for beginners.
 - [Effective Go](https://golang.org/doc/effective_go): A blog post that is a part of the official documentation, yet important enough to be a separate point by itself! Gives you an in-depth idea of how to structure and write your Go code. Recommended read once you've learnt the basics of Go
 - [Uber's Style Guide for Go](https://github.com/uber-go/guide/blob/master/style.md): Slightly opionated at times, a great resource nevertheless. Gives a very detailed look at what "bad" Go code is, and how to rewrite it to be simpler and more effective. Recommended read for people with some experince in using Go (less so for people with no prior experience)
 - [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments): A part of the Go Wiki, can be seen as a supplement to Effective Go (mentioned above)
 - [50 Shades of Go](http://devs.cloudimmunity.com/gotchas-and-common-mistakes-in-go-golang/): A collection of common traps and gotcha's for Go devs! Recommended read once you start writing code in Go, not recommended for complete newbies - can potentially drown you with excess information

### General

Articles and resources which were of great help to me when making this template

 - [Github Actions Documentation](https://help.github.com/en/actions)
 - [Docker Multi-Stage Build Docs](https://docs.docker.com/develop/develop-images/multistage-build/)
 - [Docs for `codecov.yml`](https://docs.codecov.com/docs/codecov-yaml)
 - [GolangCI-Lint Configuration Docs](https://golangci-lint.run/usage/configuration/)


## :interrobang: FAQ

#### Why is my Email ID needed?

Like all other fields, the `contact_email` field is also optional. You can choose to leave this value blank, and the template will work normally.

The main usage for the email fields is to generate `CODE_OF_CONDUCT.md` and `SECURITY.md` - both of these need people to be able to get in touch with project stakeholders directly, either to report a violation of code of conduct, or a security bug - neither of which should be done publically.

> **Note:** If you choose to leave the email field blank, both `SECURITY.md` and `CODE_OF_CONDUCT.md` will not be a part of the generated project! Since both of these files require people to get in touch directly, not having an email ID makes these files be redundant. If you still want these files, you can manually add them to the generated project!

#### What does the `github_specific_features` field do?

Not every project generated using this template needs to be hosted on Github. There are many other Git hosting-providers out there, each of them as valid as Github.

Despite this, Github still happens to be the most popular code hosting platform - as such, projects generated through `go-template` include a lot of features that would ensure a very smooth development experience on Github, but would be redundant anywhere outside Github. Some examples of this would be Github pipelines, Github actions, issue templates, pull request templates, and more. In case you choose not to use Github, you can use this field to ensure that the generated project skips any Github-specific files/code.

> **Note:** If Github specific features are required, the value of `go_module_path` should be a path to a Github repository (doesn't matter if it exists). This would be used for `dependabot.yml`

#### How to integrate Codecov for automated code analysis?

[Codecov](http://codecov.com/) is a code analysis tool, `go-template` can generate a project with pre-configured support for Codecov code analysis. With Codecov enabled, the CI pipeline will generate a code coverage report everytime tests are run.

> **Note:** This requires Github workflows, as such, if you choose not to use Github features (using the `github_specific_features` field), or chose not to use Codecov (using the `use_codecov` field) - you'll have to setup this bit yourself.

Follow [Codecov Docs](https://docs.codecov.com/docs#basic-usage) to activate Codecov for your project repository.

Once you've activated Codecov for your project, you should be able to see the `Repository Upload Token`. Copy this token, and add it as a secret to your Github repository. Checkout [Creating secrets for a Repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) for info on how to add secrets on Github.

For the secret, the name of the secret should be "`CODECOV_TOKEN`" (no spaces, copy-paste the string as it is). The value of the secret would be the `Repository Upload Token` for this repository obtained from Codecov.

Save the secret, you should be able to a secret named `CODECOV_TOKEN` in the *Settings > Secrets* section of your project repository. If this field is visible, you are done with setting up Codecov, and should be able to see code coverage reports the next time you run your CI pipeline.

#### How do I fix `ValueError: Attempt to enable Github-specific features when module path does not belong to github`?

This error would be thrown when you chose to enable Github specific features, but, the Go module path you used does not match against Github. Currently, `go-template` uses the following regex expression to validate module paths

```regex
^github.com\/[a-zA-Z0-9\-]+\/[a-zA-Z0-9\-]+\/?$
```

The reason this check is needed is to ensure the [`dependabot.yml`](../../tree/master/%7B%7Bcookiecutter.project_name%7D%7D/.github/dependabot.yml) config will add the repository owner as a reviewer whenever dependabot raises a pull request for a dependency update.

## :trophy: Acknowledgements

The main inspiration behind this template was `TezRomacH`'s [python-package-template](https://github.com/TezRomacH/python-package-template) - which I've greatly enjoyed using at one point of time.

The lack of any similar templates for Go was a large part of why I decided to *Go ahead* and make one myself. And of course, huge appreciation for [Cookiecutter](https://github.com/cookiecutter/cookiecutter) - without which such a flexible template would not be possible.

## :shield: License

![MIT License](https://img.shields.io/github/license/notsatan/go-template?color=red&style=for-the-badge)

This project is licensed under the terms of the `MIT` license. See [LICENSE](./LICENSE) for more details.
