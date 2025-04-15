from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.observable.asset.fro.contractual_definition_identifier import ContractualDefinitionIdentifier

class FloatingRateIndexMap(CdmModelBase):
    """A map for a single FRO to or from an equivalent or similar FRO in a different contractual definitions version."""
    index: List[ForwardRef("FloatingRateIndexEnum")] = Field(None, description=" The FRO name that is being mapped to/from.")
    contractual_definition_identifier: ForwardRef("ContractualDefinitionIdentifier") = Field(None, description="Contractual Definition to which the map applies. Includes Document Type and Document Version")
    identifier: ForwardRef("Identifier") = Field(None, description="Corresponds to the unique identifier of the Contractual Definition to which the map applies")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.observable.asset.fro.contractual_definition_identifier import ContractualDefinitionIdentifier
FloatingRateIndexMap.model_rebuild()
