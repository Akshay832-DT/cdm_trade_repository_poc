from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.floating_rate_index import FloatingRateIndex
    from src.models.cdm.generated.observable.asset.inflation_index import InflationIndex

class InterestRateIndex(CdmModelBase):
    """An index based in interest rates or inflation rates in a certain market."""
    floating_rate_index: ForwardRef("FloatingRateIndex") = Field(None, description="An interest rate index which can change over time, e.g. the SONIA (Sterling Overnight Index Average) in the UK.")
    inflation_index: ForwardRef("InflationIndex") = Field(None, description="An index that measures inflation in a specific market, e.g. the US Consumer Price Index.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.floating_rate_index import FloatingRateIndex
from src.models.cdm.generated.observable.asset.inflation_index import InflationIndex
InterestRateIndex.model_rebuild()
