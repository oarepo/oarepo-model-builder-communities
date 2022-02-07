# Copyright (c) 2022 CESNET
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import json
import os

import yaml
from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model

from tests.mock_filesystem import MockFilesystem


def test_jsonschema():
    schema = load_model(
        "test.yaml",
        "test",
        model_content=yaml.safe_load(open("./tests/test_model.yaml")),
        isort=False,
        black=False,
    )

    filesystem = MockFilesystem()
    builder = create_builder_from_entrypoints(filesystem=filesystem)

    builder.build(schema, "")

    data = json.loads(
        builder.filesystem.open(
            os.path.join("test", "records", "jsonschemas", "test-1.0.0.json")
        ).read()
    )
    print(data)
    communities_jsonschema = (
        data.get("properties", {})
        .get("metadata", {})
        .get("properties", {})
        .get("communities")
    )

    assert communities_jsonschema is not None
    assert set(communities_jsonschema["properties"].keys()) == {"default", "ids"}
    assert communities_jsonschema["properties"]["default"]["type"] == "string"
    assert communities_jsonschema["properties"]["ids"]["type"] == "array"
