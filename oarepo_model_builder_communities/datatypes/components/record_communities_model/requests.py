from oarepo_model_builder_requests.datatypes.components.requests_model.requests import RequestsComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.datatypes import ModelDataType, DataTypeComponent

from oarepo_model_builder_communities.datatypes import RecordCommunitiesDataType


class CommunitiesRequestsComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [RequestsComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        requests = set_default(datatype, "requests", {})
        ui_resolvers = requests.setdefault(
            "additional-ui-resolvers",
            {},
        )
        ui_resolvers |= {'"oarepo_community"': '{{oarepo_communities.resolvers.ui.OARepoCommunityReferenceUIResolver}}("oarepo_community")'}