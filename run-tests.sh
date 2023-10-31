#!/bin/bash
set -e

OAREPO_VERSION=${OAREPO_VERSION:-11}
OAREPO_VERSION_MAX=$((OAREPO_VERSION+1))


SOURCE_TEST_DIR="build-tests"
TARGET_TEST_DIR="generated-tests"
BUILDER_VENV=".venv-builder"
TESTS_VENV=".venv-tests"
MODEL="thesis"


if test -d $BUILDER_VENV ; then
	rm -rf $BUILDER_VENV
fi

python3 -m venv $BUILDER_VENV
. $BUILDER_VENV/bin/activate
pip install -U setuptools pip wheel
pip install -e .


if test -d $TARGET_TEST_DIR/$MODEL; then
	rm -rf ${TARGET_TEST_DIR/$MODEL:?}
fi

oarepo-compile-model ./$SOURCE_TEST_DIR/$MODEL.yaml --output-directory ./$TARGET_TEST_DIR/$MODEL -vvv

if test -d $TESTS_VENV ; then
	rm -rf $TESTS_VENV
fi

python3 -m venv $TESTS_VENV
. $TESTS_VENV/bin/activate
pip install -U setuptools pip wheel
pip install "oarepo>=$OAREPO_VERSION,<$OAREPO_VERSION_MAX"
pip install "./$TARGET_TEST_DIR/${MODEL}[tests]"
pytest $TARGET_TEST_DIR/$MODEL/tests