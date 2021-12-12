package main

import (
	"fmt"

	"{{ cookiecutter.go_module_path.strip('/') }}/src"
)

// title contains the name of the project
const title = "{{ cookiecutter.project_name.strip() }}"

/*
ProjectName returns the value of `title` string
*/
func ProjectName() string {
	return title
}

func main() {
	fmt.Printf("Running project: %s\n", src.ProjectName())
}
