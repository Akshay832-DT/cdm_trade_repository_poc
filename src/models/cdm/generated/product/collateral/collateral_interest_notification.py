from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum

class CollateralInterestNotification(CdmModelBase):
    """Represents the parameters describing when notifications should be made for required collateral interest transfers."""
    trigger: str = Field(description="Specifies what triggers notification (should be enum) Interest Statement Frequency, Period End Date.")
    offset: float = Field(description="Specifies the number of days before (negative) or after (positive) the trigger event.")
    notification_time: str = Field(description="Specifies the time of day that the notification should occur.")
    notification_day_type: ForwardRef("DayTypeEnum") = Field(description="The type of days on which notification should occur.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum
CollateralInterestNotification.model_rebuild()
