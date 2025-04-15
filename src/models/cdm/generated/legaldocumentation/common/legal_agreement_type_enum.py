from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class LegalAgreementTypeEnum(CdmModelBase):
    """The enumerated values to specify the legal agreement type."""
    # Enum values
    BrokerConfirmation: ClassVar[str] = "BrokerConfirmation"
    Confirmation: ClassVar[str] = "Confirmation"
    CreditSupportAgreement: ClassVar[str] = "CreditSupportAgreement"
    MasterAgreement: ClassVar[str] = "MasterAgreement"
    MasterConfirmation: ClassVar[str] = "MasterConfirmation"
    Other: ClassVar[str] = "Other"
    SecurityAgreement: ClassVar[str] = "SecurityAgreement"


# Import after class definition to avoid circular imports
LegalAgreementTypeEnum.model_rebuild()
