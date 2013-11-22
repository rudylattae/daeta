#!/bin/sh

# make sure it's good enough so we can push
flake8 daeta.py setup.py
checkit --doctest-extension=md --with-xunit