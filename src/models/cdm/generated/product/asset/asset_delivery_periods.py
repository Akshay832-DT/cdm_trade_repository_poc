from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.asset_delivery_profile import AssetDeliveryProfile

class AssetDeliveryPeriods(CdmModelBase):
    """Defines the periods of delivery, including the delivery profile."""
    profile: List[ForwardRef("AssetDeliveryProfile")] = Field(None, description="Defines the delivery profile of the asset, including the load type and the delivery intervals.")
    start_date: str = Field(None, description="Delivery start date")
    end_date: str = Field(None, description="Delivery end date")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.asset.asset_delivery_profile import AssetDeliveryProfile
AssetDeliveryPeriods.model_rebuild()
