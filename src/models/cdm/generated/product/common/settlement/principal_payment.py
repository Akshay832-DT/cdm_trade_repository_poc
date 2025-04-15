from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.observable.asset.money import Money

class PrincipalPayment(CdmModelBase):
    """Any kind of principal payments when the amount is known and thus fixed."""
    principal_payment_date: ForwardRef("AdjustableDate") = Field(None, description="The date where the PrincipalPayment shall be settled.")
    payer_receiver: ForwardRef("PayerReceiver") = Field(None, description="Specifies the parties responsible for making and receiving payments defined by this structure.")
    principal_amount: ForwardRef("Money") = Field(None, description="When known at the time the transaction is made, the cash amount to be paid.")
    discount_factor: float = Field(None, description="The value representing the discount factor used to calculate the present value of the principal payment amount.")
    present_value_principal_amount: ForwardRef("Money") = Field(None, description="The amount representing the present value of the principal payment.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.observable.asset.money import Money
PrincipalPayment.model_rebuild()
