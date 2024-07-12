from .record_communities_model import (
    CommunitiesRequestsComponent,
    CommunityRecordMetadataModelComponent,
    CommunityRecordModelComponent,
    RecordCommunitiesBlueprintsModelComponent,
    RecordCommunitiesDefaultsModelComponent,
    RecordCommunitiesExtResourceModelComponent,
    RecordCommunitiesMarshmallowModelComponent,
    RecordCommunitiesResourceModelComponent,
    RecordCommunitiesSearchOptionsModelComponent,
    RecordCommunitiesServiceModelComponent,
    RecordCommunitiesUIMarshmallowModelComponent,
)
from .record_communities_profile import RecordCommunitiesComponent

RECORD_COMMUNITIES_COMPONENTS = [
    RecordCommunitiesResourceModelComponent,
    RecordCommunitiesServiceModelComponent,
    RecordCommunitiesComponent,
    RecordCommunitiesExtResourceModelComponent,
    RecordCommunitiesDefaultsModelComponent,
    RecordCommunitiesMarshmallowModelComponent,
    RecordCommunitiesBlueprintsModelComponent,
    RecordCommunitiesUIMarshmallowModelComponent,
    CommunityRecordMetadataModelComponent,
    CommunityRecordModelComponent,
    CommunitiesRequestsComponent,
    RecordCommunitiesSearchOptionsModelComponent,
]
