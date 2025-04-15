from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.quantity import Quantity
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.product.asset.asset_delivery_profile import AssetDeliveryProfile

class CalculationScheduleDeliveryPeriods(CdmModelBase):
    """Period and time profile over which the delivery takes place."""
    profile: List[ForwardRef("AssetDeliveryProfile")] = Field(None, description="Defines the delivery profile of the asset, including the load type and the delivery intervals.")
    start_date: str = Field(None, description="Delivery start date")
    end_date: str = Field(None, description="Delivery end date")
    delivery_capacity: ForwardRef("Quantity") = Field(None, description="The number of units included in the transaction for each delivery interval")
    price_time_interval_quantity: ForwardRef("Price") = Field(None, description="Price per quantity per delivery time interval.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.quantity import Quantity
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.product.asset.asset_delivery_profile import AssetDeliveryProfile
CalculationScheduleDeliveryPeriods.model_rebuild()
