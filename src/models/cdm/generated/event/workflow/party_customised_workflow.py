from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.workflow.customised_workflow import CustomisedWorkflow
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class PartyCustomisedWorkflow(CdmModelBase):
    """A class to specify a party-related, non-standardized data in a generic form."""
    party_reference: ForwardRef("ReferenceWithMetaParty") = Field(None, description="Reference to the party to which the workflow pertains to.")
    party_name: str = Field(None, description="The party name to which the workflow pertains to.")
    customised_workflow: List[ForwardRef("CustomisedWorkflow")] = Field(None, description="Non-standardized data in a generic form.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.workflow.customised_workflow import CustomisedWorkflow
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
PartyCustomisedWorkflow.model_rebuild()
