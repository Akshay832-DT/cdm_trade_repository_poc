from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.margin.schedule.standardized_schedule_trade_info import StandardizedScheduleTradeInfo
    from src.models.cdm.generated.observable.asset.money import Money

class StandardizedScheduleInitialMargin(CdmModelBase):
    """"""
    trade_info: List[ForwardRef("StandardizedScheduleTradeInfo")] = Field(None)
    net_initial_margin: ForwardRef("Money") = Field()

# Import after class definition to avoid circular imports
from src.models.cdm.generated.margin.schedule.standardized_schedule_trade_info import StandardizedScheduleTradeInfo
from src.models.cdm.generated.observable.asset.money import Money
StandardizedScheduleInitialMargin.model_rebuild()
