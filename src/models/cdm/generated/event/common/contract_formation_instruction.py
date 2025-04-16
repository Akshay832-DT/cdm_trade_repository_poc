from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

# Import dependencies first
from src.models.cdm.generated.legaldocumentation.common.legal_agreement import LegalAgreement

# Rebuild dependencies first
LegalAgreement.model_rebuild()

class ContractFormationInstruction(CdmModelBase):
    """Specifies instructions to create a fully formed contract, with optional legal agreements."""
    legal_agreement: Optional[List["LegalAgreement"]] = Field(None, description="Optional legal agreements associated to the contract being formed, for instance a master agreement.")

# Rebuild this model
ContractFormationInstruction.model_rebuild()
