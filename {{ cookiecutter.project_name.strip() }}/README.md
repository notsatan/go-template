# {{ cookiecutter.project_name.strip() }}

{% if cookiecutter.github_specific_features.lower() == 'y' -%}
<div align="center">

[![Build Status](https://img.shields.io/github/checks-status/{{ cookiecutter.go_module_path.strip('/').replace('github.com/', '') }}/{{ cookiecutter.base_branch.strip() }}?color=black&style=for-the-badge&logo=github)][github-actions]
{% if cookiecutter.use_codecov.lower() == 'y' -%}
[![Code Coverage](https://img.shields.io/codecov/c/{{ cookiecutter.go_module_path.strip('/').replace('.com', '') }}?color=blue&logo=codecov&style=for-the-badge)][github-actions-tests]
{% endif -%}
[![Security: bandit](https://img.shields.io/badge/Security-GoSec-lightgrey?style=for-the-badge&logo=springsecurity)](https://github.com/securego/gosec)
[![Dependencies Status](https://img.shields.io/badge/Dependencies-Up%20to%20Date-brightgreen?style=for-the-badge&logo=dependabot)][dependabot-pulls]
[![Semantic Versioning](https://img.shields.io/badge/versioning-semantic-black?style=for-the-badge&logo=semver)][github-releases]
[![Pre-Commit Enabled](https://img.shields.io/badge/Pre--Commit-Enabled-blue?style=for-the-badge&logo=pre-commit)][precommit-config]
[![License](https://img.shields.io/github/license/{{ cookiecutter.go_module_path.strip('/').replace('github.com/', '') }}?color=red&style=for-the-badge)][project-license]
[![Go v{{ cookiecutter.go_version }}](https://img.shields.io/badge/Go-%20v{{ cookiecutter.go_version }}-black?style=for-the-badge&logo=go)][gomod-file]

{{ cookiecutter.project_description }}

</div>
{%- endif %}


## Initial Setup

This section is intended to help developers and contributors get a working copy of
`{{ cookiecutter.project_name.strip() }}` on their end

<details>
<summary>
    1. Clone this repository
</summary><br>

```sh
git clone https://{{ cookiecutter.go_module_path.strip('/') }}
cd {{ cookiecutter.go_module_path.strip('/').split('/')[-1] }}
```
</details>

<details>
<summary>
    2. Install `golangci-lint`
</summary><br>

Install `golangci-lint` from the [official website][golangci-install] for your OS
</details>
<br>


## Local Development

This section will guide you to setup a fully-functional local copy of `{{ cookiecutter.project_name.strip() }}`
on your end and teach you how to use it! Make sure you have installed
[golangci-lint][golangci-install] before following this section!

**Note:** This section relies on the usage of [Makefile][makefile-official]. If you
can't (or don't) use Makefile, you can follow along by running the internal commands
from [`{{ cookiecutter.project_name.strip() }}'s` Makefile][makefile-file] (most of which are
OS-independent)!

### Installing dependencies

To install all dependencies associated with `{{ cookiecutter.project_name.strip() }}`, run the
command

```sh
make install
```

{% if cookiecutter.use_precommit.lower() == 'y' -%}
### Setting up `pre-commit`

For a watered-down explanation, [pre-commit][pre-commit] hooks are an abstraction over
[git-hooks][githooks], allowing you to define a series of commands (or checks), that
would be automatically run every time you use the `git commit` command.

The pre-commit hooks used by `{{ cookiecutter.project_name.strip() }}` are located within the
[`.pre-commit-config.yml`][precommit-config] file. These hooks are configured to run;

 - Series of basic checks (JSON, YAML, XML file schema validation)
 - Checks for merge conflicts, and possible leaks of private keys
 - File formatters - whitespace trimming, end-of-file fixers
 - Checks for executable scripts
 - JSON formatters
 - Code Formatters
 - Test-suite

To install pre-commit, simply use the Makefile command

```sh
make local-setup
```

**Note**: To install (and use) `pre-commit`, make sure you have the latest stable
versions of [Python][python-install] and [pip][pip-install] installed!

The Makefile command will install *pre-commit* on your PC, and attach it to git
hooks -- ensuring pre-commit checks are run every time you use the `git commit` command!

### Using `pre-commit`

The [previous section](#setting-up-pre-commit) guided you to install pre-commit, ensuring
pre-commit runs implicitly *before ***every*** commit*.

However, if needed, you can use the `run` command to forcibly run `pre-commit` on all
staged files (i.e. files in staging area in git).

To manually run pre-commit on all files (including unstaged files), use

```sh
pre-commit run --all-files
```
{%- endif %}

### Using Code Formatters

Code formatters format your code to match pre-decided conventions. To run automated code
formatters, use the Makefile command

```sh
make codestyle
```

### Using Code Linters

Linters are tools that analyze source code for possible errors. This includes typos,
code formatting, syntax errors, calls to deprecated functions, potential security
vulnerabilities, and more!

To run pre-configured linters, use the command

```sh
make lint
```

### Running Tests

Tests in `{{ cookiecutter.project_name.strip() }}` are classified as *fast* and *slow* - depending
on how quick they are to execute.

To selectively run tests from either test group, use the Makefile command

```sh
make fast-test

OR

make slow-test
```

Alternatively, to run the complete test-suite -- i.e. *fast* and *slow* tests at one
go, use the command

```sh
make test
```

### Running the Test-Suite

The *`test-suite`* is simply a wrapper to run linters, stylecheckers and **all** tests
at once!

To run the test-suite, use the command

```sh
make test-suite
```

In simpler terms, running the test-suite is a combination of running [linters](#using-code-linters)
and [all tests](#running-tests) one after the other!
<br>


## Additional Resources

### Makefile help

<details>
<summary>
    Tap for a list of Makefile commands
</summary><br>

|     Command    	|                               Description                               	| Prerequisites 	|
|:--------------:	|:-----------------------------------------------------------------------:	|:-------------:	|
|     `help`     	| Generate help dialog listing all Makefile commands with description     	|       NA      	|
{% if cookiecutter.use_precommit.lower() == 'y' -%}
|  `local-setup` 	| Setup development environment locally                                   	|  python, pip  	|
{% endif -%}
|    `install`   	| Fetch project dependencies                                              	|       NA      	|
|   `codestyle`  	| Run code-formatters                                                     	| golangci-lint 	|
|     `lint`     	| Check codestyle and run linters                                         	| golangci-lint 	|
|     `test`     	| Run **all** tests                                                       	|       NA      	|
|  `fast-tests`  	| Selectively run *fast* tests                                            	|       NA      	|
|  `slow-tests`  	| Selectively run *slow* tests                                            	|       NA      	|
|  `test-suite`  	| Check codestyle, run linters and **tests** tests                        	| golangci-lint 	|
|      `run`     	| Run *{{ cookiecutter.project_name.strip().strip() }}*                           	|       NA      	|
|  `docker-gen`  	| Create production docker image for *{{ cookiecutter.project_name.strip().strip() }}* 	|     docker    	|
|  `docker-debug`  	| Create debug-friendly docker image for *{{ cookiecutter.project_name.strip().strip() }}* 	|     docker    	|
| `clean-docker` 	| Remove docker image generated by `docker-gen`                           	|     docker    	|

<br>
</details>

Optionally, to see a list of all Makefile commands, and a short description of what they
do, you can simply run

```sh
make
```

Which is equivalent to;

```sh
make help
```

Both of which will list out all Makefile commands available, and a short description
of what they do!

### Generating Binaries

To generate binaries for multiple OS/architectures, simply run

```sh
bash build-script.sh
```

The command will generate binaries for Linux, Windows and Mac targetting multiple
architectures at once! The binaries, once generated will be stored in the `bin`
directory inside the project directory.

The binaries generated will be named in the format

```text
{{ cookiecutter.project_name.strip() }}_<version>_<target-os>_<architecture>.<extension>
```

The `<extension>` is optional. By default, `version` is an empty string. A custom
version can be passed as an argument while running the script. As an example;

```sh
bash build-script.sh v1.2.1
```

An example of the files generated by the previous command will be;

```sh
{{ cookiecutter.project_name.strip() }}_v1.2.1_windows_x86_64.exe
```

{% if cookiecutter.github_specific_features.lower() == 'y' and cookiecutter.use_codecov.lower() == 'y' -%}
### Setting up Codecov

Follow [Codecov Docs][codecov-docs] to activate Codecov for your project repository.

Once you've activated Codecov for your project, you should be able to see the
`Repository Upload Token`. Copy this token, and add it as a secret to your Github
repository. Checkout [Creating secrets for a Repository][creating-secrets] for info
on how to add secrets on Github.

For the secret, the name of the secret should be "`CODECOV_TOKEN`" (no spaces,
copy-paste the string as it is). The value of the secret would be the
`Repository Upload Token` obtained from Codecov.

Save the secret, you should be able to a secret named `CODECOV_TOKEN` in the
*Settings > Secrets* section of your project repository. If this field is visible,
you are done with setting up Codecov, and should be able to see code coverage reports
after the next run of CI pipeline!
{%- endif %}

### Using Docker

To run `{{ cookiecutter.project_name.strip() }}` in a docker container, read the instructions in
[docker section](./docker).

### Running `{{ cookiecutter.project_name.strip() }}`

To run {{ cookiecutter.project_name.strip() }}, use the command

```sh
make run
```

Additionally, you can pass any additional command-line arguments (if needed) as the
argument "`q`". For example;

```sh
make run q="--help"

OR

make run q="--version"
```
<br>


{% if cookiecutter.github_specific_features.lower() == 'y' -%}
## Releases

You can check out a list of previous releases on the [Github Releases][github-releases]
page.

### Semantic versioning with Release Drafter

<details>
    <summary>
        What is Semantic Versioning?
    </summary><br>

Semantic versioning is a versioning scheme aimed at making software management easier.
Following semantic versioning, version identifiers are divided into three parts;

```sh
    <major>.<minor>.<patch>
```

> MAJOR version when you make incompatible API changes [breaking changes]<br>
> MINOR version when you add functionality in a backwards compatible manner [more features]<br>
> PATCH version when you make backwards compatible bug fixes [bug fixes and stuff]<br>

For a more detailed description, head over to [semver.org][semver-link]

</details>

[Release Drafter][release-drafter] automatically updates the release version as pull
requests are merged.

Labels allowed;

 - `major`: Affects the `<major>` version number for semantic versioning
 - `minor`, `patch`: Affects the `<patch>` version number for semantic versioning

Whenever a pull request with one of these labels is merged to the `master` branch,
the corresponding version number will be bumped by one digit!

### List of Labels

Pull requests once merged, will be classified into categories by
[release-drafter][release-drafter] based on pull request labels

This is managed by the [`release-drafter.yml`][release-drafter-config] config file.

|                   **Label**                   	|      **Title in Releases**      	|
|:---------------------------------------------:	|:-------------------------------:	|
| `security`                                    	| :lock: Security                 	|
| `enhancement`, `feature`,  `update`           	| :rocket: Updates                	|
| `bug`, `bugfix`, `fix`, `hotfix`              	| :bug: Bug Fixes                 	|
| `documentation`                               	| :memo: Documentation            	|
| `wip`, `in-progress`, `incomplete`, `partial` 	| :construction: Work in Progress 	|
| `dependencies`, `dependency`                  	| :package: Dependencies          	|
| `refactoring`, `refactor`, `tests`, `testing` 	| :test_tube: Tests and Refactor  	|
| `build`, `ci`, `pipeline`                     	| :robot: CI/CD and Pipelines     	|

The labels `bug`, `enhancement`, and `documentation` are automatically created by Github
for repositories. [Dependabot][dependabot-link] will implicitly create the
`dependencies` label with the first pull request raised by it.

The remaining labels can be created as needed!
{%- endif %}
<br>


## Credits

<div align="center"><br>

`{{ cookiecutter.project_name.strip() }}` is powered by a template generated using [`go-template`][go-template-link]

[![go-template](https://img.shields.io/badge/go--template-black?style=for-the-badge&logo=go)][go-template-link]

</div>

[makefile-file]: ./Makefile
[project-license]: ./LICENSE
[github-actions]: ../../actions
[github-releases]: ../../releases
[precommit-config]: ./.pre-commit-config.yaml
[gomod-file]: ../{{ cookiecutter.base_branch.strip() }}/go.mod
[github-actions-tests]: ../../actions/workflows/tests.yml
[dependabot-pulls]: ../../pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot

[semver-link]: https://semver.org
[pre-commit]: https://pre-commit.com
[github-repo]: https://github.com/new
[gitlab-repo]: https://gitlab.com/new
[dependabot-link]: https://dependabot.com
[githooks]: https://git-scm.com/docs/githooks
[python-install]: https://www.python.org/downloads
[release-drafter-config]: ./.github/release-drafter.yml
[makefile-official]: https://www.gnu.org/software/make
[pip-install]: https://pip.pypa.io/en/stable/installation
[codecov-docs]: https://docs.codecov.com/docs#basic-usage
[go-template-link]: https://github.com/notsatan/go-template
[golangci-install]: https://golangci-lint.run/usage/install
[cookiecutter-link]: https://github.com/cookiecutter/cookiecutter
[release-drafter]: https://github.com/marketplace/actions/release-drafter
[creating-secrets]: https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository
