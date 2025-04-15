from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CollateralStatusEnum(CdmModelBase):
    """Represents the enumeration list to identify the settlement status of the collateral."""
    # Enum values
    FullAmount: ClassVar[str] = "FullAmount"
    InTransitAmount: ClassVar[str] = "InTransitAmount"
    SettledAmount: ClassVar[str] = "SettledAmount"


# Import after class definition to avoid circular imports
CollateralStatusEnum.model_rebuild()
