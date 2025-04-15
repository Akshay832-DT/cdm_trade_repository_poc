from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AssetTypeEnum(CdmModelBase):
    """Represents an enumeration list to identify the asset type."""
    # Enum values
    Cash: ClassVar[str] = "Cash"
    Commodity: ClassVar[str] = "Commodity"
    Other: ClassVar[str] = "Other"
    Security: ClassVar[str] = "Security"


# Import after class definition to avoid circular imports
AssetTypeEnum.model_rebuild()
