from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.workflow.party_customised_workflow import PartyCustomisedWorkflow
    from src.models.cdm.generated.event.workflow.warehouse_identity_enum import WarehouseIdentityEnum
    from src.models.cdm.generated.event.workflow.workflow_status_enum import WorkflowStatusEnum

class WorkflowState(CdmModelBase):
    """A class to specify workflow information, which is conceptually applicable to all lifecycle events."""
    workflow_status: ForwardRef("WorkflowStatusEnum") = Field(description="The workflow status indicator, e.g. Accepted, Rejected, ...")
    comment: str = Field(None, description="A comment field to be associated with the workflow, e.g. to specify why a transaction event was rejected by a party.")
    party_customised_workflow: List[ForwardRef("PartyCustomisedWorkflow")] = Field(None, description="Workflow data that is specific to certain market participants and is expressed as part of the CDM in a very generic manner, which can be party-specific. The initial use cases have been derived from the CME clearing and the DTCC TIW submissions.")
    warehouse_identity: ForwardRef("WarehouseIdentityEnum") = Field(None, description="The identity of the warehouse, if any, that is executing that workflow step.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.workflow.party_customised_workflow import PartyCustomisedWorkflow
from src.models.cdm.generated.event.workflow.warehouse_identity_enum import WarehouseIdentityEnum
from src.models.cdm.generated.event.workflow.workflow_status_enum import WorkflowStatusEnum
WorkflowState.model_rebuild()
