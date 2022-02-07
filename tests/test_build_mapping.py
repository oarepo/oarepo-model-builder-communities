# Copyright (c) 2022 CESNET
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import json
import os

import yaml
from oarepo_model_builder.entrypoints import create_builder_from_entrypoints, load_model

from tests.mock_filesystem import MockFilesystem


def test_mapping():
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
            os.path.join("test", "records", "mappings", "v7", "test", "test-1.0.0.json")
        ).read()
    )

    communities_mapping = (
        data.get("mappings", {})
        .get("properties", {})
        .get("metadata", {})
        .get("properties", {})
        .get("communities")
    )

    assert communities_mapping is not None
    assert set(communities_mapping["properties"].keys()) == {"default", "ids"}
    assert communities_mapping["properties"]["default"]["type"] == "keyword"
    assert communities_mapping["properties"]["ids"]["type"] == "keyword"
