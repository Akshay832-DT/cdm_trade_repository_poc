from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DateRange(CdmModelBase):
    """A class defining a contiguous series of calendar dates. The date range is defined as all the dates between and including the start and the end date. The start date must fall on or before the end date."""
    start_date: str = Field(description="The first date of a date range.")
    end_date: str = Field(description="The last date of a date range.")

# Import after class definition to avoid circular imports
DateRange.model_rebuild()
