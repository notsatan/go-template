# Docker Container

## Installation

To create a new Docker container, you need to run:

```bash
make docker-gen
```

which is equivalent to:

```bash
make docker-gen VERSION=latest
```

You could also provide name and version for the image with the command.

Defaults;
`IMAGE := go-template`
`VERSION := latest`.

These values can be changed while executing any docker-related command from the Makefile

```bash
make docker-gen IMAGE=some_name VERSION=0.1.0
```

## Usage

```bash
docker run -it --rm \
   -v $(pwd):/workspace \
   go-template bash
```

## Cleaning a docker image

To uninstall/remove a docker image run `make clean-docker` with `VERSION` (if required):

```bash
make clean-docker VERSION=0.1.0
```

Just like in installation, you can also choose the image name

```bash
make clean-docker IMAGE=some_name VERSION=latest
```
