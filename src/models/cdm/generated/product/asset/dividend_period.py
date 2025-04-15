from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
    from src.models.cdm.generated.metafields.reference_with_meta_basket_constituent import ReferenceWithMetaBasketConstituent
    from src.models.cdm.generated.product.asset.dividend_payment_date import DividendPaymentDate

class DividendPeriod(CdmModelBase):
    """Time bounded dividend payment periods, each with a dividend payment date per period."""
    start_date: ForwardRef("DividendPaymentDate") = Field(None, description="Dividend period start date.")
    end_date: ForwardRef("DividendPaymentDate") = Field(None, description="Dividend period end date.")
    date_adjustments: ForwardRef("BusinessDayAdjustments") = Field(description="Date adjustments for all unadjusted dates in this dividend period.")
    basket_constituent: ForwardRef("ReferenceWithMetaBasketConstituent") = Field(None, description="For basket underliers, reference to the basket component which is paying dividends in the specified period.")
    dividend_payment_date: ForwardRef("DividendPaymentDate") = Field(description="Specifies when the dividend will be paid to the receiver of the equity return. Has the meaning as defined in the ISDA 2002 Equity Derivatives Definitions. Is not applicable in the case of a dividend reinvestment election.")
    dividend_valuation_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="Specifies the dividend valuation dates of the swap.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.datetime.business_day_adjustments import BusinessDayAdjustments
from src.models.cdm.generated.metafields.reference_with_meta_basket_constituent import ReferenceWithMetaBasketConstituent
from src.models.cdm.generated.product.asset.dividend_payment_date import DividendPaymentDate
DividendPeriod.model_rebuild()
