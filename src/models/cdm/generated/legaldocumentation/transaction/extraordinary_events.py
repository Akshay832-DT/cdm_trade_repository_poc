from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.master.nationalization_or_insolvency_or_delisting_event_enum import NationalizationOrInsolvencyOrDelistingEventEnum
    from src.models.cdm.generated.legaldocumentation.transaction.additional_disruption_events import AdditionalDisruptionEvents
    from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.equity_corporate_events import EquityCorporateEvents
    from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.index_adjustment_events import IndexAdjustmentEvents
    from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.representations import Representations
    from src.models.cdm.generated.legaldocumentation.transaction.clause import Clause

class ExtraordinaryEvents(CdmModelBase):
    """Where the underlying is shares, defines market events affecting the issuer of those shares that may require the terms of the transaction to be adjusted."""
    additional_bespoke_terms: List[ForwardRef("Clause")] = Field(None, description="Where parties may optionnaly describe any extra bespoke agreements, in regards of the standardized Extraordinary Events.")
    merger_events: ForwardRef("EquityCorporateEvents") = Field(None, description="Per the 2018 ISDA CDM Equity Confirmation for Security Equity Swap")
    tender_offer_events: ForwardRef("EquityCorporateEvents") = Field(None, description="Per the 2002 ISDA Equity Derivatives Definitions: ")
    composition_of_combined_consideration: bool = Field(None, description="Per the 2002 ISDA Equity Derivatives Definitions: ")
    index_adjustment_events: ForwardRef("IndexAdjustmentEvents") = Field(None, description="Per the 2002 ISDA Equity Derivatives Definitions: Adjustments to Indices ")
    additional_disruption_events: ForwardRef("AdditionalDisruptionEvents") = Field(None, description="Per the 2002 ISDA Equity Derivatives Definitions | 2018 ISDA CDM Equity Confirmation for Security Equity Swaps")
    failure_to_deliver: bool = Field(None, description="If true, failure to deliver is applicable.")
    representations: ForwardRef("Representations") = Field(None)
    nationalization_or_insolvency: ForwardRef("NationalizationOrInsolvencyOrDelistingEventEnum") = Field(None, description="Per the 2002 ISDA Equity Derivatives Definitions | 2018 ISDA CDM Equity Confirmation for Security Equity Swap")
    delisting: ForwardRef("NationalizationOrInsolvencyOrDelistingEventEnum") = Field(None, description="Per the 2002 ISDA Equity Derivatives Definitions | 2018 ISDA CDM Equity Confirmation for Security Equity Swap:")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.master.nationalization_or_insolvency_or_delisting_event_enum import NationalizationOrInsolvencyOrDelistingEventEnum
from src.models.cdm.generated.legaldocumentation.transaction.additional_disruption_events import AdditionalDisruptionEvents
from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.equity_corporate_events import EquityCorporateEvents
from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.index_adjustment_events import IndexAdjustmentEvents
from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.representations import Representations
from src.models.cdm.generated.legaldocumentation.transaction.clause import Clause
ExtraordinaryEvents.model_rebuild()
