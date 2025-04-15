from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class InstrumentTypeEnum(CdmModelBase):
    """Represents an enumeration list to indentify the type of an instrument."""
    # Enum values
    Certificate: ClassVar[str] = "Certificate"
    Debt: ClassVar[str] = "Debt"
    Equity: ClassVar[str] = "Equity"
    Fund: ClassVar[str] = "Fund"
    LetterOfCredit: ClassVar[str] = "LetterOfCredit"
    ListedDerivative: ClassVar[str] = "ListedDerivative"
    Warrant: ClassVar[str] = "Warrant"


# Import after class definition to avoid circular imports
InstrumentTypeEnum.model_rebuild()
