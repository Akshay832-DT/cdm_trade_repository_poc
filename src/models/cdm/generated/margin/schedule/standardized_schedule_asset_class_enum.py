from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class StandardizedScheduleAssetClassEnum(CdmModelBase):
    """"""
    # Enum values
    Commodity: ClassVar[str] = "Commodity"
    Credit: ClassVar[str] = "Credit"
    Equity: ClassVar[str] = "Equity"
    ForeignExchange: ClassVar[str] = "ForeignExchange"
    InterestRates: ClassVar[str] = "InterestRates"


# Import after class definition to avoid circular imports
StandardizedScheduleAssetClassEnum.model_rebuild()
