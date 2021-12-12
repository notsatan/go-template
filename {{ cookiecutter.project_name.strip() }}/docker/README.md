# Docker

**Note:** This section assumes you've already installed `docker` on your end, and know
how to use it!

This section guides you on how to use the [Makefile](../Makefile) to create (and remove)
a docker container for `{{ cookiecutter.project_name.strip() }}`!

## Installation

To create a new Docker container, you need to run:

```bash
make docker-gen
```

which is equivalent to:

```bash
make docker-gen VERSION=latest
```

You can also provide the name and version for the image to be created using the
variables `IMAGE` and `VERSION`.

Defaults; <br>

`IMAGE := {{ cookiecutter.project_name.strip() }}` <br>
`VERSION := latest` <br>

These values can be changed while executing any docker-related command from the Makefile

```bash
make docker-gen IMAGE=<some_name> VERSION=0.1.0
```


## Usage

Once you've created a docker container, to run the container, use

```bash
docker run -it --rm -v $(pwd):/workspace {{ cookiecutter.project_name.strip() }} bash
```

## Cleaning a docker image

To uninstall/remove a docker image run `make clean-docker` with `VERSION` (if required):

```bash
make clean-docker VERSION=0.1.0
```

Just like in installation, you can also choose the image name

```bash
make clean-docker IMAGE=<some_name> VERSION=latest
```
