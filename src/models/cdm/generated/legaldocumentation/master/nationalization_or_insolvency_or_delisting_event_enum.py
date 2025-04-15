from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class NationalizationOrInsolvencyOrDelistingEventEnum(CdmModelBase):
    """Defines the consequences of nationalization, insolvency and delisting events relating to the underlying."""
    # Enum values
    CancellationAndPayment: ClassVar[str] = "CancellationAndPayment"
    NegotiatedCloseout: ClassVar[str] = "NegotiatedCloseout"


# Import after class definition to avoid circular imports
NationalizationOrInsolvencyOrDelistingEventEnum.model_rebuild()
