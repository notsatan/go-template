# Makefile - use `make help` to get a list of possible commands.
#
# Note - Comments inside this makefile should be made using a single
# hashtag `#`, lines with double hash-tags will be the messages that
# are printed with during the `make help` command.

# Setting up some common variables.
PROJECTNAME=$(shell basename "$(PWD)")

# Go related variable(s)
GOFILES=$(wildcard *.go)

# Redirecting error output to a file, can be displayed it during development.
STDERR=/tmp/$(PROJECTNAME)-stderr.txt

# Variables used in the docker image.
IMAGE := $(PROJECTNAME)
VERSION := latest

# Setting `help` to be the default goal of the make file - ensures firing a blank
# `make` command will print help.
.DEFAULT_GOAL := help

# Make is verbose in Linux. Make it silent.
MAKEFLAGS += --silent

.PHONY: help
## `help`: Generates help dialog for the Makefile
help: Makefile
	@echo
	@echo " Commands available in "$(PROJECTNAME)":"
	@echo
	@sed -n 's/^[ \t]*##//p' $< | column -t -s ':' |  sed -e 's/^//'
	@echo

.PHONY: run
## `run`: Run the main project file
##  : Optional; `make run q="args"` to pass arguments
run:
	go run main.go $(q)

# Will install missing dependencies
.PHONY: install
## `install`: Installs missing dependencies
install:
	@echo "  >  Getting dependency..."
	go get -v $(get)
	go mod tidy

.PHONY: local-setup
## `local-setup`: Setup development environment locally
local-setup:
	@echo "Setting up pre-commit"
	pip install pre-commit
	pre-commit install
	@echo "Installing testing environment"
	bash ./setup.sh

.PHONY: codestyle
## `codestyle`: Auto-Format code using GoFmt and GoImports
codestyle:
	@echo -e "\n\t> Running Golang CI Lint"
	@./tmp/golangci-lint run --fix

.PHONY: checkstyle
## `checkstyle`: Run linter(s) and check code-style
checkstyle:
	@echo -e "\t> Running Golang CI - Lint"
	@./tmp/golangci-lint run

.PHONY: test
## `test`: Run tests and generate coverage report
test:
	@go test ./... -race -covermode=atomic -coverprofile=./coverage/coverage.txt -gcflags=-l
	@go tool cover -html=./coverage/coverage.txt -o ./coverage/coverage.html

.PHONY: test-suite
## `test-suite`: Check-styles and run tests with a single command
test-suite: checkstyle test

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
