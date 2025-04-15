from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.fx_additional_terms import FxAdditionalTerms
    from src.models.cdm.generated.legaldocumentation.transaction.equity_additional_terms import EquityAdditionalTerms

class TransactionAdditionalTerms(CdmModelBase):
    """Additional specification for the extraordinary events that may affect a trade and the related contractual rights and obligation of the parties when this happens. Such terms are typically required to extend the economics terms, for the purpose of producing the final legal contractual form of the Transaction."""
    equity_additional_terms: ForwardRef("EquityAdditionalTerms") = Field(None)
    foreign_exchange_additional_terms: ForwardRef("FxAdditionalTerms") = Field(None)
    commodities_additional_terms: str = Field(None)
    credit_additional_terms: str = Field(None)
    interest_rate_additional_terms: str = Field(None)
    digital_asset_additional_terms: str = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.fx_additional_terms import FxAdditionalTerms
from src.models.cdm.generated.legaldocumentation.transaction.equity_additional_terms import EquityAdditionalTerms
TransactionAdditionalTerms.model_rebuild()
