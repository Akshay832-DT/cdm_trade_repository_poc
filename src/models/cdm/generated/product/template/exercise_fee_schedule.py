from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
    from src.models.cdm.generated.base.math.schedule import Schedule
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.metafields.reference_with_meta_money import ReferenceWithMetaMoney
    from src.models.cdm.generated.product.common.schedule.amount_schedule import AmountSchedule

class ExerciseFeeSchedule(CdmModelBase):
    """A class to define a fee or schedule of fees to be payable on the exercise of an option. This fee may be defined as an amount or a percentage of the notional exercised. As a difference with FpML, it extends the BuyerSeller class."""
    payer: ForwardRef("CounterpartyRoleEnum") = Field(None, description="Specifies the counterparty responsible for making the payments defined by this structure.  The party is one of the two principal parties to the transaction.")
    receiver: ForwardRef("CounterpartyRoleEnum") = Field(None, description="Specifies the party that receives the payments corresponding to this structure.  The party is one of the two counterparties to the transaction.")
    notional_reference: ForwardRef("ReferenceWithMetaMoney") = Field(description="A pointer style reference to the associated notional schedule defined elsewhere in the document.")
    fee_amount_schedule: ForwardRef("AmountSchedule") = Field(None, description="The exercise fee amount schedule. The fees are expressed as currency amounts. The currency of the fee is assumed to be that of the notional schedule referenced.")
    fee_rate_schedule: ForwardRef("Schedule") = Field(None, description="The exercise free rate schedule. The fees are expressed as percentage rates of the notional being exercised. The currency of the fee is assumed to be that of the notional schedule referenced.")
    fee_payment_date: ForwardRef("RelativeDateOffset") = Field(description="The date on which exercise fee(s) will be paid. It is specified as a relative date.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
from src.models.cdm.generated.base.math.schedule import Schedule
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.metafields.reference_with_meta_money import ReferenceWithMetaMoney
from src.models.cdm.generated.product.common.schedule.amount_schedule import AmountSchedule
ExerciseFeeSchedule.model_rebuild()
