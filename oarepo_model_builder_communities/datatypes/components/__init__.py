from .record_communities_model import (
    RecordCommunitiesResourceModelComponent,
    RecordCommunitiesServiceModelComponent, RecordCommunitiesExtResourceModelComponent,
    RecordCommunitiesDefaultsModelComponent, DraftFilesRecordModelComponent, RecordCommunitiesMarshmallowModelComponent,
    RecordCommunitiesMetadataModelComponent, RecordCommunitiesBlueprintsModelComponent,
)
from .record_communities_profile import RecordCommunitiesComponent

RECORD_COMMUNITIES_COMPONENTS = [
    RecordCommunitiesResourceModelComponent,
    RecordCommunitiesServiceModelComponent,
    RecordCommunitiesComponent,
    RecordCommunitiesExtResourceModelComponent,
    RecordCommunitiesDefaultsModelComponent,
    DraftFilesRecordModelComponent,
    RecordCommunitiesMarshmallowModelComponent,
    RecordCommunitiesMetadataModelComponent,
    RecordCommunitiesBlueprintsModelComponent,
]