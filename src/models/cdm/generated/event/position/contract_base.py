from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_collateral import ReferenceWithMetaCollateral
    from src.models.cdm.generated.metafields.reference_with_meta_contract_details import ReferenceWithMetaContractDetails
    from src.models.cdm.generated.metafields.reference_with_meta_execution_details import ReferenceWithMetaExecutionDetails

class ContractBase(CdmModelBase):
    """Encapsulates data features common to trade and position."""
    contract_details: ForwardRef("ReferenceWithMetaContractDetails") = Field(None, description="Represents information specific to trades or positions involving contractual products.")
    execution_details: ForwardRef("ReferenceWithMetaExecutionDetails") = Field(None, description="Defines specific attributes that relate to trade or position executions.")
    collateral: ForwardRef("ReferenceWithMetaCollateral") = Field(None, description="Represents the collateral obligations of a party.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_collateral import ReferenceWithMetaCollateral
from src.models.cdm.generated.metafields.reference_with_meta_contract_details import ReferenceWithMetaContractDetails
from src.models.cdm.generated.metafields.reference_with_meta_execution_details import ReferenceWithMetaExecutionDetails
ContractBase.model_rebuild()
