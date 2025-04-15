from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AverageTradingVolumeMethodologyEnum(CdmModelBase):
    """Indicates the type of equity average trading volume (single) the highest amount on one exchange, or (consolidated) volumes across more than one exchange."""
    # Enum values
    Consolidated: ClassVar[str] = "Consolidated"
    Single: ClassVar[str] = "Single"


# Import after class definition to avoid circular imports
AverageTradingVolumeMethodologyEnum.model_rebuild()
