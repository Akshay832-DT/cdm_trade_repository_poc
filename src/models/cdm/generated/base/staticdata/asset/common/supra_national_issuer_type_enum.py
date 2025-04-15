from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class SupraNationalIssuerTypeEnum(CdmModelBase):
    """Represents an enumeration list to identify the type of supranational entity issuing the asset."""
    # Enum values
    InternationalOrganisation: ClassVar[str] = "InternationalOrganisation"
    MultilateralBank: ClassVar[str] = "MultilateralBank"


# Import after class definition to avoid circular imports
SupraNationalIssuerTypeEnum.model_rebuild()
