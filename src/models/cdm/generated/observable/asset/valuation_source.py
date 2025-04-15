from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_entity import AncillaryEntity
    from src.models.cdm.generated.base.staticdata.party.reference_banks import ReferenceBanks
    from src.models.cdm.generated.metafields.reference_with_meta_quoted_currency_pair import ReferenceWithMetaQuotedCurrencyPair
    from src.models.cdm.generated.observable.asset.fx_spot_rate_source import FxSpotRateSource
    from src.models.cdm.generated.observable.asset.settlement_rate_option import SettlementRateOption

class ValuationSource(CdmModelBase):
    """A class describing the method for obtaining a settlement rate, specified through either an information source (page), a settlement rate option (fixing) or by using quotes from reference banks."""
    quoted_currency_pair: ForwardRef("ReferenceWithMetaQuotedCurrencyPair") = Field(None, description="Defines the two currencies for an FX trade and the quotation relationship between the two currencies.  This attribute was formerly part of 'fxSettlementTerms', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.")
    information_source: ForwardRef("FxSpotRateSource") = Field(None, description="The information source where a published or displayed market rate will be obtained, e.g. Telerate Page 3750.")
    settlement_rate_option: ForwardRef("SettlementRateOption") = Field(None, description="The rate option to use for the fixing. Currently only applicable to foreign exchange fixing in case of cross-currency settlement.")
    reference_banks: ForwardRef("ReferenceBanks") = Field(None, description="A container for a set of reference institutions that may be called upon to provide rate quotations as part of the method to determine the applicable cash settlement amount. If institutions are not specified, it is assumed that reference institutions will be agreed between the parties on the exercise date, or in the case of swap transaction to which mandatory early termination is applicable, the cash settlement valuation date.")
    dealer_or_ccp: ForwardRef("AncillaryEntity") = Field(None, description="Holds an identifier for the reference entity that is agreed by both parties as a basis for cash settlement calculations. This could be a dealer from whom quotations are obtained by the calculation agent on the reference obligation for purposes of cash settlement in a credit event. ISDA 2003 Term: Dealer. This could be the clearing organization (CCP, DCO) to which the trade should be cleared, as applicable for cash-settled swaptions.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_entity import AncillaryEntity
from src.models.cdm.generated.base.staticdata.party.reference_banks import ReferenceBanks
from src.models.cdm.generated.metafields.reference_with_meta_quoted_currency_pair import ReferenceWithMetaQuotedCurrencyPair
from src.models.cdm.generated.observable.asset.fx_spot_rate_source import FxSpotRateSource
from src.models.cdm.generated.observable.asset.settlement_rate_option import SettlementRateOption
ValuationSource.model_rebuild()
