from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RecordAmountTypeEnum(CdmModelBase):
    """The enumeration of the account level for the billing summary."""
    # Enum values
    AccountTotal: ClassVar[str] = "AccountTotal"
    GrandTotal: ClassVar[str] = "GrandTotal"
    ParentTotal: ClassVar[str] = "ParentTotal"


# Import after class definition to avoid circular imports
RecordAmountTypeEnum.model_rebuild()
