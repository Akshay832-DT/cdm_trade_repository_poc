from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
    from src.models.cdm.generated.observable.asset.valuation_dates import ValuationDates
    from src.models.cdm.generated.product.common.schedule.observation_terms import ObservationTerms
    from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
    from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
    from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
    from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
    from src.models.cdm.generated.product.template.fx_feature import FxFeature
    from src.models.cdm.generated.product.template.portfolio_return_terms import PortfolioReturnTerms
    from src.models.cdm.generated.product.template.return_terms import ReturnTerms
    from src.models.cdm.generated.product.template.underlier import Underlier

class PerformancePayout(CdmModelBase):
    """Contains the necessary specifications for all performance payouts, encompassing equity return, dividend, variance, volatility and correlation products."""
    payer_receiver: ForwardRef("PayerReceiver") = Field(None, description="Canonical representation of the payer and receiver parties applicable to each payout leg.")
    price_quantity: ForwardRef("ResolvablePriceQuantity") = Field(None, description="Each payout leg must implement the quantity concept as a 'resolvable' type, which allows for different payout legs to be linked to each other (e.g. in the case of cross-curreny products).")
    principal_payment: ForwardRef("PrincipalPayments") = Field(None, description="The specification of the principal exchange. Optional as only applicable in the case of cross-currency or zero-coupon swaps with a final payment.")
    settlement_terms: ForwardRef("SettlementTerms") = Field(None, description="Each payout leg must specifies its settlement terms, including the delivery type (i.e. cash vs physical, and their respective terms), the transfer type (DvP etc.) and settlement date, if any.")
    observation_terms: ForwardRef("ObservationTerms") = Field(None, description="Defines how and when a performance type option or performance type swap is to be observed.")
    valuation_dates: ForwardRef("ValuationDates") = Field(description="Defines how and when a performance type option or performance type swap is to be valued, including both interim and final valuation.")
    payment_dates: ForwardRef("PaymentDates") = Field(description="Defines the payment date schedule, as defined by the parameters that are needed to specify it, either in a parametric way or by reference to another schedule of dates (e.g. the valuation dates).")
    underlier: ForwardRef("Underlier") = Field(None, description="Identifies the underlying product that is referenced for pricing of the applicable leg in a swap.  Referenced in the '2018 ISDA CDM Equity Confirmation for Security Equity Swap' as Security.")
    fx_feature: List[ForwardRef("FxFeature")] = Field(None, description="Defines quanto or composite FX features that are included in the swap leg.")
    return_terms: ForwardRef("ReturnTerms") = Field(None, description="Specifies the type of return of a performance payout.")
    portfolio_return_terms: List[ForwardRef("PortfolioReturnTerms")] = Field(None, description="Specifies an individual type of return of a Performance Payout, when such individual return is part of an aggregation of multiple similar returns, at Performance Payout level")
    initial_valuation_price: List[ForwardRef("ReferenceWithMetaPriceSchedule")] = Field(None, description="Specifies the net initial valuation price(s) of the underlier at Performance Payout level. This price can be expressed either as an actual amount/currency, as a determination method, or by reference to another value specified in the swap document.")
    interim_valuation_price: List[ForwardRef("ReferenceWithMetaPriceSchedule")] = Field(None, description="Specifies the net initial valuation price(s) of the underlier at Performance Payout level. This price can be expressed either as an actual amount/currency, as a determination method, or by reference to another value specified in the swap document.")
    final_valuation_price: List[ForwardRef("ReferenceWithMetaPriceSchedule")] = Field(None, description="Specifies the net final valuation price(s) of the underlier at Performance Payout level. This price can be expressed either as an actual amount/currency, as a determination method, or by reference to another value specified in the swap document.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
from src.models.cdm.generated.observable.asset.valuation_dates import ValuationDates
from src.models.cdm.generated.product.common.schedule.observation_terms import ObservationTerms
from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
from src.models.cdm.generated.product.template.fx_feature import FxFeature
from src.models.cdm.generated.product.template.portfolio_return_terms import PortfolioReturnTerms
from src.models.cdm.generated.product.template.return_terms import ReturnTerms
from src.models.cdm.generated.product.template.underlier import Underlier
PerformancePayout.model_rebuild()
