from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DebtPrincipalEnum(CdmModelBase):
    """Represents an enumeration list that specifies the general rule for repayment of principal."""
    # Enum values
    Amortising: ClassVar[str] = "Amortising"
    Bullet: ClassVar[str] = "Bullet"
    Callable: ClassVar[str] = "Callable"
    IndexLinked: ClassVar[str] = "IndexLinked"
    InflationLinked: ClassVar[str] = "InflationLinked"
    OtherStructured: ClassVar[str] = "OtherStructured"
    PrincipalOnly: ClassVar[str] = "PrincipalOnly"
    Puttable: ClassVar[str] = "Puttable"


# Import after class definition to avoid circular imports
DebtPrincipalEnum.model_rebuild()
