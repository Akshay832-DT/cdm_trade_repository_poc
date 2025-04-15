from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_dates import AdjustableDates
    from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_or_relative_date import AdjustableOrAdjustedOrRelativeDate
    from src.models.cdm.generated.base.datetime.business_date_range import BusinessDateRange

class SettlementDate(CdmModelBase):
    """A data defining the settlement date(s) for cash or physical settlement as either a set of explicit dates, together with applicable adjustments, or as a date relative to some other (anchor) date, or as any date in a range of contiguous business days. This data type provides a level of abstraction on top of the different legacy methods used to specify a settlement / payment date, which vary across product types, asset classes and delivery types."""
    adjustable_or_relative_date: ForwardRef("AdjustableOrAdjustedOrRelativeDate") = Field(None, description="A single settlement date subject to adjustment or specified as relative to another date (e.g. the trade date). This attribute was formerly part of 'SettlementTerms', which is now being harmonised to include a common 'SettlementDate', as inherited from 'SettlementBase'.")
    value_date: str = Field(None, description="The settlement date for a forward settling product. For Foreign Exchange contracts, this represents a common settlement date between both currency legs. To specify different settlement dates for each currency leg, see the ForeignExchange class. This attribute was formerly part of 'SettlementTerms', which is now being harmonised to include a common 'SettlementDate', as inherited from 'SettlementBase'.")
    adjustable_dates: ForwardRef("AdjustableDates") = Field(None, description="A series of dates that shall be subject to adjustment if they would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date. This attributes was formerly part of 'CashSettlementPaymentDate' as included into 'OptionCashSettlement' (which is now merged into a unique 'CashSettlementTerms' data type.")
    business_date_range: ForwardRef("BusinessDateRange") = Field(None, description="A range of contiguous business days. This attribute is meant to be merged with the 'settlementDate' at some future point once we refactor 'Date' to use a single complex type across the model. This attributes was formerly part of 'CashSettlementPaymentDate', as included into 'OptionCashSettlement' (which is now merged into a unique 'CashSettlementTerms' data type.")
    cash_settlement_business_days: int = Field(None, description="The number of business days used in the determination of the cash settlement payment date. If a cash settlement amount is specified, the cash settlement payment date will be this number of business days following the calculation of the final price. If a cash settlement amount is not specified, the cash settlement payment date will be this number of business days after all conditions to settlement are satisfied. ISDA 2003 Term: Cash Settlement Date. This attribute was formerly part of 'CashSettlementTerms' as used for credit event settlement, which now includes a common 'SettlementDate' attribute.")
    payment_delay: bool = Field(None, description="Applicable to CDS on MBS to specify whether payment delays are applicable to the fixed Amount. RMBS typically have a payment delay of 5 days between the coupon date of the reference obligation and the payment date of the synthetic swap. CMBS do not, on the other hand, with both payment dates being on the 25th of each month.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_dates import AdjustableDates
from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_or_relative_date import AdjustableOrAdjustedOrRelativeDate
from src.models.cdm.generated.base.datetime.business_date_range import BusinessDateRange
SettlementDate.model_rebuild()
