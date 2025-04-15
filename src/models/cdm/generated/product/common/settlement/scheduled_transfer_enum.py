from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ScheduledTransferEnum(CdmModelBase):
    """The qualification of the type of cash flows associated with OTC derivatives contracts and their lifecycle events."""
    # Enum values
    CorporateAction: ClassVar[str] = "CorporateAction"
    Coupon: ClassVar[str] = "Coupon"
    CreditEvent: ClassVar[str] = "CreditEvent"
    DividendReturn: ClassVar[str] = "DividendReturn"
    Exercise: ClassVar[str] = "Exercise"
    FixedRateReturn: ClassVar[str] = "FixedRateReturn"
    FloatingRateReturn: ClassVar[str] = "FloatingRateReturn"
    FractionalAmount: ClassVar[str] = "FractionalAmount"
    InterestReturn: ClassVar[str] = "InterestReturn"
    NetInterest: ClassVar[str] = "NetInterest"
    Performance: ClassVar[str] = "Performance"
    PrincipalPayment: ClassVar[str] = "PrincipalPayment"


# Import after class definition to avoid circular imports
ScheduledTransferEnum.model_rebuild()
