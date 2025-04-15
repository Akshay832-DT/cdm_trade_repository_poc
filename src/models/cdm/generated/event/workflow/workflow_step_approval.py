from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.workflow.event_timestamp import EventTimestamp
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class WorkflowStepApproval(CdmModelBase):
    """Party approvals associated to the current WorkflowStep. """
    approved: bool = Field(description="Flag denoting whether the workflow step is approved or not")
    party: ForwardRef("ReferenceWithMetaParty") = Field(description="Reference to the Party who is approving/rejecting this workflow step")
    rejected_reason: str = Field(None, description="Optional reason for rejecting the workflow step")
    timestamp: ForwardRef("EventTimestamp") = Field(description="Timestamp of the approval")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.workflow.event_timestamp import EventTimestamp
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
WorkflowStepApproval.model_rebuild()
