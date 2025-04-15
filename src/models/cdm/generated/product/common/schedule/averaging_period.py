from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.averaging_schedule import AveragingSchedule
    from src.models.cdm.generated.base.datetime.date_time_list import DateTimeList
    from src.models.cdm.generated.metafields.field_with_meta_market_disruption_enum import FieldWithMetaMarketDisruptionEnum
    from src.models.cdm.generated.product.common.schedule.averaging_observation_list import AveragingObservationList

class AveragingPeriod(CdmModelBase):
    """Period over which an average value is taken."""
    schedule: List[ForwardRef("AveragingSchedule")] = Field(None, description="A schedule for generating averaging observation dates.")
    averaging_date_times: ForwardRef("DateTimeList") = Field(None, description="An unweighted list of averaging observation date and times.")
    averaging_observations: ForwardRef("AveragingObservationList") = Field(None, description="A weighted list of averaging observation date and times.")
    market_disruption: ForwardRef("FieldWithMetaMarketDisruptionEnum") = Field(None, description="The market disruption event as defined by ISDA 2002 Definitions.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.averaging_schedule import AveragingSchedule
from src.models.cdm.generated.base.datetime.date_time_list import DateTimeList
from src.models.cdm.generated.metafields.field_with_meta_market_disruption_enum import FieldWithMetaMarketDisruptionEnum
from src.models.cdm.generated.product.common.schedule.averaging_observation_list import AveragingObservationList
AveragingPeriod.model_rebuild()
