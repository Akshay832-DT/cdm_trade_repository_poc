from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class InterestShortfallCapEnum(CdmModelBase):
    """The enumerated values to specify the interest shortfall cap, applicable to mortgage derivatives."""
    # Enum values
    Fixed: ClassVar[str] = "Fixed"
    Variable: ClassVar[str] = "Variable"


# Import after class definition to avoid circular imports
InterestShortfallCapEnum.model_rebuild()
