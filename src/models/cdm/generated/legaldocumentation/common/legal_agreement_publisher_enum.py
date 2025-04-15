from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class LegalAgreementPublisherEnum(CdmModelBase):
    """The enumerated values to specify the legal agreement publisher."""
    # Enum values
    AFB: ClassVar[str] = "AFB"
    BNYM: ClassVar[str] = "BNYM"
    EMTA: ClassVar[str] = "EMTA"
    ICMA: ClassVar[str] = "ICMA"
    ISDA: ClassVar[str] = "ISDA"
    ISDAClearstream: ClassVar[str] = "ISDAClearstream"
    ISDAEuroclear: ClassVar[str] = "ISDAEuroclear"
    ISLA: ClassVar[str] = "ISLA"
    JPMorgan: ClassVar[str] = "JPMorgan"
    TheFXCommittee: ClassVar[str] = "TheFXCommittee"


# Import after class definition to avoid circular imports
LegalAgreementPublisherEnum.model_rebuild()
