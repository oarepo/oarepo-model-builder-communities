#!/bin/bash
set -e

OAREPO_VERSION=${OAREPO_VERSION:-12}

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

curl -L -o forked_install.sh https://github.com/oarepo/nrp-devtools/raw/main/tests/forked_install.sh
if test -d $TARGET_TEST_DIR/$MODEL; then
	rm -rf ${TARGET_TEST_DIR/$MODEL:?}
fi

oarepo-compile-model ./$SOURCE_TEST_DIR/$MODEL.yaml --output-directory ./$TARGET_TEST_DIR/$MODEL -vvv

python3 -m venv $TESTS_VENV
. $TESTS_VENV/bin/activate
pip install -U setuptools pip wheel
pip install "oarepo[tests]==$OAREPO_VERSION.*"
pip install "./$TARGET_TEST_DIR/${MODEL}[tests]"

sh forked_install.sh invenio-records-resources
sh forked_install.sh invenio-requests
sh forked_install.sh invenio-drafts-resources
pip install oarepo-global-search
pip install oarepo-workflows
# editable_install /home/ron/prace/oarepo-communities

pytest $TARGET_TEST_DIR/$MODEL/tests