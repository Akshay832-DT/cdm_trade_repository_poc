from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DayTypeEnum(CdmModelBase):
    """Lists the enumerated values to specify the day type classification used in counting the number of days between two dates."""
    # Enum values
    Business: ClassVar[str] = "Business"
    Calendar: ClassVar[str] = "Calendar"
    CurrencyBusiness: ClassVar[str] = "CurrencyBusiness"
    ExchangeBusiness: ClassVar[str] = "ExchangeBusiness"
    ScheduledTradingDay: ClassVar[str] = "ScheduledTradingDay"


# Import after class definition to avoid circular imports
DayTypeEnum.model_rebuild()
