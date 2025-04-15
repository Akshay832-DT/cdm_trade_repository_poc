from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class SettlementTypeEnum(CdmModelBase):
    """The enumeration values to specify how the option is to be settled when exercised."""
    # Enum values
    Cash: ClassVar[str] = "Cash"
    CashOrPhysical: ClassVar[str] = "CashOrPhysical"
    Election: ClassVar[str] = "Election"
    Physical: ClassVar[str] = "Physical"


# Import after class definition to avoid circular imports
SettlementTypeEnum.model_rebuild()
