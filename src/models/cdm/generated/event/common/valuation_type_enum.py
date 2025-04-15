from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ValuationTypeEnum(CdmModelBase):
    """Method used for the valuation of the transaction by the valuation party."""
    # Enum values
    MarkToMarket: ClassVar[str] = "MarkToMarket"
    MarkToModel: ClassVar[str] = "MarkToModel"


# Import after class definition to avoid circular imports
ValuationTypeEnum.model_rebuild()
