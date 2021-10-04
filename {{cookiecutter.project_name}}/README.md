## go-template

Work in progress. 

A simple repository to act as a template to create Go projects. Created for my personal needs, public visibilty just in case this repo might inspire someone else to make something even better ;)

If you're using this template, be sure to generate an [Upload Token](https://docs.codecov.io/docs/frequently-asked-questions#where-is-the-repository-upload-token-found) through [Codecov](https://codecov.io), and set it as a [secret](https://docs.github.com/en/actions/reference/encrypted-secrets) on Github named `CODECOV_TOKEN`

List of places to modify project name
  - GitHub actions ([Linter](../.github/workflows/linter.yml), [Testing](../.github/workflows/testing.yml))
  - Docker ([Dockerfile](docker/Dockerfile), [Readme](docker/README.md))
  - [Build Script](build-script.sh)
  - [go.mod](go.mod)
  - [main.go](main.go)
  - [Readme](README.md)

Additionally, you may want to modify/remove/replace the [license](LICENSE) as well.

Pull Requests are welcome.

### ToDo
  - Add support for cookiecutter or something similar?
  - Improve this readme (seriously!)
