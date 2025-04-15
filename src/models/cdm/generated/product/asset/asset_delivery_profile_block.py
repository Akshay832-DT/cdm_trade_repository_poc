from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.day_of_week_enum import DayOfWeekEnum
    from src.models.cdm.generated.base.math.quantity import Quantity
    from src.models.cdm.generated.observable.asset.price import Price

class AssetDeliveryProfileBlock(CdmModelBase):
    """Defines a delivery profile block, including start and end time, days of the week, duration, delivery capacity and price time interval quantity."""
    start_time: str = Field(None, description="The start time of the delivery interval for each block or shape.")
    end_time: str = Field(None, description="The end time of the delivery interval for each block or shape.")
    day_of_week: List[ForwardRef("DayOfWeekEnum")] = Field(None, description="The days of the week of the delivery.")
    delivery_capacity: ForwardRef("Quantity") = Field(None, description="The number of units included in the transaction for each delivery interval")
    price_time_interval_quantity: ForwardRef("Price") = Field(None, description="Price per quantity per delivery time interval.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.day_of_week_enum import DayOfWeekEnum
from src.models.cdm.generated.base.math.quantity import Quantity
from src.models.cdm.generated.observable.asset.price import Price
AssetDeliveryProfileBlock.model_rebuild()
