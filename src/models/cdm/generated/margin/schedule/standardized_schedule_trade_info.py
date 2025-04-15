from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.margin.schedule.standardized_schedule_asset_class_enum import StandardizedScheduleAssetClassEnum
    from src.models.cdm.generated.margin.schedule.standardized_schedule_product_class_enum import StandardizedScheduleProductClassEnum
    from src.models.cdm.generated.observable.asset.money import Money

class StandardizedScheduleTradeInfo(CdmModelBase):
    """"""
    asset_class: ForwardRef("StandardizedScheduleAssetClassEnum") = Field(None)
    product_class: ForwardRef("StandardizedScheduleProductClassEnum") = Field(None)
    gross_initial_margin: ForwardRef("Money") = Field(None)
    mark_to_market_value: ForwardRef("Money") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.margin.schedule.standardized_schedule_asset_class_enum import StandardizedScheduleAssetClassEnum
from src.models.cdm.generated.margin.schedule.standardized_schedule_product_class_enum import StandardizedScheduleProductClassEnum
from src.models.cdm.generated.observable.asset.money import Money
StandardizedScheduleTradeInfo.model_rebuild()
