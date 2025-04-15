from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class InstructionFunctionEnum(CdmModelBase):
    """The enumeration values indicating the BusinessEvent function associated input instructions."""
    # Enum values
    Compression: ClassVar[str] = "Compression"
    ContractFormation: ClassVar[str] = "ContractFormation"
    Execution: ClassVar[str] = "Execution"
    QuantityChange: ClassVar[str] = "QuantityChange"
    Renegotiation: ClassVar[str] = "Renegotiation"


# Import after class definition to avoid circular imports
InstructionFunctionEnum.model_rebuild()
