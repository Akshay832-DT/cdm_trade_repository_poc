from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FeeTypeEnum(CdmModelBase):
    """The enumerated values to specify an event that has given rise to a fee."""
    # Enum values
    Assignment: ClassVar[str] = "Assignment"
    BrokerageCommission: ClassVar[str] = "BrokerageCommission"
    CorporateAction: ClassVar[str] = "CorporateAction"
    CreditEvent: ClassVar[str] = "CreditEvent"
    Increase: ClassVar[str] = "Increase"
    Novation: ClassVar[str] = "Novation"
    PartialTermination: ClassVar[str] = "PartialTermination"
    Premium: ClassVar[str] = "Premium"
    Renegotiation: ClassVar[str] = "Renegotiation"
    Termination: ClassVar[str] = "Termination"
    Upfront: ClassVar[str] = "Upfront"


# Import after class definition to avoid circular imports
FeeTypeEnum.model_rebuild()
