# Makefile - use `make` or `make help` to get a list of commands.
#
# Note - Comments inside this makefile should be made using a single
# hashtag `#`, lines with double hash-tags will be the messages that
# printed in the help command

# Name of the current directory
PROJECTNAME=$(shell basename "$(PWD)")

# List of all Go-files to be processed
GOFILES=$(wildcard *.go)

# Redirecting error output to a file, acts as logs that can
# be referenced if needed
STDERR=/tmp/$(PROJECTNAME)-stderr.txt

# Docker image variables
IMAGE := $(PROJECTNAME)
VERSION := latest

# Ensures firing a blank `make` command default to help
.DEFAULT_GOAL := help

# Make is verbose in Linux. Make it silent
MAKEFLAGS += --silent


.PHONY: help
## `help`: Generates this help dialog the Makefile
help: Makefile
	@echo
	@echo " Commands available in "$(PROJECTNAME)":"
	@echo
	@sed -n 's/^[ \t]*##//p' $< | column -t -s ':' |  sed -e 's/^//'
	@echo

.PHONY: local-setup
## `local-setup`: Setup development environment locally
local-setup:
	@echo "  >  Ensuring directory is a git repository"
	git init &> /dev/null
	{%- if cookiecutter.use_precommit.lower() == 'y' -%}
	@echo "  >  Installing pre-commit"
	pip install --upgrade pre-commit &> /dev/null
	pre-commit install
	{% endif %}
	@echo "  >  Installing GolangCI-Lint"
	curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.42.1

# Will install missing dependencies
.PHONY: install
## `install`: Get dependencies and stuff needed to run the project
install:
	@echo "  >  Getting dependencies..."
	go get -v $(get)
	go mod tidy


.PHONY: codestyle
## :
## `codestyle`: Run code formatter(s)
codestyle:
	@echo -e "\n\t> Running Golang CI Lint"
	@golangci-lint run --fix

.PHONY: checkstyle
## `checkstyle`: Run linter(s) and check code-style
checkstyle:
	@echo -e "\t> Running Golang CI - Lint"
	@golangci-lint run


# Delibrately not revealing this command - designed to be consumed internally
.PHONY: --test-runner
--test-runner:
	@go test ./... -race -covermode=atomic -coverprofile=./coverage/coverage.txt -gcflags=-l
	@go tool cover -html=./coverage/coverage.txt -o ./coverage/coverage.html

.PHONY: test
## :
## `test`: Run fast and medium tests
test: export FAST_TEST="true"
test: export MEDIUM_TEST="true"
test: --test-runner

.PHONY: fast-test
## `fast-test`: Selectively run fast tests
fast-test: export FAST_TEST="true"
fast-test: --test-runner

.PHONY: medium-test
## `medium-test`: Selectively run medium tests
medium-test: export MEDIUM_TEST="true"
medium-test: --test-runner

.PHONY: slow-test
## `slow-test`: Selectively run long tests
slow-test: export SLOW_TEST="true"
slow-test: --test-runner


.PHONY: test-suite
## `test-suite`: Checkstyle and run ALL tests
test-suite: export FAST_TEST="true"
test-suite: export MEDIUM_TEST="true"
test-suite: export SLOW_TEST="true"
test-suite: checkstyle test


.PHONY: run
## :
## `run`: Run the project
##  : Optional; `make run q="args"` to pass arguments
run:
	go run main.go $(q)


.PHONY: docker-gen
## `docker-gen`: Create a new docker image for the project
docker-gen:
	@echo Building docker image \`$(IMAGE):$(VERSION)\`...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile


.PHONY: clean-docker
## `clean-docker`: Delete an existing docker image
clean-docker:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	@docker rmi -f $(IMAGE):$(VERSION)


## :
##  NOTE: All docker-related commands can contain `IMAGE`
## : and `VERSION` parameters to modify the docker
## : image being targeted
## :
## : Example;
## :     `make docker-gen NAME=go-template_v2 IMAGE=2.1.0`
