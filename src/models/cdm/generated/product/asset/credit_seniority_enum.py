from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditSeniorityEnum(CdmModelBase):
    """Seniority of debt instruments comprising the index."""
    # Enum values
    Other: ClassVar[str] = "Other"
    SeniorLossAbsorbingCapacity: ClassVar[str] = "SeniorLossAbsorbingCapacity"
    SeniorSec: ClassVar[str] = "SeniorSec"
    SeniorUnSec: ClassVar[str] = "SeniorUnSec"
    SubLowerTier2: ClassVar[str] = "SubLowerTier2"
    SubTier1: ClassVar[str] = "SubTier1"
    SubTier3: ClassVar[str] = "SubTier3"
    SubUpperTier2: ClassVar[str] = "SubUpperTier2"


# Import after class definition to avoid circular imports
CreditSeniorityEnum.model_rebuild()
