from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class InflationCalculationStyleEnum(CdmModelBase):
    """Indicates the style of how the inflation index calculates the payment (e.g. YearOnYear, ZeroCoupon)."""
    # Enum values
    YearOnYear: ClassVar[str] = "YearOnYear"
    ZeroCoupon: ClassVar[str] = "ZeroCoupon"


# Import after class definition to avoid circular imports
InflationCalculationStyleEnum.model_rebuild()
