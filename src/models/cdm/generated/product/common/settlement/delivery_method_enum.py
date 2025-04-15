from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DeliveryMethodEnum(CdmModelBase):
    """Specifies delivery methods for securities transactions. This coding-scheme defines the possible delivery methods for securities."""
    # Enum values
    DeliveryVersusPayment: ClassVar[str] = "DeliveryVersusPayment"
    FreeOfPayment: ClassVar[str] = "FreeOfPayment"
    PreDelivery: ClassVar[str] = "PreDelivery"
    PrePayment: ClassVar[str] = "PrePayment"


# Import after class definition to avoid circular imports
DeliveryMethodEnum.model_rebuild()
