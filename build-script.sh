#!/bin/bash

# Inspired by https://github.com/HarukaNetwork/HarukaX/blob/master/build_cross.sh
# This script will generate binaries for the multiple OS/architectures, and a file
# containing SHA256 checksums for the binaries

# Directory where the binaries will be generated - created if does not exist
bin_path="./bin"

# File containing checksums - just the file name, file will be saved inside `bin_path`
checksums="checksums.txt"

# Basename for the generated binaries - name of the project for example
basename="go-template"

# Release version - can be blank if needed; if blank, will be populated by command-line
# arguments passed while running this script (if any).
version=""

if [[ "${version}" == "" ]]; then
  # If empty, populate `version` with the first argument passed to the script
  version="${1}"
fi

# Name pattern used for files being generated - will be appended with build system info
file_name="${basename}_${version}_"

# The final file path
full_path="${bin_path}/${file_name}"

# Remove existing binaries (if any)
rm -f "${full_path}"** # force-flag ensures no error message if no file is found

# Ensure `bin_path` exists, created if does not exist, ignored otherwise
mkdir -p "${bin_path}"

echo -e "\n\tGenerating binaries\n"

# Build linux targets
echo -e "\nBuilding for Linux"
echo -n " -> Targeting x86_64" # `-n` skips newline at the end
env GOOS=linux GOARCH=amd64 go build -o "${full_path}linux_x86_64"
echo -e ": Done"

echo -n " -> Targeting x86"
env GOOS=linux GOARCH=386 go build -o "${full_path}linux_x86"
echo -e ": Done"

echo -n " -> Targeting ARM"
env GOOS=linux GOARCH=arm go build -o "${full_path}linux_arm"
echo -e ": Done"

echo -n " -> Targeting ARM64"
env GOOS=linux GOARCH=arm64 go build -o "${full_path}linux_arm64"
echo -e ": Done"

# Build windows targets
echo -e "\n\nBuilding for Windows"

echo -n " -> Targeting x86_64"
env GOOS=windows GOARCH=amd64 go build -o "${full_path}windows_x86_64.exe"
echo -e ": Done"

echo -n " -> Targeting x86"
env GOOS=windows GOARCH=386 go build -o "${full_path}windows_x86.exe"
echo -e ": Done"

# Build mac targets
echo -e "\n\nBuilding for MacOS"

echo -n " -> Targeting x86_64"
env GOOS=darwin GOARCH=amd64 go build -o "${full_path}darwin_x86_64"
echo -e ": Done"

echo -n " -> Targeting ARM64"
env GOOS=darwin GOARCH=arm64 go build -o "${full_path}darwin_arm64"
echo -e ": Done"

echo -e "\nBinaries Generated Successfully!"
echo -ne "\nGenerating Checksums"

# Iterate through each file in output directory matching the pattern
flag=true
for file in "${full_path}"**; do
  if [[ "${flag}" == true ]]; then
    # Overwrite the file with this line
    sha256sum "$file" >"${checksums}"
    flag=false # mark flag as off
  else
    sha256sum "$file" >>"${checksums}"
  fi
done

echo -e ": Done"
echo -ne "Archiving Binaries"

cd "${bin_path}" || exit # Exit if `cd` fails

# Zip the windows executables
if ! command -v zip >/dev/null; then
  echo -e "\tZip not found, unable to generate archives for Windows executables"
else

  # Iterating through each executable file - to generate individual `.zip` files
  for file in "${file_name}"**".exe"; do
    zip_name="${file//.exe/}" # form name of the zip file - remove `.exe`

    # Create a zip container for the file, the `-m` flag deletes the original file
    zip "${zip_name}.zip" "${file}" -q -m
  done
fi

# Run GZip on Linux/Mac binaries
if ! command -v gzip >/dev/null; then
  echo -e "\tGZip not found, unable to generate archives"
else
  for file in "${file_name}"**; do
    if [[ "${file}" == "${file_name}"**".zip" ]]; then
      # Skip iteration over zip files
      continue
    fi

    gzip "${file}" -q
  done
fi

# Add these checksums to the text file as well
echo "" >>"${checksums}" # append new line
for file in "${file_name}"**; do
  sha256sum "$file" >>"${checksums}"
done

echo -e ": Done"
echo -e "\nExecution completed successfully \nBinaries stored in: \"${bin_path}\" \n"
