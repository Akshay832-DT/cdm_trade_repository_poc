"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.event.workflow.credit_limit_information import CreditLimitInformation
    from src.models.cdm.generated.event.workflow.credit_limit_type_enum import CreditLimitTypeEnum
    from src.models.cdm.generated.event.workflow.credit_limit_utilisation import CreditLimitUtilisation
    from src.models.cdm.generated.event.workflow.credit_limit_utilisation_position import CreditLimitUtilisationPosition
    from src.models.cdm.generated.event.workflow.customised_workflow import CustomisedWorkflow
    from src.models.cdm.generated.event.workflow.event_instruction import EventInstruction
    from src.models.cdm.generated.event.workflow.event_timestamp import EventTimestamp
    from src.models.cdm.generated.event.workflow.event_timestamp_qualification_enum import EventTimestampQualificationEnum
    from src.models.cdm.generated.event.workflow.limit_applicable import LimitApplicable
    from src.models.cdm.generated.event.workflow.limit_applicable_extended import LimitApplicableExtended
    from src.models.cdm.generated.event.workflow.limit_level_enum import LimitLevelEnum
    from src.models.cdm.generated.event.workflow.message_information import MessageInformation
    from src.models.cdm.generated.event.workflow.party_customised_workflow import PartyCustomisedWorkflow
    from src.models.cdm.generated.event.workflow.velocity import Velocity
    from src.models.cdm.generated.event.workflow.warehouse_identity_enum import WarehouseIdentityEnum
    from src.models.cdm.generated.event.workflow.workflow import Workflow
    from src.models.cdm.generated.event.workflow.workflow_state import WorkflowState
    from src.models.cdm.generated.event.workflow.workflow_status_enum import WorkflowStatusEnum
    from src.models.cdm.generated.event.workflow.workflow_step import WorkflowStep
    from src.models.cdm.generated.event.workflow.workflow_step_approval import WorkflowStepApproval
