from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.determination_roles_and_terms import DeterminationRolesAndTerms
    from src.models.cdm.generated.legaldocumentation.transaction.extraordinary_events import ExtraordinaryEvents
    from src.models.cdm.generated.legaldocumentation.transaction.underlier_substitution_provision import UnderlierSubstitutionProvision

class EquityAdditionalTerms(CdmModelBase):
    """Transaction AdditionalTerms that apply to Equity asset class."""
    extraordinary_events: ForwardRef("ExtraordinaryEvents") = Field(None)
    determination_terms: List[ForwardRef("DeterminationRolesAndTerms")] = Field(None)
    substitution_provision: ForwardRef("UnderlierSubstitutionProvision") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.transaction.additionalterms.determination_roles_and_terms import DeterminationRolesAndTerms
from src.models.cdm.generated.legaldocumentation.transaction.extraordinary_events import ExtraordinaryEvents
from src.models.cdm.generated.legaldocumentation.transaction.underlier_substitution_provision import UnderlierSubstitutionProvision
EquityAdditionalTerms.model_rebuild()
