from .record_communities_model import (
    RecordCommunitiesBlueprintsModelComponent,
    RecordCommunitiesDefaultsModelComponent,
    RecordCommunitiesExtResourceModelComponent,
    RecordCommunitiesMarshmallowModelComponent,
    RecordCommunitiesResourceModelComponent,
    RecordCommunitiesServiceModelComponent,
    RecordCommunitiesUIMarshmallowModelComponent,
)
from .record_communities_profile import RecordCommunitiesComponent
from .shared import CommunityRecordMetadataModelComponent, CommunityRecordModelComponent

RECORD_COMMUNITIES_COMPONENTS = [
    RecordCommunitiesResourceModelComponent,
    RecordCommunitiesServiceModelComponent,
    RecordCommunitiesComponent,
    RecordCommunitiesExtResourceModelComponent,
    RecordCommunitiesDefaultsModelComponent,
    RecordCommunitiesMarshmallowModelComponent,
    RecordCommunitiesBlueprintsModelComponent,
    RecordCommunitiesUIMarshmallowModelComponent,
]
# todo rename
SHARED_COMPONENTS = [
    CommunityRecordMetadataModelComponent,
    CommunityRecordModelComponent,
]
