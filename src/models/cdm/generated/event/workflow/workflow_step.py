from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.base.staticdata.party.account import Account
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.event.common.action_enum import ActionEnum
    from src.models.cdm.generated.event.common.business_event import BusinessEvent
    from src.models.cdm.generated.event.common.counterparty_position_business_event import CounterpartyPositionBusinessEvent
    from src.models.cdm.generated.event.common.lineage import Lineage
    from src.models.cdm.generated.event.workflow.credit_limit_information import CreditLimitInformation
    from src.models.cdm.generated.event.workflow.event_instruction import EventInstruction
    from src.models.cdm.generated.event.workflow.event_timestamp import EventTimestamp
    from src.models.cdm.generated.event.workflow.message_information import MessageInformation
    from src.models.cdm.generated.event.workflow.workflow_state import WorkflowState
    from src.models.cdm.generated.event.workflow.workflow_step_approval import WorkflowStepApproval
    from src.models.cdm.generated.metafields.reference_with_meta_workflow_step import ReferenceWithMetaWorkflowStep

class WorkflowStep(CdmModelBase):
    """A workflow step represents the state of a business event. The workflow step contains a reference to a previous WorkflowStep in order to preserve lineage. A workflow step is accepted if it contains a business event, proposed if proposedEvent is present and is rejected if the rejected flag is set."""
    business_event: ForwardRef("BusinessEvent") = Field(None, description="Life cycle event for the step. The businessEvent is optional when a proposedEvent or rejection are present.")
    counterparty_position_business_event: ForwardRef("CounterpartyPositionBusinessEvent") = Field(None, description="Documents the life cycle event for a position.")
    proposed_event: ForwardRef("EventInstruction") = Field(None, description="The proposed event for a workflow step. The proposedEvent is optional when the businessEvent or rejection are present")
    rejected: bool = Field(None, description="Flags this step as rejected.")
    approval: List[ForwardRef("WorkflowStepApproval")] = Field(None, description="Optional party approvals for the current workflow step. A workflow step can have any number of parties associated to it, thus this object is represented as a list. All parties that are expected to provide approval should have an item in this list that references them.")
    previous_workflow_step: ForwardRef("ReferenceWithMetaWorkflowStep") = Field(None, description="Optional previous workflow step that provides lineage to workflow steps that precedes it.")
    next_event: ForwardRef("EventInstruction") = Field(None, description="The intended next event can be specified, even if the instructions are not known yet.")
    message_information: ForwardRef("MessageInformation") = Field(None, description="Contains all information pertaining the FpML messaging header ")
    timestamp: List[ForwardRef("EventTimestamp")] = Field(None, description="The set of timestamp(s) associated with the event as a collection of [dateTime, qualifier].")
    event_identifier: List[ForwardRef("Identifier")] = Field(None, description="The identifier(s) that uniquely identify a lifecycle event. The unbounded cardinality is meant to provide the ability to associate identifiers that are issued by distinct parties. As an example, each of the parties to the event may choose to associate their own identifiers to the event.")
    action: ForwardRef("ActionEnum") = Field(None, description="Specifies whether the event is a new, a correction or a cancellation.")
    party: List[ForwardRef("Party")] = Field(None, description="The specification of the event parties. This attribute is optional, as not applicable to certain events (e.g. most of the observations).")
    account: List[ForwardRef("Account")] = Field(None, description="Optional account information that could be associated to the event.")
    lineage: ForwardRef("Lineage") = Field(None, description="The lineage attribute provides a linkage among lifecycle events through the globalKey hash value. One example is when a given lifecycle event is being corrected or cancelled. In such case, each subsequent event will have lineage into the prior version of that event. The second broad use case is when an event has a dependency upon either another event (e.g. the regular payment associated with a fix/float swap will have a lineage into the reset event, which will in turn have a lineage into the observation event for the floating rate and the contract) or a contract (e.g. the exercise of an option has a lineage into that option).")
    credit_limit_information: ForwardRef("CreditLimitInformation") = Field(None)
    workflow_state: ForwardRef("WorkflowState") = Field(None, description="The event workflow information, i.e. the workflow status, the associated comment and the partyCustomisedWorkflow which purpose is to provide the ability to associate custom workflow information to the CDM.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.base.staticdata.party.account import Account
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.event.common.action_enum import ActionEnum
from src.models.cdm.generated.event.common.business_event import BusinessEvent
from src.models.cdm.generated.event.common.counterparty_position_business_event import CounterpartyPositionBusinessEvent
from src.models.cdm.generated.event.common.lineage import Lineage
from src.models.cdm.generated.event.workflow.credit_limit_information import CreditLimitInformation
from src.models.cdm.generated.event.workflow.event_instruction import EventInstruction
from src.models.cdm.generated.event.workflow.event_timestamp import EventTimestamp
from src.models.cdm.generated.event.workflow.message_information import MessageInformation
from src.models.cdm.generated.event.workflow.workflow_state import WorkflowState
from src.models.cdm.generated.event.workflow.workflow_step_approval import WorkflowStepApproval
from src.models.cdm.generated.metafields.reference_with_meta_workflow_step import ReferenceWithMetaWorkflowStep
WorkflowStep.model_rebuild()
