from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CashPriceTypeEnum(CdmModelBase):
    """Provides a list of possible types of cash prices, applicable when PriceTypeEnum is itself of type CashPrice."""
    # Enum values
    Discount: ClassVar[str] = "Discount"
    Fee: ClassVar[str] = "Fee"
    Premium: ClassVar[str] = "Premium"


# Import after class definition to avoid circular imports
CashPriceTypeEnum.model_rebuild()
