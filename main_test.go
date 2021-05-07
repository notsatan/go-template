package main

import "testing"

func TestProjectName(t *testing.T) {
	if ProjectName() != Title {
		t.Errorf("(/main) project title does not match")
	}
}

func TestMainMethod(_ *testing.T) {
	main()
}
