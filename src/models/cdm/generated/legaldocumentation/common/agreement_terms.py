from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
    from src.models.cdm.generated.legaldocumentation.contract.agreement import Agreement

class AgreementTerms(CdmModelBase):
    """Specification of the content of a legal agreement."""
    agreement: ForwardRef("Agreement") = Field(description="Specification of the standard set of terms that define a legal agreement.")
    clause_library: bool = Field(None, description="Specification of whether the agreement terms have been negotiated using the clause library methodology.")
    counterparty: List[ForwardRef("Counterparty")] = Field(None, description="Specification of the roles of the counterparties to the agreement.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
from src.models.cdm.generated.legaldocumentation.contract.agreement import Agreement
AgreementTerms.model_rebuild()
