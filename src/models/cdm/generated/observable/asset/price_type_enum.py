from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PriceTypeEnum(CdmModelBase):
    """Provides enumerated values for types of prices in the Price data type in order to explain how to interpret the amount and use it in calculations."""
    # Enum values
    AssetPrice: ClassVar[str] = "AssetPrice"
    CashPrice: ClassVar[str] = "CashPrice"
    Correlation: ClassVar[str] = "Correlation"
    Dividend: ClassVar[str] = "Dividend"
    ExchangeRate: ClassVar[str] = "ExchangeRate"
    InterestRate: ClassVar[str] = "InterestRate"
    Variance: ClassVar[str] = "Variance"
    Volatility: ClassVar[str] = "Volatility"


# Import after class definition to avoid circular imports
PriceTypeEnum.model_rebuild()
