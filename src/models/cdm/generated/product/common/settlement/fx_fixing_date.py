from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
    from src.models.cdm.generated.base.datetime.business_day_convention_enum import BusinessDayConventionEnum
    from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum
    from src.models.cdm.generated.base.datetime.period_enum import PeriodEnum
    from src.models.cdm.generated.metafields.reference_with_meta_business_centers import ReferenceWithMetaBusinessCenters
    from src.models.cdm.generated.product.common.schedule.date_relative_to_calculation_period_dates import DateRelativeToCalculationPeriodDates
    from src.models.cdm.generated.product.common.schedule.date_relative_to_payment_dates import DateRelativeToPaymentDates
    from src.models.cdm.generated.product.common.schedule.date_relative_to_valuation_dates import DateRelativeToValuationDates

class FxFixingDate(CdmModelBase):
    """Extends the Offset structure to specify an FX fixing date as an offset to dates specified somewhere else in the document."""
    period_multiplier: int = Field(None, description="A time period multiplier, e.g. 1, 2 or 3 etc. A negative value can be used when specifying an offset relative to another date, e.g. -2 days.")
    period: ForwardRef("PeriodEnum") = Field(None, description="A time period, e.g. a day, week, month or year of the stream. If the periodMultiplier value is 0 (zero) then period must contain the value D (day).")
    day_type: ForwardRef("DayTypeEnum") = Field(None, description="In the case of an offset specified as a number of days, this element defines whether consideration is given as to whether a day is a good business day or not. If a day type of business days is specified then non-business days are ignored when calculating the offset. The financial business centers to use for determination of business days are implied by the context in which this element is used. This element must only be included when the offset is specified as a number of days. If the offset is zero days then the dayType element should not be included.")
    business_day_convention: ForwardRef("BusinessDayConventionEnum") = Field(None, description="The convention for adjusting a date if it would otherwise fall on a day that is not a business day, as specified by an ISDA convention (e.g. Following, Precedent).")
    business_centers: ForwardRef("BusinessCenters") = Field(None)
    business_centers_reference: ForwardRef("ReferenceWithMetaBusinessCenters") = Field(None, description="A reference to a set of financial business centers defined elsewhere in the document. This set of business centers is used to determine whether a particular day is a business day or not.")
    date_relative_to_payment_dates: ForwardRef("DateRelativeToPaymentDates") = Field(None, description="The payment date references on which settlements in non-deliverable currency are due and will then have to be converted according to the terms specified through the other parts of the nonDeliverableSettlement structure.")
    date_relative_to_calculation_period_dates: ForwardRef("DateRelativeToCalculationPeriodDates") = Field(None, description="The calculation period references on which settlements in non-deliverable currency are due and will then have to be converted according to the terms specified through the other parts of the nonDeliverableSettlement structure. Implemented for Brazilian-CDI swaps where it will refer to the termination date of the appropriate leg.")
    date_relative_to_valuation_dates: ForwardRef("DateRelativeToValuationDates") = Field(None, description="The calculation period references on which settlements in non-deliverable currency are due and will then have to be converted according to the terms specified through the other parts of the nonDeliverableSettlement structure. Implemented for Brazilian-CDI swaps where it will refer to the termination date of the appropriate leg.")
    fx_fixing_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="Describes the specific date when a non-deliverable forward or cash-settled option will 'fix' against a particular rate, which will be used to compute the ultimate cash settlement. This element should be omitted where a single, discrete fixing date cannot be identified e.g. on an american option, where fixing may occur at any date on a continuous range.  This attribute was formerly part of 'fxSettlementTerms', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
from src.models.cdm.generated.base.datetime.business_day_convention_enum import BusinessDayConventionEnum
from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum
from src.models.cdm.generated.base.datetime.period_enum import PeriodEnum
from src.models.cdm.generated.metafields.reference_with_meta_business_centers import ReferenceWithMetaBusinessCenters
from src.models.cdm.generated.product.common.schedule.date_relative_to_calculation_period_dates import DateRelativeToCalculationPeriodDates
from src.models.cdm.generated.product.common.schedule.date_relative_to_payment_dates import DateRelativeToPaymentDates
from src.models.cdm.generated.product.common.schedule.date_relative_to_valuation_dates import DateRelativeToValuationDates
FxFixingDate.model_rebuild()
