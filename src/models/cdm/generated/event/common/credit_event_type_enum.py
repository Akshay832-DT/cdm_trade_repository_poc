from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditEventTypeEnum(CdmModelBase):
    """Represents the enumerated values to specify a credit event type."""
    # Enum values
    Bankruptcy: ClassVar[str] = "Bankruptcy"
    DistressedRatingsDowngrade: ClassVar[str] = "DistressedRatingsDowngrade"
    FailureToPay: ClassVar[str] = "FailureToPay"
    FailureToPayInterest: ClassVar[str] = "FailureToPayInterest"
    FailureToPayPrincipal: ClassVar[str] = "FailureToPayPrincipal"
    GovernmentalIntervention: ClassVar[str] = "GovernmentalIntervention"
    ImpliedWritedown: ClassVar[str] = "ImpliedWritedown"
    MaturityExtension: ClassVar[str] = "MaturityExtension"
    ObligationAcceleration: ClassVar[str] = "ObligationAcceleration"
    ObligationDefault: ClassVar[str] = "ObligationDefault"
    RepudiationMoratorium: ClassVar[str] = "RepudiationMoratorium"
    Restructuring: ClassVar[str] = "Restructuring"
    Writedown: ClassVar[str] = "Writedown"


# Import after class definition to avoid circular imports
CreditEventTypeEnum.model_rebuild()
