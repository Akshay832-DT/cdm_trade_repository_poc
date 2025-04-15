from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DividendPeriodEnum(CdmModelBase):
    """2002 ISDA Equity Derivatives Definitions: First Period, Second Period |"""
    # Enum values
    FirstPeriod: ClassVar[str] = "FirstPeriod"
    SecondPeriod: ClassVar[str] = "SecondPeriod"


# Import after class definition to avoid circular imports
DividendPeriodEnum.model_rebuild()
