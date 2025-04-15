from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PerformanceTransferTypeEnum(CdmModelBase):
    """The enumerated values to specify the origin of a performance transfer"""
    # Enum values
    Commodity: ClassVar[str] = "Commodity"
    Correlation: ClassVar[str] = "Correlation"
    Dividend: ClassVar[str] = "Dividend"
    Equity: ClassVar[str] = "Equity"
    Interest: ClassVar[str] = "Interest"
    Variance: ClassVar[str] = "Variance"
    Volatility: ClassVar[str] = "Volatility"


# Import after class definition to avoid circular imports
PerformanceTransferTypeEnum.model_rebuild()
