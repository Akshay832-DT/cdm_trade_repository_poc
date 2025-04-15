"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.determination_roles_and_terms import DeterminationRolesAndTerms
    from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.equity_corporate_events import EquityCorporateEvents
    from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.fx_additional_terms import FxAdditionalTerms
    from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.index_adjustment_events import IndexAdjustmentEvents
    from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.representations import Representations
