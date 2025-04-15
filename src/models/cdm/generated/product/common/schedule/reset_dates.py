from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
    from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
    from src.models.cdm.generated.base.datetime.offset import Offset
    from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
    from src.models.cdm.generated.metafields.reference_with_meta_calculation_period_dates import ReferenceWithMetaCalculationPeriodDates
    from src.models.cdm.generated.product.common.schedule.initial_fixing_date import InitialFixingDate
    from src.models.cdm.generated.product.common.schedule.reset_frequency import ResetFrequency
    from src.models.cdm.generated.product.common.schedule.reset_relative_to_enum import ResetRelativeToEnum

class ResetDates(CdmModelBase):
    """A data defining:  the parameters used to generate the reset dates schedule and associated fixing dates. The reset dates are the dates on which the new index value (which is observed on the fixing date) is applied for each period and on which the interest rate hence begins to accrue."""
    calculation_period_dates_reference: ForwardRef("ReferenceWithMetaCalculationPeriodDates") = Field(None, description="A pointer style reference to the associated calculation period dates component defined elsewhere in the document.")
    reset_relative_to: ForwardRef("ResetRelativeToEnum") = Field(None, description="Specifies whether the reset dates are determined with respect to each adjusted calculation period start date or adjusted calculation period end date. If the reset frequency is specified as daily this element must not be included.")
    initial_fixing_date: ForwardRef("InitialFixingDate") = Field(None, description="The initial fixing date.")
    fixing_dates: ForwardRef("RelativeDateOffset") = Field(None, description="The fixing dates are the dates on which the index values are observed. The fixing dates are specified by reference to the reset date through business days offset and an associated set of financial business centers. Normally these offset calculation rules will be those specified in the ISDA definition for the relevant floating rate index (ISDA's Floating Rate Option). However, non-standard offset calculation rules may apply for a trade if mutually agreed by the principal parties to the transaction.")
    final_fixing_date: ForwardRef("AdjustableDate") = Field(None, description="This attribute is not part of the FpML ResetDate, and has been added as part of the CDM to support the credit derivatives final fixing date.")
    rate_cut_off_days_offset: ForwardRef("Offset") = Field(None, description="Specifies the number of business days before the period end date when the rate cut-off date is assumed to apply. The financial business centers associated with determining the rate cut-off date are those specified in the reset dates adjustments. The rate cut-off number of days must be a negative integer (a value of zero would imply no rate cut off applies in which case the rateCutOffDaysOffset element should not be included). The relevant rate for each reset date in the period from, and including, a rate cut-off date to, but excluding, the next applicable period end date (or, in the case of the last calculation period, the termination date) will (solely for purposes of calculating the floating amount payable on the next applicable payment date) be deemed to be the relevant rate in effect on that rate cut-off date. For example, if rate cut-off days for a daily averaging deal is -2 business days, then the refix rate applied on (period end date - 2 days) will also be applied as the reset on (period end date - 1 day), i.e. the actual number of reset dates remains the same but from the rate cut-off date until the period end date, the same refix rate is applied. Note that in the case of several calculation periods contributing to a single payment, the rate cut-off is assumed only to apply to the final calculation period contributing to that payment. The day type associated with the offset must imply a business days offset.")
    reset_frequency: ForwardRef("ResetFrequency") = Field(None, description="The frequency at which the reset dates occur. In the case of a weekly reset frequency, also specifies the day of the week that the reset occurs. If the reset frequency is greater than the calculation period frequency then this implies that more than one reset is established for each calculation period and some form of rate averaging is applicable.")
    reset_dates_adjustments: ForwardRef("BusinessDayAdjustments") = Field(None, description="The definition of the business day convention and financial business centers used for adjusting the reset date if it would otherwise fall on a day that is not a business day in the specified business center.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
from src.models.cdm.generated.base.datetime.offset import Offset
from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
from src.models.cdm.generated.metafields.reference_with_meta_calculation_period_dates import ReferenceWithMetaCalculationPeriodDates
from src.models.cdm.generated.product.common.schedule.initial_fixing_date import InitialFixingDate
from src.models.cdm.generated.product.common.schedule.reset_frequency import ResetFrequency
from src.models.cdm.generated.product.common.schedule.reset_relative_to_enum import ResetRelativeToEnum
ResetDates.model_rebuild()
