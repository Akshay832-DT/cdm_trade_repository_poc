from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DividendAmountTypeEnum(CdmModelBase):
    """The enumerated values to specify whether the dividend is paid with respect to the Dividend Period."""
    # Enum values
    AsSpecifiedInMasterConfirmation: ClassVar[str] = "AsSpecifiedInMasterConfirmation"
    ExAmount: ClassVar[str] = "ExAmount"
    PaidAmount: ClassVar[str] = "PaidAmount"
    RecordAmount: ClassVar[str] = "RecordAmount"


# Import after class definition to avoid circular imports
DividendAmountTypeEnum.model_rebuild()
