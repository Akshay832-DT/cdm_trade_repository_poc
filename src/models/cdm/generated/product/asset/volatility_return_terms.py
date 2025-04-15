from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.listed_derivative import ListedDerivative
    from src.models.cdm.generated.observable.asset.dividend_applicability import DividendApplicability
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.observable.common.determination_method_enum import DeterminationMethodEnum
    from src.models.cdm.generated.product.asset.equity_underlier_provisions import EquityUnderlierProvisions
    from src.models.cdm.generated.product.asset.valuation_terms import ValuationTerms
    from src.models.cdm.generated.product.asset.volatility_cap_floor import VolatilityCapFloor

class VolatilityReturnTerms(CdmModelBase):
    """"""
    valuation_terms: ForwardRef("ValuationTerms") = Field(None, description="Contains all non-date valuation information.")
    annualization_factor: int = Field(None, description="This specifies the numerator of an annualization factor. Frequently this number is equal to the number of observations of prices in a year e.g. 252.")
    dividend_applicability: ForwardRef("DividendApplicability") = Field(None, description="The parameters which define whether dividends are applicable")
    equity_underlier_provisions: ForwardRef("EquityUnderlierProvisions") = Field(None, description="Contains Equity Underlyer provisions regarding jurisdiction and fallbacks.")
    share_price_dividend_adjustment: bool = Field(None, description="Indicates whether the price of shares is adjusted for dividends or not.")
    expected_n: int = Field(None, description="Expected number of trading days.")
    initial_level: float = Field(None, description="Contract will strike off this initial level. Providing just the initialLevel without initialLevelSource, infers that this is AgreedInitialPrice - a specified Initial Index Level.")
    initial_level_source: ForwardRef("DeterminationMethodEnum") = Field(None, description="In this context, this is AgreedInitialPrice - a specified Initial Index Level.")
    mean_adjustment: bool = Field(None, description="Specifies whether Mean Adjustment is applicable or not in the calculation of the Realized Volatility, Variance or Correlation")
    performance: str = Field(None, description="Performance calculation, in accordance with Part 1 Section 12 of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap, Para 75. 'Equity Performance'. Cumulative performance is used as a notional multiplier factor on both legs of an Equity Swap.")
    volatility_strike_price: ForwardRef("Price") = Field(description="Volatility Strike Price in accordance with the ISDA 2011 Equity Derivatives Definitions.")
    volatility_cap_floor: ForwardRef("VolatilityCapFloor") = Field(None, description="Contains volatility-based barriers")
    exchange_traded_contract_nearest: ForwardRef("ListedDerivative") = Field(None, description="Specification of the exchange traded contract nearest.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.listed_derivative import ListedDerivative
from src.models.cdm.generated.observable.asset.dividend_applicability import DividendApplicability
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.observable.common.determination_method_enum import DeterminationMethodEnum
from src.models.cdm.generated.product.asset.equity_underlier_provisions import EquityUnderlierProvisions
from src.models.cdm.generated.product.asset.valuation_terms import ValuationTerms
from src.models.cdm.generated.product.asset.volatility_cap_floor import VolatilityCapFloor
VolatilityReturnTerms.model_rebuild()
