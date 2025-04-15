from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset

class InitialFixingDate(CdmModelBase):
    """A CDM class which purpose is to specify the initial fixing date either alongside the FpML interest rate specification as an offset of another date, or alongside the credit derivative specification as an unadjusted date."""
    relative_date_offset: ForwardRef("RelativeDateOffset") = Field(None)
    initial_fixing_date: str = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
InitialFixingDate.model_rebuild()
