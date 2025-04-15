from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
    from src.models.cdm.generated.product.common.settlement.principal_payment import PrincipalPayment

class PrincipalPaymentSchedule(CdmModelBase):
    """Describe dates schedules for Principal Exchanges and related role of the parties when known."""
    initial_principal_payment: ForwardRef("PrincipalPayment") = Field(None, description="Principal Payment made at Trade inception.")
    intermediate_principal_payment: ForwardRef("AdjustableRelativeOrPeriodicDates") = Field(None, description="Principal Payment as part of the Trade lifecycle e.g. as part of notional reset adjustements in a Cross Currency Swap with a varying notional leg.")
    final_principal_payment: ForwardRef("PrincipalPayment") = Field(None, description="Principal Payment at Trade maturity")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
from src.models.cdm.generated.product.common.settlement.principal_payment import PrincipalPayment
PrincipalPaymentSchedule.model_rebuild()
