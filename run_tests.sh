#!/bin/bash
set -e

SOURCE_TEST_DIR="build-tests"
TARGET_TEST_DIR="generated-tests"
BUILDER_VENV="venv"
MODEL_VENV=".model_venv"
MODEL="thesis"


if test -d $BUILDER_VENV ; then
	rm -rf $BUILDER_VENV
fi

python3 -m venv $BUILDER_VENV
. $BUILDER_VENV/bin/activate
pip install -U setuptools pip wheel
pip install -e .


if test -d $TARGET_TEST_DIR/$MODEL; then
	rm -rf $TARGET_TEST_DIR/$MODEL
fi

oarepo-compile-model ./$SOURCE_TEST_DIR/$MODEL.yaml --output-directory ./$TARGET_TEST_DIR/$MODEL -vvv

if test -d $MODEL_VENV ; then
	rm -rf $MODEL_VENV
fi

python3 -m venv $MODEL_VENV
. $MODEL_VENV/bin/activate
pip install -U setuptools pip wheel
pip install "./$TARGET_TEST_DIR/$MODEL[tests]"
pytest $TARGET_TEST_DIR/$MODEL/tests