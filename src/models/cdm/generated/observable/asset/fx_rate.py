from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.quoted_currency_pair import QuotedCurrencyPair

class FxRate(CdmModelBase):
    """A class describing the rate of a currency conversion: pair of currency, quotation mode and exchange rate."""
    quoted_currency_pair: ForwardRef("QuotedCurrencyPair") = Field(description="Defines the two currencies for an FX trade and the quotation relationship between the two currencies.")
    rate: float = Field(None, description="The rate of exchange between the two currencies of the leg of a deal. Must be specified with a quote basis.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.quoted_currency_pair import QuotedCurrencyPair
FxRate.model_rebuild()
