from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.observable.asset.fro.contractual_definition_identifier import ContractualDefinitionIdentifier

class ContractualDefinition(CdmModelBase):
    """"""
    identifier: ForwardRef("Identifier") = Field(None, description="Corresponds to the unique identifier of the Contractual Definition in which the code is published")
    contractual_definition_identifier: ForwardRef("ContractualDefinitionIdentifier") = Field(None, description="Contractual Definition Identifier in which the code is published. Includes Document Type and Document Version")
    publication_date: str = Field(None, description="2021-06-11")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.observable.asset.fro.contractual_definition_identifier import ContractualDefinitionIdentifier
ContractualDefinition.model_rebuild()
