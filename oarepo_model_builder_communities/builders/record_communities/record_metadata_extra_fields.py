from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class RecordCommunitiesRecordMetadataExtraFieldsBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "record_communities_record_metadata_extra_fields"
    section = "record-metadata"
    template = "record-metadata-extra-fields"
