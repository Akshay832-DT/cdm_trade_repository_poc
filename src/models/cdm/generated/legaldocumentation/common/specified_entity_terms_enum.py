from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class SpecifiedEntityTermsEnum(CdmModelBase):
    """The enumerated values to specify the specified entity terms for the Event of Default or Termination Event specified."""
    # Enum values
    AnyAffiliate: ClassVar[str] = "AnyAffiliate"
    MaterialSubsidiary: ClassVar[str] = "MaterialSubsidiary"
    NamedSpecifiedEntity: ClassVar[str] = "NamedSpecifiedEntity"
    None: ClassVar[str] = "None"
    OtherSpecifiedEntity: ClassVar[str] = "OtherSpecifiedEntity"


# Import after class definition to avoid circular imports
SpecifiedEntityTermsEnum.model_rebuild()
