black oarepo_model_builder_communities tests --target-version py310
autoflake --in-place --remove-all-unused-imports --recursive oarepo_model_builder_communities tests
isort oarepo_model_builder_communities tests  --profile black
