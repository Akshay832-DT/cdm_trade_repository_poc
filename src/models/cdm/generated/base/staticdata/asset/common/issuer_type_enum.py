from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class IssuerTypeEnum(CdmModelBase):
    """Represents an enumeration list to identify the type of entity issuing the asset."""
    # Enum values
    Corporate: ClassVar[str] = "Corporate"
    Fund: ClassVar[str] = "Fund"
    QuasiGovernment: ClassVar[str] = "QuasiGovernment"
    RegionalGovernment: ClassVar[str] = "RegionalGovernment"
    SovereignCentralBank: ClassVar[str] = "SovereignCentralBank"
    SpecialPurposeVehicle: ClassVar[str] = "SpecialPurposeVehicle"
    SupraNational: ClassVar[str] = "SupraNational"


# Import after class definition to avoid circular imports
IssuerTypeEnum.model_rebuild()
