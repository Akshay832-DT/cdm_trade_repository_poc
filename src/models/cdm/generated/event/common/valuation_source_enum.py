from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ValuationSourceEnum(CdmModelBase):
    """Source for the valuation of the transaction by the valuation party."""
    # Enum values
    CentralCounterparty: ClassVar[str] = "CentralCounterparty"


# Import after class definition to avoid circular imports
ValuationSourceEnum.model_rebuild()
