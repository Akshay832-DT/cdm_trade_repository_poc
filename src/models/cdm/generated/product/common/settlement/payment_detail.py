from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.product.common.settlement.payment_rule import PaymentRule

class PaymentDetail(CdmModelBase):
    """"""
    payment_date: ForwardRef("AdjustableOrRelativeDate") = Field(None)
    payment_rule: ForwardRef("PaymentRule") = Field(description="The calculation rule.")
    payment_amount: ForwardRef("Money") = Field(None, description="A fixed payment amount.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.product.common.settlement.payment_rule import PaymentRule
PaymentDetail.model_rebuild()
