from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PersonIdentifierTypeEnum(CdmModelBase):
    """The enumeration values associated with person identifier sources."""
    # Enum values
    ARNU: ClassVar[str] = "ARNU"
    CCPT: ClassVar[str] = "CCPT"
    CUST: ClassVar[str] = "CUST"
    DRLC: ClassVar[str] = "DRLC"
    EMPL: ClassVar[str] = "EMPL"
    NIDN: ClassVar[str] = "NIDN"
    NPID: ClassVar[str] = "NPID"
    PLID: ClassVar[str] = "PLID"
    SOSE: ClassVar[str] = "SOSE"
    TXID: ClassVar[str] = "TXID"


# Import after class definition to avoid circular imports
PersonIdentifierTypeEnum.model_rebuild()
