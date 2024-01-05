# Makefile - use `make` or `make help` to get a list of commands.
#
# Note - Comments inside this makefile should be made using a single
# hashtag `#`, lines with double hash-tags will be the messages that
# printed in the help command

# Name of the current directory
PROJECTNAME="{{ cookiecutter.project_name.strip() }}"

# List of all Go-files to be processed
GOFILES=$(wildcard *.go)

# Docker image variables
IMAGE := $(PROJECTNAME)
VERSION := latest

# Ensures firing a blank `make` command default to help
.DEFAULT_GOAL := help

# Make is verbose in Linux. Make it silent
MAKEFLAGS += --silent


.PHONY: help
## `help`: Generates this help dialog for the Makefile
help: Makefile
	echo
	echo " Commands available in \`"$(PROJECTNAME)"\`:"
	echo
	sed -n 's/^[ \t]*##//p' $< | column -t -s ':' |  sed -e 's/^//'
	echo


{% if cookiecutter.use_precommit.lower() == 'y' -%}
.PHONY: local-setup
## `local-setup`: Setup development environment locally
local-setup:
	echo "  >  Ensuring directory is a git repository"
	git init &> /dev/null
	echo "  >  Installing pre-commit"
	pip install --upgrade pre-commit &> /dev/null
	pre-commit install
{%- endif +%}


# Will install missing dependencies
.PHONY: install
## `install`: Fetch dependencies needed to run `{{ cookiecutter.project_name.strip() }}`
install:
	echo "  >  Getting dependencies..."
	go get -v $(get)
	go mod tidy


.PHONY: codestyle
## :
## `codestyle`: Run code formatter(s)
codestyle:
	golangci-lint run --fix


.PHONY: lint
## `lint`: Run linters and check code-style
lint:
	golangci-lint run


# No `help` message for this command - designed to be consumed internally
.PHONY: --test-runner
--test-runner:
	go test ./... -race -covermode=atomic -coverprofile=./coverage/coverage.txt
	go tool cover -html=./coverage/coverage.txt -o ./coverage/coverage.html


.PHONY: test
## :
## `test`: Run all tests
test: export TEST_MODE=complete
test: --test-runner


.PHONY: fast-tests
## `fast-tests`: Selectively run fast tests
fast-tests: export TEST_MODE=fast
fast-tests: --test-runner


.PHONY: slow-tests
## `slow-tests`: Selectively run slow tests
slow-tests: export TEST_MODE=slow
slow-tests: --test-runner


.PHONY: test-suite
## `test-suite`: Check code style, run linters and ALL tests
test-suite: export TEST_MODE=complete
test-suite: lint test


.PHONY: run
## :
## `run`: Run `{{ cookiecutter.project_name.strip() }}` in production mode
run: export production_mode=production
run: export __BUILD_MODE__=production
run:
	go run main.go $(q)

.PHONY: run-debug
## `run-debug`: Run `{{ cookiecutter.project_name.strip() }}` in debug mode
run-debug: export debug_mode=debug
run-debug: export __BUILD_MODE__=debug
run-debug:
	go run main.go $(q)


.PHONY: docker-gen
## :
## `docker-gen`: Create a production docker image for `{{ cookiecutter.project_name.strip() }}`
docker-gen:
	echo "Building docker image \`$(IMAGE):$(VERSION)\`..."
	docker build --rm \
		--build-arg final_image=scratch \
		--build-arg build_mode=production \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile


.PHONY: docker-debug
## `docker-debug`: Create debug-friendly docker images for `{{ cookiecutter.project_name.strip() }}`
docker-debug:
	echo "Building docker image \`$(IMAGE):$(VERSION)\`..."
	docker build --rm=false \
		--build-arg final_image=golang:{{ cookiecutter.go_version }} \
		--build-arg build_mode=debug \
		-t $(IMAGE)-debug:$(VERSION) . \
		-f ./docker/Dockerfile


.PHONY: clean-docker
## `clean-docker`: Delete an existing docker image
clean-docker:
	echo "Removing docker $(IMAGE):$(VERSION)..."
	docker rmi -f $(IMAGE):$(VERSION)


## :
##  NOTE: All docker-related commands can use `IMAGE`
## : and `VERSION` variables to modify the docker
## : image being targeted
## :
## : Example;
## :     make docker-gen IMAGE=new_project VERSION=3.15
## :
## : Likewise, both the `run` commands can pass runtime
## : arguments under the `q` arg
## :
## : Example;
## :	`make run q="time --version"`
