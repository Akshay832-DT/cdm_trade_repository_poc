from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditSupportAgreementTypeEnum(CdmModelBase):
    """The enumerated values to specify the type of Credit Support Agreement governing the transaction."""
    # Enum values
    CollateralTransferAgreement: ClassVar[str] = "CollateralTransferAgreement"
    CreditSupportAnnex: ClassVar[str] = "CreditSupportAnnex"
    CreditSupportDeed: ClassVar[str] = "CreditSupportDeed"


# Import after class definition to avoid circular imports
CreditSupportAgreementTypeEnum.model_rebuild()
