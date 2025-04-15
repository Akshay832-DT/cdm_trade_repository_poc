from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AssetTransferTypeEnum(CdmModelBase):
    """The qualification of the type of asset transfer."""
    # Enum values
    FreeOfPayment: ClassVar[str] = "FreeOfPayment"


# Import after class definition to avoid circular imports
AssetTransferTypeEnum.model_rebuild()
