from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class CommunityRecordsParentConftestBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "community_records_parent_conftest"
    template = "community-records-parent-conftest"

    def _get_output_module(self):
        return f'{self.current_model.definition["tests"]["module"]}.conftest'
