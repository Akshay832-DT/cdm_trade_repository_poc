from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FxLinkedNotionalAmount(CdmModelBase):
    """A data to:  describe the cashflow representation for FX linked notionals."""
    reset_date: str = Field(None, description="The reset date.")
    adjusted_fx_spot_fixing_date: str = Field(None, description="The date on which the FX spot rate is observed. This date should already be adjusted for any applicable business day convention.")
    observed_fx_spot_rate: float = Field(None, description="The actual observed FX spot rate.")
    notional_amount: float = Field(None, description="The calculation period notional amount.")

# Import after class definition to avoid circular imports
FxLinkedNotionalAmount.model_rebuild()
