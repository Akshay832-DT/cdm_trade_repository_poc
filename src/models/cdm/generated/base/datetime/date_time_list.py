from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DateTimeList(CdmModelBase):
    """List of dateTimes."""
    date_time: List[List] = Field(None, description="The CDM specifies that the zoned date time is to be expressed in accordance with ISO 8601, either as UTC as an offset to UTC.")

# Import after class definition to avoid circular imports
DateTimeList.model_rebuild()
