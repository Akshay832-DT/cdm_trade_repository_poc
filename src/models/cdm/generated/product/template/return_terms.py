from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.correlation_return_terms import CorrelationReturnTerms
    from src.models.cdm.generated.product.asset.dividend_return_terms import DividendReturnTerms
    from src.models.cdm.generated.product.asset.price_return_terms import PriceReturnTerms
    from src.models.cdm.generated.product.asset.variance_return_terms import VarianceReturnTerms
    from src.models.cdm.generated.product.asset.volatility_return_terms import VolatilityReturnTerms

class ReturnTerms(CdmModelBase):
    """Specifies the type of return of a performance payout."""
    price_return_terms: ForwardRef("PriceReturnTerms") = Field(None, description="Return terms based upon the underlier's observed price.")
    dividend_return_terms: ForwardRef("DividendReturnTerms") = Field(None, description="Return terms based upon dividend payments associated to the underlier.")
    variance_return_terms: ForwardRef("VarianceReturnTerms") = Field(None, description="Return terms based upon the observed variance of the underlier's price.")
    volatility_return_terms: ForwardRef("VolatilityReturnTerms") = Field(None, description="Return terms based upon the observed volatility of the underlier's price.")
    correlation_return_terms: ForwardRef("CorrelationReturnTerms") = Field(None, description="Return terms based upon the observed correlation between the components of the underlying basket.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.asset.correlation_return_terms import CorrelationReturnTerms
from src.models.cdm.generated.product.asset.dividend_return_terms import DividendReturnTerms
from src.models.cdm.generated.product.asset.price_return_terms import PriceReturnTerms
from src.models.cdm.generated.product.asset.variance_return_terms import VarianceReturnTerms
from src.models.cdm.generated.product.asset.volatility_return_terms import VolatilityReturnTerms
ReturnTerms.model_rebuild()
