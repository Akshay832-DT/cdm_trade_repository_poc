from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PartyIdentifierTypeEnum(CdmModelBase):
    """The enumeration values associated with party identifier sources."""
    # Enum values
    BIC: ClassVar[str] = "BIC"
    LEI: ClassVar[str] = "LEI"
    MIC: ClassVar[str] = "MIC"


# Import after class definition to avoid circular imports
PartyIdentifierTypeEnum.model_rebuild()
