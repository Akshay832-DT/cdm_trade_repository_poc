from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PriceExpressionEnum(CdmModelBase):
    """Enumerated values to specify whether the price is expressed in absolute or relative terms."""
    # Enum values
    AbsoluteTerms: ClassVar[str] = "AbsoluteTerms"
    ParValueFraction: ClassVar[str] = "ParValueFraction"
    PerOption: ClassVar[str] = "PerOption"
    PercentageOfNotional: ClassVar[str] = "PercentageOfNotional"


# Import after class definition to avoid circular imports
PriceExpressionEnum.model_rebuild()
