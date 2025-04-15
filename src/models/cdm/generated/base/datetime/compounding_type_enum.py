from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CompoundingTypeEnum(CdmModelBase):
    """The enumerated values to specify how the compounding calculation is done"""
    # Enum values
    Business: ClassVar[str] = "Business"
    Calendar: ClassVar[str] = "Calendar"
    None: ClassVar[str] = "None"


# Import after class definition to avoid circular imports
CompoundingTypeEnum.model_rebuild()
