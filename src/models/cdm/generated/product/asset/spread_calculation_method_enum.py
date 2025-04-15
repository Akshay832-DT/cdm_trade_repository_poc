from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class SpreadCalculationMethodEnum(CdmModelBase):
    """Method by which spread is calculated. For example on an asset swap: 'ParPar' or 'Proceeds' may be the method indicated."""
    # Enum values
    ParPar: ClassVar[str] = "ParPar"
    Proceeds: ClassVar[str] = "Proceeds"


# Import after class definition to avoid circular imports
SpreadCalculationMethodEnum.model_rebuild()
