from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.metafields.reference_with_meta_non_negative_quantity_schedule import ReferenceWithMetaNonNegativeQuantitySchedule
    from src.models.cdm.generated.metafields.reference_with_meta_observable import ReferenceWithMetaObservable
    from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
    from src.models.cdm.generated.product.asset.correlation_return_terms import CorrelationReturnTerms
    from src.models.cdm.generated.product.asset.dividend_return_terms import DividendReturnTerms
    from src.models.cdm.generated.product.asset.price_return_terms import PriceReturnTerms
    from src.models.cdm.generated.product.asset.variance_return_terms import VarianceReturnTerms
    from src.models.cdm.generated.product.asset.volatility_return_terms import VolatilityReturnTerms

class PortfolioReturnTerms(CdmModelBase):
    """Specifies an individual type of return of a Performance Payout, when such individual return is part of an aggregation of multiple similar returns, at Performance Payout level."""
    price_return_terms: ForwardRef("PriceReturnTerms") = Field(None, description="Return terms based upon the underlier's observed price.")
    dividend_return_terms: ForwardRef("DividendReturnTerms") = Field(None, description="Return terms based upon dividend payments associated to the underlier.")
    variance_return_terms: ForwardRef("VarianceReturnTerms") = Field(None, description="Return terms based upon the observed variance of the underlier's price.")
    volatility_return_terms: ForwardRef("VolatilityReturnTerms") = Field(None, description="Return terms based upon the observed volatility of the underlier's price.")
    correlation_return_terms: ForwardRef("CorrelationReturnTerms") = Field(None, description="Return terms based upon the observed correlation between the components of the underlying basket.")
    payer_receiver: ForwardRef("PayerReceiver") = Field(description="Canonical representation of the payer and receiver parties applicable to each individual return leg.")
    underlier: ForwardRef("ReferenceWithMetaObservable") = Field(description="Defines the product that is the subject of a tradable product definition, an underlying product definition, a physical exercise, a position, or other purposes.")
    quantity: ForwardRef("ReferenceWithMetaNonNegativeQuantitySchedule") = Field(None, description="Specifies a quantity schedule for the underlier, which applies to each individual return leg.")
    initial_valuation_price: List[ForwardRef("ReferenceWithMetaPriceSchedule")] = Field(None, description="Specifies the initial valuation price(s) of the underlier. This price can be expressed either as an actual amount/currency, as a determination method, or by reference to another value specified in the swap document.")
    interim_valuation_price: List[ForwardRef("ReferenceWithMetaPriceSchedule")] = Field(None, description="Specifies the initial valuation price(s) of the underlier. This price can be expressed either as an actual amount/currency, as a determination method, or by reference to another value specified in the swap document.")
    final_valuation_price: List[ForwardRef("ReferenceWithMetaPriceSchedule")] = Field(None, description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Final Price | Specifies the final valuation price of the underlier. This price can be expressed either as an actual amount/currency, as a determination method, or by reference to another value specified in the swap document.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.metafields.reference_with_meta_non_negative_quantity_schedule import ReferenceWithMetaNonNegativeQuantitySchedule
from src.models.cdm.generated.metafields.reference_with_meta_observable import ReferenceWithMetaObservable
from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
from src.models.cdm.generated.product.asset.correlation_return_terms import CorrelationReturnTerms
from src.models.cdm.generated.product.asset.dividend_return_terms import DividendReturnTerms
from src.models.cdm.generated.product.asset.price_return_terms import PriceReturnTerms
from src.models.cdm.generated.product.asset.variance_return_terms import VarianceReturnTerms
from src.models.cdm.generated.product.asset.volatility_return_terms import VolatilityReturnTerms
PortfolioReturnTerms.model_rebuild()
