from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_matrix_term_enum import FieldWithMetaMatrixTermEnum
    from src.models.cdm.generated.metafields.field_with_meta_matrix_type_enum import FieldWithMetaMatrixTypeEnum

class ContractualMatrix(CdmModelBase):
    """"""
    matrix_type: ForwardRef("FieldWithMetaMatrixTypeEnum") = Field(description="Identifies the form of applicable matrix.")
    matrix_term: ForwardRef("FieldWithMetaMatrixTermEnum") = Field(None, description="Defines any applicable key into the relevant matrix. For example, the Transaction Type would be the single term required for the Credit Derivatives Physical Settlement Matrix. This element should be omitted in the case of the 2000 ISDA Definitions Settlement Matrix for Early Termination and Swaptions.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_matrix_term_enum import FieldWithMetaMatrixTermEnum
from src.models.cdm.generated.metafields.field_with_meta_matrix_type_enum import FieldWithMetaMatrixTypeEnum
ContractualMatrix.model_rebuild()
