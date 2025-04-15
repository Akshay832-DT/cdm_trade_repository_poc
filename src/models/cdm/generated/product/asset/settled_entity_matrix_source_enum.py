from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class SettledEntityMatrixSourceEnum(CdmModelBase):
    """The enumerated values to specify the relevant settled entity matrix source."""
    # Enum values
    ConfirmationAnnex: ClassVar[str] = "ConfirmationAnnex"
    NotApplicable: ClassVar[str] = "NotApplicable"
    Publisher: ClassVar[str] = "Publisher"


# Import after class definition to avoid circular imports
SettledEntityMatrixSourceEnum.model_rebuild()
