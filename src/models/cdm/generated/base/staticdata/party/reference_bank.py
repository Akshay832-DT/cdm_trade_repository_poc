from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class ReferenceBank(CdmModelBase):
    """A class to describe an institution (party) identified by means of a coding scheme and an optional name."""
    reference_bank_id: ForwardRef("FieldWithMetaString") = Field(description="An institution (party) identifier, e.g. a bank identifier code (BIC). FpML specifies a referenceBankIdScheme.")
    reference_bank_name: str = Field(None, description="The name of the institution (party). A free format string. FpML does not define usage rules for the element.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
ReferenceBank.model_rebuild()
