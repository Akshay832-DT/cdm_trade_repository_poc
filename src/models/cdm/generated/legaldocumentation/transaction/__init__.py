"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.transaction.additional_disruption_events import AdditionalDisruptionEvents
    from src.models.cdm.generated.legaldocumentation.transaction.clause import Clause
    from src.models.cdm.generated.legaldocumentation.transaction.equity_additional_terms import EquityAdditionalTerms
    from src.models.cdm.generated.legaldocumentation.transaction.extraordinary_events import ExtraordinaryEvents
    from src.models.cdm.generated.legaldocumentation.transaction.transaction_additional_terms import TransactionAdditionalTerms
    from src.models.cdm.generated.legaldocumentation.transaction.underlier_substitution_provision import UnderlierSubstitutionProvision
