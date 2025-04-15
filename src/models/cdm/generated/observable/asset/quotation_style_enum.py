from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class QuotationStyleEnum(CdmModelBase):
    """The enumerated values to specify the actual quotation style (e.g. PointsUpFront, TradedSpread) used to quote a credit default swap fee leg."""
    # Enum values
    PointsUpFront: ClassVar[str] = "PointsUpFront"
    Price: ClassVar[str] = "Price"
    TradedSpread: ClassVar[str] = "TradedSpread"


# Import after class definition to avoid circular imports
QuotationStyleEnum.model_rebuild()
