from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ProductIdTypeEnum(CdmModelBase):
    """Provides the enumerated values to specify the product identifier source."""
    # Enum values
    BBGID: ClassVar[str] = "BBGID"
    BBGTICKER: ClassVar[str] = "BBGTICKER"
    CUSIP: ClassVar[str] = "CUSIP"
    FIGI: ClassVar[str] = "FIGI"
    ISDACRP: ClassVar[str] = "ISDACRP"
    ISIN: ClassVar[str] = "ISIN"
    Name: ClassVar[str] = "Name"
    Other: ClassVar[str] = "Other"
    RIC: ClassVar[str] = "RIC"
    SEDOL: ClassVar[str] = "SEDOL"
    Sicovam: ClassVar[str] = "Sicovam"
    UPI: ClassVar[str] = "UPI"
    Wertpapier: ClassVar[str] = "Wertpapier"


# Import after class definition to avoid circular imports
ProductIdTypeEnum.model_rebuild()
