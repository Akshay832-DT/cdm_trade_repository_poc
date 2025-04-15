from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.interpolation_method_enum import InterpolationMethodEnum
    from src.models.cdm.generated.observable.asset.valuation_dates import ValuationDates
    from src.models.cdm.generated.product.asset.price_return_terms import PriceReturnTerms
    from src.models.cdm.generated.product.asset.return_type_enum import ReturnTypeEnum
    from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
    from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms

class EquitySwapMasterConfirmation2018(CdmModelBase):
    """Specification for the General Terms and Relationship Supplement Elections as provided in the 2018 ISDA CDM Equity Confirmation for Security Equity Swap."""
    type_of_swap_election: ForwardRef("ReturnTypeEnum") = Field(description="Per Part 1 Section 4, 'Dividend Obligations', of the 2018 ISDA CDM Equity Confirmation, Para 4.2 'Dividend Returns'")
    pricing_method_election: ForwardRef("PriceReturnTerms") = Field(description="Per Part 1 Section 5, 'Pricing', of the 2018 ISDA CDM Equity Confirmation, Para 5.1")
    linear_interpolation_election: ForwardRef("InterpolationMethodEnum") = Field(description="Per Part 1 Section 3, 'Floating Obligations', of the 2018 ISDA CDM Equity Confirmation. Para 3.3")
    settlement_terms: ForwardRef("SettlementTerms") = Field(description="Per Part 1 Section 8, 'Settlement', of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap")
    valuation_dates: ForwardRef("ValuationDates") = Field(description="The parameters used to generate the 'Equity Valuation Dates' schedule, including the Effective Date and Termination Date for the Swap.")
    equity_cash_settlement_dates: ForwardRef("PaymentDates") = Field(description="The parameters used to generate the payment date schedule, relative to the equityCalculationPeriod. Per Part 1 Section 12, 'Definitions', of the 2018 ISDA CDM Equity Confirmation. Para 73")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.interpolation_method_enum import InterpolationMethodEnum
from src.models.cdm.generated.observable.asset.valuation_dates import ValuationDates
from src.models.cdm.generated.product.asset.price_return_terms import PriceReturnTerms
from src.models.cdm.generated.product.asset.return_type_enum import ReturnTypeEnum
from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
EquitySwapMasterConfirmation2018.model_rebuild()
