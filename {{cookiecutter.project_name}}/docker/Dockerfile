# Dockerfile to generate docker image - the base docker image will simply copy the
# contents from the directory to the docker container, compile and generate a binary
# and run it.
#
# Uses multi-stage build to reduce the size of docker image.

FROM golang:1.16-alpine as builder

# Setup environmet variables - chores.
ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

# Create a build directory if one does not exist, and use it as the work directory
RUN mkdir -p /build
WORKDIR /build

# Copy code into the work directory
COPY . .

# Fetch all required modules, build and install them.
RUN go get -d -v ./...
RUN go install -v ./...

# Generate a compiled binary for the app
RUN go build -v -o go-template

# Create a new directory named `dist` in the parent, and copy the generated binary in it
RUN mkdir -p ../dist/ && cp -v ./go-template ../dist


# Create a new base image
FROM scratch

# Copy the generated binary from previous image to this one
COPY --from=builder /dist/go-template .

# Run the binary
CMD ["/go-template"]
