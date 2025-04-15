from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.calendar_spread import CalendarSpread
    from src.models.cdm.generated.product.template.strike_spread import StrikeSpread

class StrategyFeature(CdmModelBase):
    """A class for defining option strategy features."""
    strike_spread: ForwardRef("StrikeSpread") = Field(None, description="Definition of the upper strike in a strike spread.")
    calendar_spread: ForwardRef("CalendarSpread") = Field(None, description="Definition of the later expiration date in a calendar spread.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.calendar_spread import CalendarSpread
from src.models.cdm.generated.product.template.strike_spread import StrikeSpread
StrategyFeature.model_rebuild()
