from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AlternativeToInterestAmountEnum(CdmModelBase):
    """If there is an alternative to interest amounts, how is it specified?"""
    # Enum values
    ActualAmountReceived: ClassVar[str] = "ActualAmountReceived"
    Other: ClassVar[str] = "Other"
    Standard: ClassVar[str] = "Standard"
    TransferIfDeliveryAmountBelowMTA: ClassVar[str] = "TransferIfDeliveryAmountBelowMTA"


# Import after class definition to avoid circular imports
AlternativeToInterestAmountEnum.model_rebuild()
