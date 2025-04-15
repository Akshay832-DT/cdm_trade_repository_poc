from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DebtInterestEnum(CdmModelBase):
    """Represents an enumeration list that specifies the general rule for periodic interest rate payment."""
    # Enum values
    Fixed: ClassVar[str] = "Fixed"
    Floating: ClassVar[str] = "Floating"
    IndexLinked: ClassVar[str] = "IndexLinked"
    InflationLinked: ClassVar[str] = "InflationLinked"
    InterestOnly: ClassVar[str] = "InterestOnly"
    InverseFloating: ClassVar[str] = "InverseFloating"
    OtherStructured: ClassVar[str] = "OtherStructured"
    ZeroCoupon: ClassVar[str] = "ZeroCoupon"


# Import after class definition to avoid circular imports
DebtInterestEnum.model_rebuild()
