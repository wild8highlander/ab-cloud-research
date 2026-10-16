# 06_code Makefile
SHELL := /bin/bash
PY ?= python3

.PHONY: all smoke build-rs build-go test
all: smoke

smoke:
        $(PY) python/run.py doctor
        bash bash/run.sh doctor
        node js/run.js doctor

build-rs:
        cd rust && cargo build --release

build-go:
        cd go && go build -o run .

test:
        cd $(dir $(abspath $(lastword $(MAKEFILE_LIST)))).. && $(PY) -m pytest 09_tests/python -q
