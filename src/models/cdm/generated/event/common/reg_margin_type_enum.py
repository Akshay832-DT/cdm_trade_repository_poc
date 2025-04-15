from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RegMarginTypeEnum(CdmModelBase):
    """Represents the enumeration values to specify the margin type in relation to bilateral or regulatory obligation."""
    # Enum values
    NonRegIM: ClassVar[str] = "NonRegIM"
    RegIM: ClassVar[str] = "RegIM"
    VM: ClassVar[str] = "VM"


# Import after class definition to avoid circular imports
RegMarginTypeEnum.model_rebuild()
