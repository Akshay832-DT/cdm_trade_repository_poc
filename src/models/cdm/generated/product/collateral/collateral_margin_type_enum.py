from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CollateralMarginTypeEnum(CdmModelBase):
    """The enumerated values to specify the type of margin for which a legal agreement is named."""
    # Enum values
    InitialMargin: ClassVar[str] = "InitialMargin"
    VariationMargin: ClassVar[str] = "VariationMargin"


# Import after class definition to avoid circular imports
CollateralMarginTypeEnum.model_rebuild()
