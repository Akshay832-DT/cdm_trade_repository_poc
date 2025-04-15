from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditSupportProviderTermsEnum(CdmModelBase):
    """The enumerated values to specify the Credit Support Provider Terms"""
    # Enum values
    Any: ClassVar[str] = "Any"
    None: ClassVar[str] = "None"
    Specified: ClassVar[str] = "Specified"


# Import after class definition to avoid circular imports
CreditSupportProviderTermsEnum.model_rebuild()
