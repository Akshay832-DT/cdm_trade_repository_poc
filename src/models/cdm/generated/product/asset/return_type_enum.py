from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ReturnTypeEnum(CdmModelBase):
    """The enumerated values to specify the type of return associated the equity payout."""
    # Enum values
    Price: ClassVar[str] = "Price"
    Total: ClassVar[str] = "Total"


# Import after class definition to avoid circular imports
ReturnTypeEnum.model_rebuild()
