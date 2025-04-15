from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FundProductTypeEnum(CdmModelBase):
    """Represents an enumeration list to identify the fund product type."""
    # Enum values
    ExchangeTradedFund: ClassVar[str] = "ExchangeTradedFund"
    MoneyMarketFund: ClassVar[str] = "MoneyMarketFund"
    MutualFund: ClassVar[str] = "MutualFund"
    OtherFund: ClassVar[str] = "OtherFund"


# Import after class definition to avoid circular imports
FundProductTypeEnum.model_rebuild()
