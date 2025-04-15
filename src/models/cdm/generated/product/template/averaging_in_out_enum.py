from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AveragingInOutEnum(CdmModelBase):
    """The enumerated values to specify the type of averaging used in an Asian option."""
    # Enum values
    Both: ClassVar[str] = "Both"
    In: ClassVar[str] = "In"
    Out: ClassVar[str] = "Out"


# Import after class definition to avoid circular imports
AveragingInOutEnum.model_rebuild()
