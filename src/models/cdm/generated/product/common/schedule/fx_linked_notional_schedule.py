from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.observable.asset.fx_spot_rate_source import FxSpotRateSource

class FxLinkedNotionalSchedule(CdmModelBase):
    """A data to:  describe a notional schedule where each notional that applies to a calculation period is calculated with reference to a notional amount or notional amount schedule in a different currency by means of a spot currency exchange rate which is normally observed at the beginning of each period."""
    varying_notional_currency: ForwardRef("FieldWithMetaString") = Field(description="The currency of the varying notional amount, i.e. the notional amount being determined periodically based on observation of a spot currency exchange rate. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
    varying_notional_fixing_dates: ForwardRef("RelativeDateOffset") = Field(description="The dates on which spot currency exchange rates are observed for purposes of determining the varying notional currency amount that will apply to a calculation period.")
    fx_spot_rate_source: ForwardRef("FxSpotRateSource") = Field(description="The information source and time at which the spot currency exchange rate will be observed.")
    fixing_time: ForwardRef("BusinessCenterTime") = Field(None, description="The time at which the spot currency exchange rate will be observed. It is specified as a time in a business day calendar location, e.g. 11:00am London time.")
    varying_notional_interim_exchange_payment_dates: ForwardRef("RelativeDateOffset") = Field(description="The dates on which interim exchanges of notional are paid. Interim exchanges will arise as a result of changes in the spot currency exchange amount or changes in the constant notional schedule (e.g. amortisation).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.asset.fx_spot_rate_source import FxSpotRateSource
FxLinkedNotionalSchedule.model_rebuild()
