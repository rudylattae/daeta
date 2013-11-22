#!/bin/sh

# setup our development venv and activate it
deactivate
rm -rf *.pyc
tox -e dev "$@"
. .tox/dev/bin/activate
