from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.margin.schedule.standardized_schedule_asset_class_enum import StandardizedScheduleAssetClassEnum
    from src.models.cdm.generated.margin.schedule.standardized_schedule_product_class_enum import StandardizedScheduleProductClassEnum

class StandardizedSchedule(CdmModelBase):
    """"""
    asset_class: ForwardRef("StandardizedScheduleAssetClassEnum") = Field()
    product_class: ForwardRef("StandardizedScheduleProductClassEnum") = Field()
    notional: float = Field()
    notional_currency: str = Field()
    duration_in_years: float = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.margin.schedule.standardized_schedule_asset_class_enum import StandardizedScheduleAssetClassEnum
from src.models.cdm.generated.margin.schedule.standardized_schedule_product_class_enum import StandardizedScheduleProductClassEnum
StandardizedSchedule.model_rebuild()
