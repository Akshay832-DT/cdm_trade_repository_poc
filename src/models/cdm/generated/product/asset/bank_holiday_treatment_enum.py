from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class BankHolidayTreatmentEnum(CdmModelBase):
    """Defines whether the bank holidays are treated as weekdays or weekends in terms of delivery profile in the context of commodity products, in particular those with peak or off-peak delivery profiles."""
    # Enum values
    AsWeekday: ClassVar[str] = "AsWeekday"
    AsWeekend: ClassVar[str] = "AsWeekend"


# Import after class definition to avoid circular imports
BankHolidayTreatmentEnum.model_rebuild()
