from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AvailableInventoryTypeEnum(CdmModelBase):
    """Enumeration to describe the type of AvailableInventory"""
    # Enum values
    AvailableToLend: ClassVar[str] = "AvailableToLend"
    RequestToBorrow: ClassVar[str] = "RequestToBorrow"


# Import after class definition to avoid circular imports
AvailableInventoryTypeEnum.model_rebuild()
