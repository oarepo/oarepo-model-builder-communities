from oarepo_model_builder.datatypes.components import ResourceModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default

from ...communities import RecordCommunitiesDataType


class RecordCommunitiesResourceModelComponent(ResourceModelComponent):
    eligible_datatypes = [RecordCommunitiesDataType]
    dependency_remap = ResourceModelComponent

    def before_model_prepare(self, datatype, *, context, **kwargs):
        resource = set_default(datatype, "resource", {})
        resource.setdefault(
            "base-classes",
            [
                "oarepo_communities.resources.record_communities.resource.RecordCommunitiesResource"
            ],
        )
        resource.setdefault("imports", [])

        config = set_default(datatype, "resource-config", {})
        config.setdefault(
            "base-classes",
            [
                "oarepo_communities.resources.record_communities.config.RecordCommunitiesResourceConfig"
            ],
        )
        config.setdefault("imports", [])
        resource.setdefault("proxy", "current_record_communities_resource")
        super().before_model_prepare(datatype, context=context, **kwargs)
