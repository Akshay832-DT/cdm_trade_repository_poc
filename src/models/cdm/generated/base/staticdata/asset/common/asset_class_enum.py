from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AssetClassEnum(CdmModelBase):
    """The enumerated values to specify the FpML asset class categorization."""
    # Enum values
    Commodity: ClassVar[str] = "Commodity"
    Credit: ClassVar[str] = "Credit"
    Equity: ClassVar[str] = "Equity"
    ForeignExchange: ClassVar[str] = "ForeignExchange"
    InterestRate: ClassVar[str] = "InterestRate"
    MoneyMarket: ClassVar[str] = "MoneyMarket"


# Import after class definition to avoid circular imports
AssetClassEnum.model_rebuild()
