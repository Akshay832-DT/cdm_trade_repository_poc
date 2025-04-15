from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement import LegalAgreement

class ContractFormationInstruction(CdmModelBase):
    """Specifies instructions to create a fully formed contract, with optional legal agreements."""
    legal_agreement: List[ForwardRef("LegalAgreement")] = Field(None, description="Optional legal agreements associated to the contract being formed, for instance a master agreement.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.common.legal_agreement import LegalAgreement
ContractFormationInstruction.model_rebuild()
