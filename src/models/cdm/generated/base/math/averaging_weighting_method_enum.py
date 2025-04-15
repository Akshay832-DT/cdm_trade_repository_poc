from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AveragingWeightingMethodEnum(CdmModelBase):
    """The enumerated values to specify the method of calculation to be used when averaging rates. Per ISDA 2000 Definitions, Section 6.2. Certain Definitions Relating to Floating Amounts."""
    # Enum values
    Unweighted: ClassVar[str] = "Unweighted"
    Weighted: ClassVar[str] = "Weighted"


# Import after class definition to avoid circular imports
AveragingWeightingMethodEnum.model_rebuild()
