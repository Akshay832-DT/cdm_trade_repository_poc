from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditLimitTypeEnum(CdmModelBase):
    """The enumeration values to qualify the type of credit limits."""
    # Enum values
    CS01: ClassVar[str] = "CS01"
    DV01: ClassVar[str] = "DV01"
    IM: ClassVar[str] = "IM"
    NPV: ClassVar[str] = "NPV"
    Notional: ClassVar[str] = "Notional"
    PV01: ClassVar[str] = "PV01"


# Import after class definition to avoid circular imports
CreditLimitTypeEnum.model_rebuild()
