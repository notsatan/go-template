## Docker

This section guides you on how to use the [Makefile][makefile] to create (and remove)
a docker container for `{{ cookiecutter.project_name.strip() }}`!

> **Note:** This section assumes you've already installed [`docker`](https://www.docker.com)
on your end, and know how to use it!


## Installation

To create a new Docker container, you need to run:

```bash
make docker-gen
```

You can also provide the name and version for the image to be created using the
variables `IMAGE` and `VERSION`. The above command is equivalent to;

```bash
make docker-gen IMAGE={{ cookiecutter.project_name.strip() }} VERSION=latest
```

The default values for these environment variables are; <br>

```bash
IMAGE := {{ cookiecutter.project_name.strip() }}
VERSION := latest
```

These values can be changed when executing docker commands through the Makefile

```bash
make docker-gen IMAGE=<some_name> VERSION=<version_number>
```


## Usage

Once you've created a docker container, to run the container, use

```bash
docker run {{ cookiecutter.project_name.strip() }}
```

[makefile]: (../Makefile)
