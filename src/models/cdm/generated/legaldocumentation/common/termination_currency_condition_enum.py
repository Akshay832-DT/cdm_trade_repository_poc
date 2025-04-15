from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TerminationCurrencyConditionEnum(CdmModelBase):
    """"""
    # Enum values
    FreelyAvailable: ClassVar[str] = "FreelyAvailable"
    PaymentsDue: ClassVar[str] = "PaymentsDue"
    PaymentsDueAndFreelyAvailable: ClassVar[str] = "PaymentsDueAndFreelyAvailable"
    Specified: ClassVar[str] = "Specified"


# Import after class definition to avoid circular imports
TerminationCurrencyConditionEnum.model_rebuild()
