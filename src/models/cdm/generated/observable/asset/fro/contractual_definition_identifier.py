from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.common.contractual_definitions_enum import ContractualDefinitionsEnum

class ContractualDefinitionIdentifier(CdmModelBase):
    """"""
    contractual_definition_type: ForwardRef("ContractualDefinitionsEnum") = Field(description="e.g. ISDA2021Definitions")
    contractual_definition_version: str = Field(None, description="e.g. V1")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.common.contractual_definitions_enum import ContractualDefinitionsEnum
ContractualDefinitionIdentifier.model_rebuild()
