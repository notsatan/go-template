## Docker

This section guides you on how to use the [Makefile][makefile] to create (and remove)
a docker containers for `{{ cookiecutter.project_name.strip() }}`!

> **Note:** This section assumes you've already installed [`docker`](https://www.docker.com)
on your end, and know how to use it!


## Installation

To create a new Docker container, use the command:

```bash
make docker-gen
```

You can modify the name and version for the image to be created using the variables
`IMAGE` and `VERSION`. The above command is equivalent to;

```bash
make docker-gen IMAGE={{ cookiecutter.project_name.strip() }} VERSION=latest
```

By default, the values for these environment variables are; <br>

```bash
IMAGE := {{ cookiecutter.project_name.strip() }}
VERSION := latest
```

The values of these environment variables can be customized when executing any docker
command through the Makefile

```bash
make docker-gen IMAGE=<some_name> VERSION=<version_number>
```


## Usage

Once you've created a docker container, to run the container, use

```bash
docker run {{ cookiecutter.project_name.strip() }}
```

## Cleaning a docker image

To remove a docker image run `make clean-docker` with `VERSION` or `IMAGE` (if needed):

```bash
make clean-docker
```

If you want to target a specific image, you can use the long-form version

```bash
make clean-docker IMAGE=<name> VERSION=<specific_version>
```

Running a simple `make clean-docker` is the same as

```bash
make clean-docker IMAGE={{ cookiecutter.project_name.strip() }} VERSION=latest
```


## Debug Image

The [dockerfile](./Dockerfile) for *{{ cookiecutter.project_name.strip() }}* uses
[multistage builds][multistage] to generate light-weight docker images.

Images generated using the `make docker-gen` command use [`scratch`][scratch_image] as
the base image for the final build stage - these images are referred to as *production*
images.

While this allows creating extremely small images, at the same time these images are
very minimal, which makes it very difficult to debug applications - as an example,
the production image cannot be `shell`-ed into!

To resolve this, the [Makefile][makefile] allows you to create debug-friendly docker
images. These images use `golang:{{ cookiecutter.go_version }}` as base for the final
image. The resulting image is a lot larger compared to production images, on the other
hand, it comes with the tools you'll need to debug applications inside docker containers!

To create a debug-friendly docker images, use the command

```bash
make docker-debug
```

Similar to `docker-gen`, you can modify the name/version for the final image using
environment variables `IMAGE` and `VERSION`. The previous command is the same as

```bash
make docker-debug IMAGE={{ cookiecutter.project_name.strip() }}-debug VERSION=latest
```

> P.S. Notice that for the sake of clarity, debug images will **always** have their
> name appended with `-debug`!

You can run the image generated as

```bash
docker run {{ cookiecutter.project_name.strip() }}-debug
```

And, `shell` into a running debug image with;

```bash
docker run --rm -it {{ cookiecutter.project_name.strip() }}-debug bash
```

[makefile]: ../Makefile
[scratch_image]: https://hub.docker.com/_/scratch
[multistage]: https://docs.docker.com/develop/develop-images/multistage-build/
