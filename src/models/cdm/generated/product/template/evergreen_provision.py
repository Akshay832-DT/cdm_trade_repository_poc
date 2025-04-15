from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
    from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.observable.asset.price import Price

class EvergreenProvision(CdmModelBase):
    """Specifies a transaction which automatically extends for a specified timeframe until the exercise of an embedded option."""
    single_party_option: ForwardRef("PartyRole") = Field(None, description="If evergreen termination is not available to both parties then this component specifies the buyer and seller of the option.")
    notice_period: ForwardRef("RelativeDateOffset") = Field(description="The length of each evergreen extension period relative to the effective date of the preceding contract.")
    notice_deadline_period: ForwardRef("RelativeDateOffset") = Field(None, description="Defines the minimum period before an evergreen is scheduled to terminate that notice can be given that it will terminate beyond the scheduled termination date.")
    notice_deadline_date_time: str = Field(None, description="A specific date and time for the notice deadline")
    extension_frequency: ForwardRef("AdjustableRelativeOrPeriodicDates") = Field(description="The frequency with which the evergreen contract will be extended if notice is not given.")
    final_period_fee_adjustment: ForwardRef("Price") = Field(None, description="An optional adjustment to the rate for the last period of the evergreen i.e. the period from when notice is given to stop rolling the contract through to the termination date.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.observable.asset.price import Price
EvergreenProvision.model_rebuild()
