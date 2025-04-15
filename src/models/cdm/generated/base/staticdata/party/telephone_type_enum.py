from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TelephoneTypeEnum(CdmModelBase):
    """The enumerated values to specify the type of telephone number, e.g. work vs. mobile."""
    # Enum values
    Fax: ClassVar[str] = "Fax"
    Mobile: ClassVar[str] = "Mobile"
    Personal: ClassVar[str] = "Personal"
    Work: ClassVar[str] = "Work"


# Import after class definition to avoid circular imports
TelephoneTypeEnum.model_rebuild()
