from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ValuationMethodEnum(CdmModelBase):
    """The enumerated values to specify the ISDA defined methodology for determining the final price of the reference obligation for purposes of cash settlement."""
    # Enum values
    AverageBlendedHighest: ClassVar[str] = "AverageBlendedHighest"
    AverageBlendedMarket: ClassVar[str] = "AverageBlendedMarket"
    AverageHighest: ClassVar[str] = "AverageHighest"
    AverageMarket: ClassVar[str] = "AverageMarket"
    BlendedHighest: ClassVar[str] = "BlendedHighest"
    BlendedMarket: ClassVar[str] = "BlendedMarket"
    Highest: ClassVar[str] = "Highest"
    Market: ClassVar[str] = "Market"


# Import after class definition to avoid circular imports
ValuationMethodEnum.model_rebuild()
