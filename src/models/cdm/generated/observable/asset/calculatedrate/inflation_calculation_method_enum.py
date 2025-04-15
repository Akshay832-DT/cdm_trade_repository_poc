from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class InflationCalculationMethodEnum(CdmModelBase):
    """Indicates how to use the inflation index to calculate the payment (e.g. Ratio, Return, Spread). Added for Inflation Asset Swap"""
    # Enum values
    Ratio: ClassVar[str] = "Ratio"
    Return: ClassVar[str] = "Return"
    Spread: ClassVar[str] = "Spread"


# Import after class definition to avoid circular imports
InflationCalculationMethodEnum.model_rebuild()
