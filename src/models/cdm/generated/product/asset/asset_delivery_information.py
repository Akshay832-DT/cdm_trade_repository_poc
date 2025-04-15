from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.quantity import Quantity
    from src.models.cdm.generated.base.staticdata.identifier.location_identifier import LocationIdentifier
    from src.models.cdm.generated.product.asset.asset_delivery_periods import AssetDeliveryPeriods

class AssetDeliveryInformation(CdmModelBase):
    """Contains the information relative to the delivery of the asset."""
    periods: ForwardRef("AssetDeliveryPeriods") = Field(None, description="Defines the periods of delivery, including the delivery profile.")
    location: List[ForwardRef("LocationIdentifier")] = Field(None, description="Defines the location of the delivery of the commodity.")
    delivery_capacity: ForwardRef("Quantity") = Field(None, description="The number of units included in the transaction for each delivery interval")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.quantity import Quantity
from src.models.cdm.generated.base.staticdata.identifier.location_identifier import LocationIdentifier
from src.models.cdm.generated.product.asset.asset_delivery_periods import AssetDeliveryPeriods
AssetDeliveryInformation.model_rebuild()
