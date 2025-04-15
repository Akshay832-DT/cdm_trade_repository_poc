from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class QuotationSideEnum(CdmModelBase):
    """The enumerated values to specify the side from which perspective a value is quoted."""
    # Enum values
    Afternoon: ClassVar[str] = "Afternoon"
    Ask: ClassVar[str] = "Ask"
    Bid: ClassVar[str] = "Bid"
    Closing: ClassVar[str] = "Closing"
    High: ClassVar[str] = "High"
    Index: ClassVar[str] = "Index"
    LocationalMarginal: ClassVar[str] = "LocationalMarginal"
    Low: ClassVar[str] = "Low"
    MarginalHourly: ClassVar[str] = "MarginalHourly"
    MarketClearing: ClassVar[str] = "MarketClearing"
    MeanOfBidAndAsk: ClassVar[str] = "MeanOfBidAndAsk"
    MeanOfHighAndLow: ClassVar[str] = "MeanOfHighAndLow"
    Mid: ClassVar[str] = "Mid"
    Morning: ClassVar[str] = "Morning"
    NationalSingle: ClassVar[str] = "NationalSingle"
    OSP: ClassVar[str] = "OSP"
    Official: ClassVar[str] = "Official"
    Opening: ClassVar[str] = "Opening"
    Settlement: ClassVar[str] = "Settlement"
    Spot: ClassVar[str] = "Spot"
    UnWeightedAverage: ClassVar[str] = "UnWeightedAverage"
    WeightedAverage: ClassVar[str] = "WeightedAverage"


# Import after class definition to avoid circular imports
QuotationSideEnum.model_rebuild()
