from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class WarehouseIdentityEnum(CdmModelBase):
    """"""
    # Enum values
    DTCC_TIW_Gold: ClassVar[str] = "DTCC_TIW_Gold"


# Import after class definition to avoid circular imports
WarehouseIdentityEnum.model_rebuild()
