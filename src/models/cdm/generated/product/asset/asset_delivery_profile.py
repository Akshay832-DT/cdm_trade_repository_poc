from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.asset_delivery_profile_block import AssetDeliveryProfileBlock
    from src.models.cdm.generated.product.asset.bank_holiday_treatment_enum import BankHolidayTreatmentEnum
    from src.models.cdm.generated.product.asset.load_type_enum import LoadTypeEnum

class AssetDeliveryProfile(CdmModelBase):
    """Defines the delivery profile of the asset, including the load type and the delivery intervals."""
    load_type: ForwardRef("LoadTypeEnum") = Field(None, description="Identification of the delivery profile.")
    block: List[ForwardRef("AssetDeliveryProfileBlock")] = Field(None, description="Defines a delivery profile block, including start and end time, days of the week, duration, delivery capacity and price time interval quantity.")
    bank_holidays_treatment: ForwardRef("BankHolidayTreatmentEnum") = Field(None, description="Specifies whether the dates defined include holidays or not.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.asset.asset_delivery_profile_block import AssetDeliveryProfileBlock
from src.models.cdm.generated.product.asset.bank_holiday_treatment_enum import BankHolidayTreatmentEnum
from src.models.cdm.generated.product.asset.load_type_enum import LoadTypeEnum
AssetDeliveryProfile.model_rebuild()
