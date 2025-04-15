from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class OffsetCalculation(CdmModelBase):
    """Defines business day shifts for daily componded or averaged rates.  This type is used for lookback and lockout rates. This type is used to represent modular computed rates in interestRatePayouts."""
    offset_days: int = Field(None, description="The number of business days offset.")

# Import after class definition to avoid circular imports
OffsetCalculation.model_rebuild()
