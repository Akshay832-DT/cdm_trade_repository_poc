from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class SettlementCentreEnum(CdmModelBase):
    """Defines the settlement centre for a securities transaction."""
    # Enum values
    ClearstreamBankingLuxembourg: ClassVar[str] = "ClearstreamBankingLuxembourg"
    EuroclearBank: ClassVar[str] = "EuroclearBank"


# Import after class definition to avoid circular imports
SettlementCentreEnum.model_rebuild()
