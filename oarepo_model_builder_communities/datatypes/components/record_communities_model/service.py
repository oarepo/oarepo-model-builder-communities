from oarepo_model_builder.datatypes.components import ServiceModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default

from ...communities import RecordCommunitiesDataType


class RecordCommunitiesServiceModelComponent(ServiceModelComponent):
    eligible_datatypes = [RecordCommunitiesDataType]
    dependency_remap = ServiceModelComponent

    def before_model_prepare(self, datatype, *, context, **kwargs):
        config = set_default(datatype, "service-config", {})
        config.setdefault(
            "base-classes",
            ["RecordCommunitiesServiceConfig"],
        )
        config.setdefault(
            "imports",
            [{"import": "oarepo_communities.services.record_communities.config.RecordCommunitiesServiceConfig",},
             ]
        )

        service = set_default(datatype, "service", {})
        service.setdefault("base-classes", ["RecordCommunitiesService"])
        service.setdefault(
            "imports",
            [
                {
                    "import": "oarepo_communities.services.record_communities.service.RecordCommunitiesService",
                }
            ],
        )

        super().before_model_prepare(datatype, context=context, **kwargs)

    def after_model_prepare(self, datatype, *, context, **kwargs):
        datatype.definition["service-config"]["components"] = []