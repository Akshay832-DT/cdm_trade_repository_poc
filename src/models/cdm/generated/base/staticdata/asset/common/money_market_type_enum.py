from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MoneyMarketTypeEnum(CdmModelBase):
    """"""
    # Enum values
    CertificateOfDeposit: ClassVar[str] = "CertificateOfDeposit"
    CommercialPaper: ClassVar[str] = "CommercialPaper"


# Import after class definition to avoid circular imports
MoneyMarketTypeEnum.model_rebuild()
