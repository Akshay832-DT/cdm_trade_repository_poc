from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TransferSettlementEnum(CdmModelBase):
    """The enumeration values to specify how the transfer will settle, e.g. DvP."""
    # Enum values
    DeliveryVersusDelivery: ClassVar[str] = "DeliveryVersusDelivery"
    DeliveryVersusPayment: ClassVar[str] = "DeliveryVersusPayment"
    NotCentralSettlement: ClassVar[str] = "NotCentralSettlement"
    PaymentVersusPayment: ClassVar[str] = "PaymentVersusPayment"


# Import after class definition to avoid circular imports
TransferSettlementEnum.model_rebuild()
