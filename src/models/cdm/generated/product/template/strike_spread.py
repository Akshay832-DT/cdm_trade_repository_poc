from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.option_strike import OptionStrike

class StrikeSpread(CdmModelBase):
    """A class for defining a strike spread feature."""
    upper_strike: ForwardRef("OptionStrike") = Field(description="Upper strike in a strike spread.")
    upper_strike_number_of_options: float = Field(description="Number of options at the upper strike price in a strike spread.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.option_strike import OptionStrike
StrikeSpread.model_rebuild()
