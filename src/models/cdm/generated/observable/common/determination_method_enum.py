from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DeterminationMethodEnum(CdmModelBase):
    """The enumerated values to specify the method according to which an amount or a date is determined."""
    # Enum values
    AgreedInitialPrice: ClassVar[str] = "AgreedInitialPrice"
    AsSpecifiedInMasterConfirmation: ClassVar[str] = "AsSpecifiedInMasterConfirmation"
    CalculationAgent: ClassVar[str] = "CalculationAgent"
    ClosingPrice: ClassVar[str] = "ClosingPrice"
    DividendCurrency: ClassVar[str] = "DividendCurrency"
    ExpiringContractLevel: ClassVar[str] = "ExpiringContractLevel"
    HedgeExecution: ClassVar[str] = "HedgeExecution"
    IssuerPaymentCurrency: ClassVar[str] = "IssuerPaymentCurrency"
    NAV: ClassVar[str] = "NAV"
    OSPPrice: ClassVar[str] = "OSPPrice"
    OpenPrice: ClassVar[str] = "OpenPrice"
    SettlementCurrency: ClassVar[str] = "SettlementCurrency"
    StrikeDateDetermination: ClassVar[str] = "StrikeDateDetermination"
    TWAPPrice: ClassVar[str] = "TWAPPrice"
    VWAPPrice: ClassVar[str] = "VWAPPrice"
    ValuationTime: ClassVar[str] = "ValuationTime"


# Import after class definition to avoid circular imports
DeterminationMethodEnum.model_rebuild()
