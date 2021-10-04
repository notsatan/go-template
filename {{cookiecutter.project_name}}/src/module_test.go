package src

import (
	"testing"
)

func TestModuleName(t *testing.T) {
	if ProjectName() != "{{ cookiecutter.project_name }}" {
		t.Errorf("Project name `%s` incorrect", ProjectName())
	}
}
