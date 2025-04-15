from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class EventIntentEnum(CdmModelBase):
    """The enumeration values to qualify the intent associated with a transaction event."""
    # Enum values
    Allocation: ClassVar[str] = "Allocation"
    CashFlow: ClassVar[str] = "CashFlow"
    Clearing: ClassVar[str] = "Clearing"
    Compression: ClassVar[str] = "Compression"
    ContractFormation: ClassVar[str] = "ContractFormation"
    ContractTermsAmendment: ClassVar[str] = "ContractTermsAmendment"
    CorporateActionAdjustment: ClassVar[str] = "CorporateActionAdjustment"
    CreditEvent: ClassVar[str] = "CreditEvent"
    Decrease: ClassVar[str] = "Decrease"
    EarlyTerminationProvision: ClassVar[str] = "EarlyTerminationProvision"
    Increase: ClassVar[str] = "Increase"
    IndexTransition: ClassVar[str] = "IndexTransition"
    NotionalReset: ClassVar[str] = "NotionalReset"
    NotionalStep: ClassVar[str] = "NotionalStep"
    Novation: ClassVar[str] = "Novation"
    ObservationRecord: ClassVar[str] = "ObservationRecord"
    OptionExercise: ClassVar[str] = "OptionExercise"
    OptionalCancellation: ClassVar[str] = "OptionalCancellation"
    OptionalExtension: ClassVar[str] = "OptionalExtension"
    PortfolioRebalancing: ClassVar[str] = "PortfolioRebalancing"
    PrincipalExchange: ClassVar[str] = "PrincipalExchange"
    Reallocation: ClassVar[str] = "Reallocation"
    Repurchase: ClassVar[str] = "Repurchase"


# Import after class definition to avoid circular imports
EventIntentEnum.model_rebuild()
