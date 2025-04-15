from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
    from src.models.cdm.generated.base.datetime.frequency import Frequency
    from src.models.cdm.generated.base.datetime.offset import Offset
    from src.models.cdm.generated.product.common.schedule.pay_relative_to_enum import PayRelativeToEnum
    from src.models.cdm.generated.product.common.schedule.payment_date_schedule import PaymentDateSchedule

class PaymentDates(CdmModelBase):
    """Specifies the parameters to generate the payment date schedule, either through a parametric representation or by reference to specified dates."""
    payment_frequency: ForwardRef("Frequency") = Field(None, description="The frequency at which regular payment dates occur. If the payment frequency is equal to the frequency defined in the calculation period dates component then one calculation period contributes to each payment amount. If the payment frequency is less frequent than the frequency defined in the calculation period dates component then more than one calculation period will contribute to the payment amount. A payment frequency more frequent than the calculation period frequency or one that is not a multiple of the calculation period frequency is invalid. If the payment frequency is of value T (term), the period is defined by the effectiveDate and the terminationDate.")
    first_payment_date: str = Field(None, description="The first unadjusted payment date. This day may be subject to adjustment in accordance with any business day convention specified in paymentDatesAdjustments. This element must only be included if there is an initial stub. This date will normally correspond to an unadjusted calculation period start or end date. This is true even if early or delayed payment is specified to be applicable since the actual first payment date will be the specified number of days before or after the applicable adjusted calculation period start or end date with the resulting payment date then being adjusted in accordance with any business day convention specified in paymentDatesAdjustments.")
    last_regular_payment_date: str = Field(None, description="The last regular payment date when specified as a date, as in the FpML interest rate construct. FpML specifies that this date may be subject to adjustment in accordance with any business day convention specified in the paymentDatesAdjustments attribute.")
    payment_date_schedule: ForwardRef("PaymentDateSchedule") = Field(None, description="The payment dates when specified as relative to a set of dates specified somewhere else in the instance document/transaction, e.g. the valuation dates as typically the case for equity swaps, or when specified as a calculation period schedule.")
    pay_relative_to: ForwardRef("PayRelativeToEnum") = Field(None, description="Specifies whether the payments occur relative to each adjusted calculation period start date or end date, each reset date, valuation date or the last pricing date. Calculation period start date means relative to the start of the first calculation period contributing to a given payment. Similarly, calculation period end date means the end of the last calculation period contributing to a given payment. The valuation date is applicable for Brazilian-CDI and equity swaps.")
    payment_days_offset: ForwardRef("Offset") = Field(None, description="If early payment or delayed payment is required, specifies the number of days offset that the payment occurs relative to what would otherwise be the unadjusted payment date. The offset can be specified in terms of either calendar or business days. Even in the case of a calendar days offset, the resulting payment date, adjusted for the specified calendar days offset, will still be adjusted in accordance with the specified payment dates adjustments. This element should only be included if early or delayed payment is applicable, i.e. if the periodMultiplier element value is not equal to zero. An early payment would be indicated by a negative periodMultiplier element value and a delayed payment (or payment lag) would be indicated by a positive periodMultiplier element value.")
    payment_dates_adjustments: ForwardRef("BusinessDayAdjustments") = Field(None, description="The definition of the business day convention and financial business centers used for adjusting the payment date if it would otherwise fall on a day that is not a business day in the specified business center.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
from src.models.cdm.generated.base.datetime.frequency import Frequency
from src.models.cdm.generated.base.datetime.offset import Offset
from src.models.cdm.generated.product.common.schedule.pay_relative_to_enum import PayRelativeToEnum
from src.models.cdm.generated.product.common.schedule.payment_date_schedule import PaymentDateSchedule
PaymentDates.model_rebuild()
