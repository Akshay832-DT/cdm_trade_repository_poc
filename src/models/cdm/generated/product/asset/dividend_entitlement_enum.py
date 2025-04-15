from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DividendEntitlementEnum(CdmModelBase):
    """The enumerated values to specify the date on which the receiver of the equity payout is entitled to the dividend."""
    # Enum values
    ExDate: ClassVar[str] = "ExDate"
    RecordDate: ClassVar[str] = "RecordDate"


# Import after class definition to avoid circular imports
DividendEntitlementEnum.model_rebuild()
