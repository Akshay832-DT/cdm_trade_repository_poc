from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ResourceTypeEnum(CdmModelBase):
    """The enumerated values to specify the type of a resource (e.g. document)."""
    # Enum values
    Confirmation: ClassVar[str] = "Confirmation"
    SupplementalMaterialEconomicTerms: ClassVar[str] = "SupplementalMaterialEconomicTerms"
    TermSheet: ClassVar[str] = "TermSheet"


# Import after class definition to avoid circular imports
ResourceTypeEnum.model_rebuild()
