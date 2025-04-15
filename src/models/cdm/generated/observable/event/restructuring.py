from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_restructuring_enum import FieldWithMetaRestructuringEnum

class Restructuring(CdmModelBase):
    """"""
    applicable: bool = Field(description="Indicates whether the restructuring provision is applicable.")
    restructuring_type: ForwardRef("FieldWithMetaRestructuringEnum") = Field(None, description="Specifies the type of restructuring that is applicable.")
    multiple_holder_obligation: bool = Field(None, description="In relation to a restructuring credit event, unless multiple holder obligation is not specified restructurings are limited to multiple holder obligations. A multiple holder obligation means an obligation that is held by more than three holders that are not affiliates of each other and where at least two thirds of the holders must agree to the event that constitutes the restructuring credit event. ISDA 2003 Term: Multiple Holder Obligation.")
    multiple_credit_event_notices: bool = Field(None, description="Presence of this element and value set to 'true' indicates that Section 3.9 of the 2003 Credit Derivatives Definitions shall apply. Absence of this element indicates that Section 3.9 shall not apply. NOTE: Not allowed under ISDA Credit 1999.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_restructuring_enum import FieldWithMetaRestructuringEnum
Restructuring.model_rebuild()
