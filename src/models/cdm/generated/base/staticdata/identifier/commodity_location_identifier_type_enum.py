from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CommodityLocationIdentifierTypeEnum(CdmModelBase):
    """Defines the enumerated values to specify the nature of a location identifier."""
    # Enum values
    BuyerHub: ClassVar[str] = "BuyerHub"
    DeliveryPoint: ClassVar[str] = "DeliveryPoint"
    DeliveryZone: ClassVar[str] = "DeliveryZone"
    EntryPoint: ClassVar[str] = "EntryPoint"
    InterconnectionPoint: ClassVar[str] = "InterconnectionPoint"
    SellerHub: ClassVar[str] = "SellerHub"
    WithdrawalPoint: ClassVar[str] = "WithdrawalPoint"


# Import after class definition to avoid circular imports
CommodityLocationIdentifierTypeEnum.model_rebuild()
