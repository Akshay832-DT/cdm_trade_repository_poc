from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.base.math.rounding import Rounding
    from src.models.cdm.generated.observable.asset.fx_spot_rate_source import FxSpotRateSource
    from src.models.cdm.generated.observable.common.time_type_enum import TimeTypeEnum
    from src.models.cdm.generated.product.common.schedule.calculation_period_dates import CalculationPeriodDates
    from src.models.cdm.generated.product.common.schedule.observation_dates import ObservationDates

class ObservationTerms(CdmModelBase):
    """Class containing terms that are associated with observing a price/benchmark/index across either single or multiple observations. """
    observation_time: ForwardRef("BusinessCenterTime") = Field(None, description="Defines time in respect to a business calendar location that the price/benchmark/index is observed")
    observation_time_type: ForwardRef("TimeTypeEnum") = Field(None, description="The enumerated values to specify points in the day when option exercise and valuation can occur.")
    information_source: ForwardRef("FxSpotRateSource") = Field(None, description="The information source where a published or displayed market rate will be obtained, e.g. Telerate Page 3750.")
    precision: ForwardRef("Rounding") = Field(None, description="Defines rounding rules and precision to be used in the rounding of observations.")
    calculation_period_dates: ForwardRef("CalculationPeriodDates") = Field(None, description="Defines parameters used to generate the calculation period dates schedule, including the specification of any initial or final stub calculation periods. A calculation period schedule consists of an optional initial stub calculation period, one or more regular calculation periods and an optional final stub calculation period. In the absence of any initial or final stub calculation periods, the regular part of the calculation period schedule is assumed to be between the effective date and the termination date. No implicit stubs are allowed, i.e. stubs must be explicitly specified using an appropriate combination of firstPeriodStartDate, firstRegularPeriodStartDate and lastRegularPeriodEndDate.")
    observation_dates: ForwardRef("ObservationDates") = Field(description="Describes date details for a set of observation dates in parametric or non-parametric form.")
    number_of_observation_dates: int = Field(None, description="The number of observation dates between observation start date and observation end date.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.base.math.rounding import Rounding
from src.models.cdm.generated.observable.asset.fx_spot_rate_source import FxSpotRateSource
from src.models.cdm.generated.observable.common.time_type_enum import TimeTypeEnum
from src.models.cdm.generated.product.common.schedule.calculation_period_dates import CalculationPeriodDates
from src.models.cdm.generated.product.common.schedule.observation_dates import ObservationDates
ObservationTerms.model_rebuild()
