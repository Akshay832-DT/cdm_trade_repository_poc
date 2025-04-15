from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AncillaryRoleEnum(CdmModelBase):
    """Defines the enumerated values to specify the ancillary roles to the transaction. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and the AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference."""
    # Enum values
    CalculationAgentFallback: ClassVar[str] = "CalculationAgentFallback"
    CalculationAgentIndependent: ClassVar[str] = "CalculationAgentIndependent"
    CalculationAgentMandatoryEarlyTermination: ClassVar[str] = "CalculationAgentMandatoryEarlyTermination"
    CalculationAgentOptionalEarlyTermination: ClassVar[str] = "CalculationAgentOptionalEarlyTermination"
    DisruptionEventsDeterminingParty: ClassVar[str] = "DisruptionEventsDeterminingParty"
    ExerciseNoticeReceiverPartyCancelableProvision: ClassVar[str] = "ExerciseNoticeReceiverPartyCancelableProvision"
    ExerciseNoticeReceiverPartyExtendibleProvision: ClassVar[str] = "ExerciseNoticeReceiverPartyExtendibleProvision"
    ExerciseNoticeReceiverPartyManual: ClassVar[str] = "ExerciseNoticeReceiverPartyManual"
    ExerciseNoticeReceiverPartyOptionalEarlyTermination: ClassVar[str] = "ExerciseNoticeReceiverPartyOptionalEarlyTermination"
    ExtraordinaryDividendsParty: ClassVar[str] = "ExtraordinaryDividendsParty"
    PredeterminedClearingOrganizationParty: ClassVar[str] = "PredeterminedClearingOrganizationParty"


# Import after class definition to avoid circular imports
AncillaryRoleEnum.model_rebuild()
