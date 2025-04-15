from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_dates import AdjustableDates
    from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
    from src.models.cdm.generated.observable.asset.multiple_valuation_dates import MultipleValuationDates
    from src.models.cdm.generated.observable.asset.single_valuation_date import SingleValuationDate
    from src.models.cdm.generated.product.common.settlement.fx_fixing_date import FxFixingDate

class ValuationDate(CdmModelBase):
    """A single object that represents the different methods to specify a valuation date, as used for cash settlement. The Single / Multiple ValuationDate is used for the determination of recovery in a credit event, the RelativeDateOffset is used for cash-settled option, and FxFixingDate is used for cross-currency settlement."""
    single_valuation_date: ForwardRef("SingleValuationDate") = Field(None, description="Where single valuation date is specified as being applicable for cash settlement, this element specifies the number of business days after satisfaction of all conditions to settlement when such valuation date occurs. ISDA 2003 Term: Single Valuation Date.")
    multiple_valuation_dates: ForwardRef("MultipleValuationDates") = Field(None, description="Where multiple valuation dates are specified as being applicable for cash settlement, this element specifies (a) the number of applicable valuation dates, and (b) the number of business days after satisfaction of all conditions to settlement when the first such valuation date occurs, and (c) the number of business days thereafter of each successive valuation date. ISDA 2003 Term: Multiple Valuation Dates.")
    valuation_date: ForwardRef("RelativeDateOffset") = Field(None, description="The date on which the cash settlement amount will be determined according to the cash settlement method if the parties have not otherwise been able to agree the cash settlement amount. This attribute was formerly part of 'OptionCashSettlement', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.")
    fx_fixing_date: ForwardRef("FxFixingDate") = Field(None, description="The date on which the currency rate will be determined for the purpose of specifying the amount in deliverable currency. This attribute was formerly part of 'NonDeliverableSettlement', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.")
    fx_fixing_schedule: ForwardRef("AdjustableDates") = Field(None, description="The date, when expressed as a schedule of date(s), on which the currency rate will be determined for the purpose of specifying the amount in deliverable currency. This attribute was formerly part of 'NonDeliverableSettlement', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_dates import AdjustableDates
from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
from src.models.cdm.generated.observable.asset.multiple_valuation_dates import MultipleValuationDates
from src.models.cdm.generated.observable.asset.single_valuation_date import SingleValuationDate
from src.models.cdm.generated.product.common.settlement.fx_fixing_date import FxFixingDate
ValuationDate.model_rebuild()
