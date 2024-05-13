from .record_communities_model import (
    CommunityRecordMetadataModelComponent,
    CommunityRecordModelComponent,
    RecordCommunitiesBlueprintsModelComponent,
    RecordCommunitiesDefaultsModelComponent,
    RecordCommunitiesExtResourceModelComponent,
    RecordCommunitiesMarshmallowModelComponent,
    RecordCommunitiesResourceModelComponent,
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
]
