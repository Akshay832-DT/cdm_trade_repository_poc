from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ConcentrationLimitTypeEnum(CdmModelBase):
    """Represents the enumerated values to identify where a concentration limit is applied."""
    # Enum values
    Asset: ClassVar[str] = "Asset"
    BaseCurrencyEquivalent: ClassVar[str] = "BaseCurrencyEquivalent"
    IndustrySector: ClassVar[str] = "IndustrySector"
    IssueOutstandingAmount: ClassVar[str] = "IssueOutstandingAmount"
    Issuer: ClassVar[str] = "Issuer"
    MarketCapitalisation: ClassVar[str] = "MarketCapitalisation"
    PrimaryExchange: ClassVar[str] = "PrimaryExchange"
    UltimateParentInstitution: ClassVar[str] = "UltimateParentInstitution"


# Import after class definition to avoid circular imports
ConcentrationLimitTypeEnum.model_rebuild()
