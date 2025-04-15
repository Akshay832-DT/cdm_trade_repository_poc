from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ExpirationTimeTypeEnum(CdmModelBase):
    """The time of day at which the equity option expires, for example the official closing time of the exchange."""
    # Enum values
    AsSpecifiedInMasterConfirmation: ClassVar[str] = "AsSpecifiedInMasterConfirmation"
    Close: ClassVar[str] = "Close"
    DerivativesClose: ClassVar[str] = "DerivativesClose"
    OSP: ClassVar[str] = "OSP"
    Open: ClassVar[str] = "Open"
    SpecificTime: ClassVar[str] = "SpecificTime"
    XETRA: ClassVar[str] = "XETRA"


# Import after class definition to avoid circular imports
ExpirationTimeTypeEnum.model_rebuild()
