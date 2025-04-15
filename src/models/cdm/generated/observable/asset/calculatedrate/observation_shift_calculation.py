from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
    from src.models.cdm.generated.observable.asset.calculatedrate.observation_period_dates_enum import ObservationPeriodDatesEnum

class ObservationShiftCalculation(CdmModelBase):
    """Parameters to describe the observation shift for a daily compounded or averaged floating rate. This type is used to represent modular computed rates in interestRatePayouts."""
    offset_days: int = Field(None, description="The number of days of observation shift.")
    calculation_base: ForwardRef("ObservationPeriodDatesEnum") = Field(None, description="Whether the rate is calculated in advance, in arrears, or relative to a reset date.")
    additional_business_days: ForwardRef("BusinessCenters") = Field(None, description="Any additional business days that be applicable.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
from src.models.cdm.generated.observable.asset.calculatedrate.observation_period_dates_enum import ObservationPeriodDatesEnum
ObservationShiftCalculation.model_rebuild()
