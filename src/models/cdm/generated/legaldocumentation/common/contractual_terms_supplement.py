from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_contractual_supplement_type_enum import FieldWithMetaContractualSupplementTypeEnum

class ContractualTermsSupplement(CdmModelBase):
    """A contractual supplement (such as those published by ISDA) and its publication date that will apply to the trade."""
    contractual_terms_supplement_type: ForwardRef("FieldWithMetaContractualSupplementTypeEnum") = Field(description="Identifies the form of applicable contractual supplement.")
    publication_date: str = Field(None, description="Specifies the publication date of the applicable version of the contractual supplement.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_contractual_supplement_type_enum import FieldWithMetaContractualSupplementTypeEnum
ContractualTermsSupplement.model_rebuild()
