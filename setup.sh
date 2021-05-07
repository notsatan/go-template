# Sets up the project with dependencies needs for local testing/linting

# Name of the temporary directory in which compiled binaries will be stored.
temp_directory="tmp"

# List of binaries that will be installed
binaries=(golangci-lint)

echo -e "\nInstalling Golang CI - Lint"
curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.34.1

# Fetching the location of the compiled binaries.
gopath=$(go env GOPATH)

# Creating a directory named `tmp` - command will be ignored if the directory exists
mkdir -p "./${temp_directory}"

path=$(pwd)

# Switching over to the path in GoRoot containing the compiled binaries.
cd "${gopath}/bin/"

# Moving all the binaries into the directory.
for file in "${binaries[@]}"; do
  mv "${file}" "${path}/tmp/"
done

echo -e "\n\nExecution completed. Compiled binaries are now stored in \`${path}/${temp_directory}\`\n"
