from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.common.settlement.principal_payment_schedule import PrincipalPaymentSchedule

class PrincipalPayments(CdmModelBase):
    """A class defining which principal exchanges occur for the stream."""
    initial_payment: bool = Field(description="A true/false flag to indicate whether there is an initial exchange of principal on the effective date.")
    final_payment: bool = Field(description="A true/false flag to indicate whether there is a final exchange of principal on the termination date.")
    intermediate_payment: bool = Field(description="A true/false flag to indicate whether there are intermediate or interim exchanges of principal during the term of the swap.")
    varying_leg_notional_currency: List[List] = Field(None, description="Indicate the Payout legs which nominal amount may vary in regards of FX Fixing dates as determined in the product terms.")
    principal_payment_schedule: ForwardRef("PrincipalPaymentSchedule") = Field(None, description="Describe dates schedules for Principal Exchanges and related role of the parties when known.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.common.settlement.principal_payment_schedule import PrincipalPaymentSchedule
PrincipalPayments.model_rebuild()
