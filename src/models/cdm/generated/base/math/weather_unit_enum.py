from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class WeatherUnitEnum(CdmModelBase):
    """Provides enumerated values for weather units, generally used in the context of defining quantities for commodities."""
    # Enum values
    CDD: ClassVar[str] = "CDD"
    CPD: ClassVar[str] = "CPD"
    HDD: ClassVar[str] = "HDD"


# Import after class definition to avoid circular imports
WeatherUnitEnum.model_rebuild()
