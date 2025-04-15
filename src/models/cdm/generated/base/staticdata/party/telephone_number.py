from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.telephone_type_enum import TelephoneTypeEnum

class TelephoneNumber(CdmModelBase):
    """A class to specify a telephone number as a type of phone number (e.g. work, personal, ...) alongside with the actual number."""
    telephone_number_type: ForwardRef("TelephoneTypeEnum") = Field(None, description="The type of telephone number, e.g. work, mobile.")
    number: str = Field(description="The actual telephone number.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.telephone_type_enum import TelephoneTypeEnum
TelephoneNumber.model_rebuild()
