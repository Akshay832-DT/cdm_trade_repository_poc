from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CorporateActionTypeEnum(CdmModelBase):
    """The enumerated values to specify the origin of a corporate action transfer."""
    # Enum values
    BonusIssue: ClassVar[str] = "BonusIssue"
    CashDividend: ClassVar[str] = "CashDividend"
    ClassAction: ClassVar[str] = "ClassAction"
    Delisting: ClassVar[str] = "Delisting"
    EarlyRedemption: ClassVar[str] = "EarlyRedemption"
    Liquidation: ClassVar[str] = "Liquidation"
    Merger: ClassVar[str] = "Merger"
    ReverseStockSplit: ClassVar[str] = "ReverseStockSplit"
    RightsIssue: ClassVar[str] = "RightsIssue"
    SpinOff: ClassVar[str] = "SpinOff"
    StockDividend: ClassVar[str] = "StockDividend"
    StockIdentifierChange: ClassVar[str] = "StockIdentifierChange"
    StockNameChange: ClassVar[str] = "StockNameChange"
    StockReclassification: ClassVar[str] = "StockReclassification"
    StockSplit: ClassVar[str] = "StockSplit"
    Takeover: ClassVar[str] = "Takeover"


# Import after class definition to avoid circular imports
CorporateActionTypeEnum.model_rebuild()
