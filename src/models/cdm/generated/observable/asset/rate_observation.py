from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_rate_observation import ReferenceWithMetaRateObservation

class RateObservation(CdmModelBase):
    """A class defining parameters associated with an individual observation or fixing. This class forms part of the cashflow representation of a stream."""
    reset_date: str = Field(None, description="The reset date.")
    adjusted_fixing_date: str = Field(None, description="The adjusted fixing date, i.e. the actual date the rate is observed. The date should already be adjusted for any applicable business day convention.")
    observed_rate: float = Field(None, description="The actual observed rate before any required rate treatment is applied, e.g. before converting a rate quoted on a discount basis to an equivalent yield. An observed rate of 5% would be represented as 0.05.")
    treated_rate: float = Field(None, description="The observed rate after any required rate treatment is applied. A treated rate of 5% would be represented as 0.05.")
    observation_weight: int = Field(None, description="The number of days weighting to be associated with the rate observation, i.e. the number of days such rate is in effect. This is applicable in the case of a weighted average method of calculation where more than one reset date is established for a single calculation period.")
    rate_reference: ForwardRef("ReferenceWithMetaRateObservation") = Field(None, description="A pointer style reference to a floating rate component defined as part of a stub calculation period amount component. It is only required when it is necessary to distinguish two rate observations for the same fixing date which could occur when linear interpolation of two different rates occurs for a stub calculation period.")
    forecast_rate: float = Field(None, description="The value representing the forecast rate used to calculate the forecast future value of the accrual period.A value of 1% should be represented as 0.01.")
    treated_forecast_rate: float = Field(None, description="The value representing the forecast rate after applying rate treatment rules. A value of 1% should be represented as 0.01.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_rate_observation import ReferenceWithMetaRateObservation
RateObservation.model_rebuild()
