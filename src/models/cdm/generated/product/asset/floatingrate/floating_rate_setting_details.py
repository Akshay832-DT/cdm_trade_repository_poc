from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.calculatedrate.calculated_rate_details import CalculatedRateDetails

class FloatingRateSettingDetails(CdmModelBase):
    """Type for reporting the raw (untreated) observed or calculated rate for a calculation period.  If this is a calculated rate, it allows details of the observations and the resulting rate to be returned."""
    calculation_details: ForwardRef("CalculatedRateDetails") = Field(None, description="Calculated rate details (observation dates, values, and weights).")
    observation_date: str = Field(None, description="The day upon which the rate was observed (for term rates).")
    reset_date: str = Field(None, description="The day for which the rate is needed (e.g. period beginning or end date).")
    floating_rate: float = Field(description="The resulting rate that was observed or calculated.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.calculatedrate.calculated_rate_details import CalculatedRateDetails
FloatingRateSettingDetails.model_rebuild()
