from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.additional_fixed_payments import AdditionalFixedPayments
    from src.models.cdm.generated.product.asset.floating_amount_provisions import FloatingAmountProvisions
    from src.models.cdm.generated.product.asset.interest_short_fall import InterestShortFall

class FloatingAmountEvents(CdmModelBase):
    """A class to specify the ISDA terms relating to the floating rate payment events and the implied additional fixed payments, applicable to the credit derivatives transactions on mortgage-backed securities with pay-as-you-go or physical settlement."""
    failure_to_pay_principal: bool = Field(None, description="A floating rate payment event. Corresponds to the failure by the Reference Entity to pay an expected principal amount or the payment of an actual principal amount that is less than the expected principal amount. ISDA 2003 Term: Failure to Pay Principal.")
    interest_shortfall: ForwardRef("InterestShortFall") = Field(None, description="A floating rate payment event. With respect to any Reference Obligation Payment Date, either (a) the non-payment of an Expected Interest Amount or (b) the payment of an Actual Interest Amount that is less than the Expected Interest Amount. ISDA 2003 Term: Interest Shortfall.")
    writedown: bool = Field(None, description="A floating rate payment event. Results from the fact that the underlier writes down its outstanding principal amount. ISDA 2003 Term: Writedown.")
    implied_writedown: bool = Field(None, description="A floating rate payment event. Results from the fact that losses occur to the underlying instruments that do not result in reductions of the outstanding principal of the reference obligation.")
    floating_amount_provisions: ForwardRef("FloatingAmountProvisions") = Field(None, description="Specifies the floating amount provisions associated with the floatingAmountEvents.")
    additional_fixed_payments: ForwardRef("AdditionalFixedPayments") = Field(None, description="Specifies the events that will give rise to the payment additional fixed payments.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.asset.additional_fixed_payments import AdditionalFixedPayments
from src.models.cdm.generated.product.asset.floating_amount_provisions import FloatingAmountProvisions
from src.models.cdm.generated.product.asset.interest_short_fall import InterestShortFall
FloatingAmountEvents.model_rebuild()
