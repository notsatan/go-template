package main

import (
	"fmt"
	"{{ cookiecutter.module_root }}/{{ cookiecutter.module_name }}/src"
)

// title contains the name of the project
const title = "{{ cookiecutter.project_name }}"

/*
ProjectName returns the value of `title` string
*/
func ProjectName() string {
	return title
}

func main() {
	fmt.Printf("Running project: %s\n", src.ProjectName())
}
