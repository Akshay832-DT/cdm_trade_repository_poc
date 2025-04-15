from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TimeTypeEnum(CdmModelBase):
    """The enumerated values to specify points in the day when option exercise and valuation can occur."""
    # Enum values
    AsSpecifiedInMasterConfirmation: ClassVar[str] = "AsSpecifiedInMasterConfirmation"
    Close: ClassVar[str] = "Close"
    DerivativesClose: ClassVar[str] = "DerivativesClose"
    OSP: ClassVar[str] = "OSP"
    Open: ClassVar[str] = "Open"
    SpecificTime: ClassVar[str] = "SpecificTime"
    XETRA: ClassVar[str] = "XETRA"


# Import after class definition to avoid circular imports
TimeTypeEnum.model_rebuild()
