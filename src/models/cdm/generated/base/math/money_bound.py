from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money

class MoneyBound(CdmModelBase):
    """The money bound is defined as a money amount and whether the bound is inclusive."""
    money: ForwardRef("Money") = Field(description="The money amount to be used as the bound, e.g. 1,000 USD.")
    inclusive: bool = Field(description="Whether the money amount bound is inclusive, e.g. for a lower bound, false would indicate greater than, whereas true would indicate greater than or equal to.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
MoneyBound.model_rebuild()
