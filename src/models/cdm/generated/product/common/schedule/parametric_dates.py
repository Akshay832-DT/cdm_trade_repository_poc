from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
    from src.models.cdm.generated.base.datetime.day_of_week_enum import DayOfWeekEnum
    from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum
    from src.models.cdm.generated.product.asset.day_distribution_enum import DayDistributionEnum
    from src.models.cdm.generated.product.common.schedule.lag import Lag

class ParametricDates(CdmModelBase):
    """Defines rules for the dates on which the price will be determined."""
    day_type: ForwardRef("DayTypeEnum") = Field(description="Denotes the enumerated values to specify the day type classification used in counting the number of days between two dates.")
    day_distribution: ForwardRef("DayDistributionEnum") = Field(None, description="Denotes the method by which the pricing days are distributed across the pricing period.")
    day_of_week: List[ForwardRef("DayOfWeekEnum")] = Field(None, description="Indicates the days of the week on which the price will be determined.")
    day_frequency: float = Field(None, description="Defines the occurrence of the dayOfWeek within the pricing period on which pricing will take place, e.g. the 3rd Friday within each Calculation Period. If omitted, every dayOfWeek will be a pricing day.")
    lag: ForwardRef("Lag") = Field(None, description="The pricing period per calculation period if the pricing days do not wholly fall within the respective calculation period.")
    business_centers: ForwardRef("BusinessCenters") = Field(description="The enumerated values to specify the business centers.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
from src.models.cdm.generated.base.datetime.day_of_week_enum import DayOfWeekEnum
from src.models.cdm.generated.base.datetime.day_type_enum import DayTypeEnum
from src.models.cdm.generated.product.asset.day_distribution_enum import DayDistributionEnum
from src.models.cdm.generated.product.common.schedule.lag import Lag
ParametricDates.model_rebuild()
