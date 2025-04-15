from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
    from src.models.cdm.generated.product.asset.fpv_final_price_election_fallback_enum import FPVFinalPriceElectionFallbackEnum

class ValuationTerms(CdmModelBase):
    """"""
    futures_price_valuation: bool = Field(None, description="The official settlement price as announced by the related exchange is applicable, in accordance with the ISDA 2002 definitions.")
    options_price_valuation: bool = Field(None, description="The official settlement price as announced by the related exchange is applicable, in accordance with the ISDA 2002 definitions")
    number_of_valuation_dates: int = Field(None, description="The number of valuation dates between valuation start date and valuation end date.")
    dividend_valuation_dates: ForwardRef("AdjustableRelativeOrPeriodicDates") = Field(None, description="Specifies the dividend valuation dates of the swap.")
    f_pv_final_price_election_fallback: ForwardRef("FPVFinalPriceElectionFallbackEnum") = Field(None, description="Specifies the fallback provisions for Hedging Party in the determination of the Final Price.")
    multiple_exchange_index_annex_fallback: bool = Field(None, description="For an index option transaction, a flag to indicate whether a relevant Multiple Exchange Index Annex is applicable to the transaction. This annex defines additional provisions which are applicable where an index is comprised of component securities that are traded on multiple exchanges.")
    component_security_index_annex_fallback: bool = Field(None, description="For an index option transaction, a flag to indicate whether a relevant Component Security Index Annex is applicable to the transaction.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
from src.models.cdm.generated.product.asset.fpv_final_price_election_fallback_enum import FPVFinalPriceElectionFallbackEnum
ValuationTerms.model_rebuild()
