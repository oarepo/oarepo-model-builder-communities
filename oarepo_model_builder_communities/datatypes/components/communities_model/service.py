from oarepo_model_builder.datatypes.components import ServiceModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.datatypes import ModelDataType


class RecordCommunitiesServiceModelComponent(ServiceModelComponent):
    eligible_datatypes = [ModelDataType]
    affects = [ServiceModelComponent] # must be before workflow component

    def before_model_prepare(self, datatype, *, context, **kwargs):
        config = set_default(datatype, "service-config", {})
        config.setdefault("components", []).append("{{oarepo_communities.services.components.default_workflow.CommunityDefaultWorkflowComponent}}")
        config.setdefault("components", []).append("{{oarepo_communities.services.components.include.CommunityInclusionComponent}}")