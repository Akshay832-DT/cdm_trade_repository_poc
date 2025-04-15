from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DebtClassEnum(CdmModelBase):
    """Represents an enumeration list that identifies the type of debt."""
    # Enum values
    AssetBacked: ClassVar[str] = "AssetBacked"
    Convertible: ClassVar[str] = "Convertible"
    HolderConvertible: ClassVar[str] = "HolderConvertible"
    HolderExchangeable: ClassVar[str] = "HolderExchangeable"
    IssuerConvertible: ClassVar[str] = "IssuerConvertible"
    IssuerExchangeable: ClassVar[str] = "IssuerExchangeable"
    RegCap: ClassVar[str] = "RegCap"
    Structured: ClassVar[str] = "Structured"
    Vanilla: ClassVar[str] = "Vanilla"


# Import after class definition to avoid circular imports
DebtClassEnum.model_rebuild()
