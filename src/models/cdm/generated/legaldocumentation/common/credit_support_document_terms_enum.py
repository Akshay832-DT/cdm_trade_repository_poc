from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditSupportDocumentTermsEnum(CdmModelBase):
    """The enumerated values to specify the Credit Support Document Terms"""
    # Enum values
    Any: ClassVar[str] = "Any"
    None: ClassVar[str] = "None"
    Specified: ClassVar[str] = "Specified"


# Import after class definition to avoid circular imports
CreditSupportDocumentTermsEnum.model_rebuild()
