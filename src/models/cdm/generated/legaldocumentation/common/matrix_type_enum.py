from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MatrixTypeEnum(CdmModelBase):
    """The enumerated values to specify the identification the form of applicable matrix."""
    # Enum values
    CreditDerivativesPhysicalSettlementMatrix: ClassVar[str] = "CreditDerivativesPhysicalSettlementMatrix"
    EquityDerivativesMatrix: ClassVar[str] = "EquityDerivativesMatrix"
    SettlementMatrix: ClassVar[str] = "SettlementMatrix"


# Import after class definition to avoid circular imports
MatrixTypeEnum.model_rebuild()
