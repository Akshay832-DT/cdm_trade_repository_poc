from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class NaturalPersonRoleEnum(CdmModelBase):
    """The enumerated values for the natural person's role."""
    # Enum values
    Broker: ClassVar[str] = "Broker"
    Buyer: ClassVar[str] = "Buyer"
    DecisionMaker: ClassVar[str] = "DecisionMaker"
    ExecutionWithinFirm: ClassVar[str] = "ExecutionWithinFirm"
    InvestmentDecisionMaker: ClassVar[str] = "InvestmentDecisionMaker"
    Seller: ClassVar[str] = "Seller"
    Trader: ClassVar[str] = "Trader"


# Import after class definition to avoid circular imports
NaturalPersonRoleEnum.model_rebuild()
