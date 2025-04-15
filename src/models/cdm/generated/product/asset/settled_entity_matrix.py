from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_settled_entity_matrix_source_enum import FieldWithMetaSettledEntityMatrixSourceEnum

class SettledEntityMatrix(CdmModelBase):
    """A class to specify the Relevant Settled Entity Matrix."""
    matrix_source: ForwardRef("FieldWithMetaSettledEntityMatrixSourceEnum") = Field(description="Relevant settled entity matrix source.")
    publication_date: str = Field(None, description="Specifies the publication date of the applicable version of the matrix. When this element is omitted, the Standard Terms Supplement defines rules for which version of the matrix is applicable.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_settled_entity_matrix_source_enum import FieldWithMetaSettledEntityMatrixSourceEnum
SettledEntityMatrix.model_rebuild()
