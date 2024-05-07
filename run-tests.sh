#!/bin/bash
set -e

OAREPO_VERSION=${OAREPO_VERSION:-11}

SOURCE_TEST_DIR="build-tests"
TARGET_TEST_DIR="generated-tests"
MODEL="thesis"
BUILDER_VENV=".venv-builder"
TESTS_VENV=".venv-tests"

if test -d $BUILDER_VENV ; then
	rm -rf $BUILDER_VENV
fi

if test -d $TESTS_VENV ; then
	rm -rf $TESTS_VENV
fi

python3 -m venv $BUILDER_VENV
. $BUILDER_VENV/bin/activate
pip install -U setuptools pip wheel
pip install -e .


if test -d $TARGET_TEST_DIR/$MODEL; then
	rm -rf ${TARGET_TEST_DIR/$MODEL:?}
fi
#editable_install /home/ron/prace/oarepo-model-builder-drafts
oarepo-compile-model ./$SOURCE_TEST_DIR/$MODEL.yaml --output-directory ./$TARGET_TEST_DIR/$MODEL -vvv

python3 -m venv $TESTS_VENV
. $TESTS_VENV/bin/activate
pip install -U setuptools pip wheel
pip install "oarepo[tests]==$OAREPO_VERSION.*"
pip install "./$TARGET_TEST_DIR/${MODEL}[tests]"

#editable_install /home/ron/prace/oarepo-communities
#editable_install /home/ron/prace/oarepo-global-search

pytest $TARGET_TEST_DIR/$MODEL/tests