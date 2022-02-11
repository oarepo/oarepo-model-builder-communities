# Communities plugin for oarepo-model-builder

An [oarepo-model-builder](https://github.com/oarepo/oarepo-model-builder) plugin that enables support for Communities in generated record models.

## Prerequisities

In order to use this plugin, you need to have a virtualenv with [oarepo-model-builder](https://github.com/oarepo/oarepo-model-builder) package installed and a valid record model specification (`model.yaml`) file created.

## Installation

Enable the plugin in the record's model:

```yaml
# model.yaml
plugins:
  - oarepo-model-builder-communities
#...
```

When you run the `oarepo-compile-model` command for the first time, `oarepo-model-builder` will install the plugin into your virtualenv for you. Alternatively, you can use:

```shell
pip install oarepo-model-builder-communities
```

to install the plugin into your virtualenv.

## Usage

To use Communities in a record's model metadata, add the following top-level import to your specification:

```yaml
# model.yaml
oarepo:use:
  - oarepo-communities
model:
  properties:
    metadata:
      properties:
        #...
```

Doing so, will add a `communities` field to record's `metadata` properties, generation all models, jsonschemas, mappings and apis necessary for integration with Communities.
