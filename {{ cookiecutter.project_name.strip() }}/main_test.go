package main

import (
	"os"
	"testing"
)

const (
	envProd  = "production_mode"
	envDebug = "debug_mode"
	envBuild = "__BUILD_MODE__"
)

func resetEnv() {
	// Unset all environment variables
	os.Unsetenv(envProd)
	os.Unsetenv(envDebug)
	os.Unsetenv(envBuild)
}

func TestMain(m *testing.M) {
	// Run all tests, unset env variables, and exit
	resetEnv()
	val := m.Run()
	resetEnv()
	os.Exit(val)
}

func TestMainMethod(_ *testing.T) {
	main()
}

func dirtyCheck(t *testing.T, val01, val02 bool) {
	t.Helper()

	if val01 != val02 {
		t.Errorf("Values don't match: (%v, %v)", val01, val02)
	}
}

func TestFirst(t *testing.T) {
	resetEnv()
	dirtyCheck(t, firstCheck(), false) // no variable should be detected

	os.Setenv(envProd, "production")
	dirtyCheck(t, firstCheck(), true) // detect `production` mode

	resetEnv()
	os.Setenv(envDebug, "debug")
	dirtyCheck(t, firstCheck(), true) // detect `debug` mode
}

func TestSecond(t *testing.T) {
	resetEnv()
	dirtyCheck(t, secondCheck(), false) // no variable should be detected

	resetEnv()
	os.Setenv(envBuild, "production")
	dirtyCheck(t, secondCheck(), true) // detect `production` mode!

	resetEnv()
	os.Setenv(envBuild, "debug")
	dirtyCheck(t, secondCheck(), true) // detect `debug` mode!
}
