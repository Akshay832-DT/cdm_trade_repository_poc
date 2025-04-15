"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.margin.schedule.standardized_schedule import StandardizedSchedule
    from src.models.cdm.generated.margin.schedule.standardized_schedule_asset_class_enum import StandardizedScheduleAssetClassEnum
    from src.models.cdm.generated.margin.schedule.standardized_schedule_initial_margin import StandardizedScheduleInitialMargin
    from src.models.cdm.generated.margin.schedule.standardized_schedule_product_class_enum import StandardizedScheduleProductClassEnum
    from src.models.cdm.generated.margin.schedule.standardized_schedule_trade_info import StandardizedScheduleTradeInfo
