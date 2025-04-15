from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money

class PaymentDiscounting(CdmModelBase):
    """This class corresponds to the FpML PaymentDiscounting.model group for representing the discounting elements that can be associated with a payment."""
    discount_factor: float = Field(None, description="The value representing the discount factor used to calculate the present value of the cash flow.")
    present_value_amount: ForwardRef("Money") = Field(None, description="The amount representing the present value of the forecast payment.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
PaymentDiscounting.model_rebuild()
