package main

import "fmt"

// Title is a string containing the name of the project
const Title = "go-template"

/*
ProjectName acts as an (unnecessary) wrapper over the Title string.
*/
func ProjectName() string {
	return Title
}

func main() {
	fmt.Println("Hello World")
}
