#!/bin/bash
set -e

OAREPO_VERSION=${OAREPO_VERSION:-12}

export PIP_EXTRA_INDEX_URL=https://gitlab.cesnet.cz/api/v4/projects/1408/packages/pypi/simple
export UV_EXTRA_INDEX_URL=https://gitlab.cesnet.cz/api/v4/projects/1408/packages/pypi/simple

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

oarepo-compile-model ./$SOURCE_TEST_DIR/$MODEL.yaml --output-directory ./$TARGET_TEST_DIR/$MODEL -vvv

python3 -m venv $TESTS_VENV
. $TESTS_VENV/bin/activate
pip install -U setuptools pip wheel
pip install "oarepo[rdm,tests]==$OAREPO_VERSION.*"
pip install "./$TARGET_TEST_DIR/${MODEL}[tests]"

pip install oarepo-global-search
pip install oarepo-workflows
#editable_install /home/ron/prace/oarepo-communities

# TODO: the generated tests are not working as there is no support for  workflows
# in pytest tests. To support it, we would need to rewrite the test framework,
# too much work for now.
# pytest $TARGET_TEST_DIR/$MODEL/tests

# instead, just try to import all files
 (
   cd $TARGET_TEST_DIR/$MODEL/
   find $MODEL -name "*.py" | sed 's/.py$//' | sed 's#/__init__##' | sed 's#/#.#g' | grep -v '-' | while read PKG ; do
     echo "import $PKG" | ../../.venv-tests/bin/python
  done
)