from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class StandardizedScheduleProductClassEnum(CdmModelBase):
    """"""
    # Enum values
    BasisSwap: ClassVar[str] = "BasisSwap"
    ContractForDifference: ClassVar[str] = "ContractForDifference"
    CorrelationSwap: ClassVar[str] = "CorrelationSwap"
    CreditNthToDefault: ClassVar[str] = "CreditNthToDefault"
    CreditTotalReturnSwapOnABond: ClassVar[str] = "CreditTotalReturnSwapOnABond"
    CrossCurrencySwap: ClassVar[str] = "CrossCurrencySwap"
    DeliverableForward: ClassVar[str] = "DeliverableForward"
    DeliverableOption: ClassVar[str] = "DeliverableOption"
    DeliverableOptionF: ClassVar[str] = "DeliverableOptionF"
    DeliverableSwap: ClassVar[str] = "DeliverableSwap"
    DividendSwap: ClassVar[str] = "DividendSwap"
    FixedFloatSwap: ClassVar[str] = "FixedFloatSwap"
    Forward: ClassVar[str] = "Forward"
    ForwardRateAgreement: ClassVar[str] = "ForwardRateAgreement"
    IRExoticSwapWithAnExoticCouponAgainstAFloatingLeg: ClassVar[str] = "IRExoticSwapWithAnExoticCouponAgainstAFloatingLeg"
    IndexCDS: ClassVar[str] = "IndexCDS"
    IndexTranche: ClassVar[str] = "IndexTranche"
    NonDeliverableCrossCurrencySwap: ClassVar[str] = "NonDeliverableCrossCurrencySwap"
    NonDeliverableForward: ClassVar[str] = "NonDeliverableForward"
    NonDeliverableOption: ClassVar[str] = "NonDeliverableOption"
    Option: ClassVar[str] = "Option"
    SingleNameCreditDefaultSwap: ClassVar[str] = "SingleNameCreditDefaultSwap"
    Swap: ClassVar[str] = "Swap"
    SwapWithCallableBermudanRightToEnterExitSwaps: ClassVar[str] = "SwapWithCallableBermudanRightToEnterExitSwaps"
    SwapsAndPortfolioSwaps: ClassVar[str] = "SwapsAndPortfolioSwaps"
    Swaption: ClassVar[str] = "Swaption"
    SwaptionStraddle: ClassVar[str] = "SwaptionStraddle"
    VarianceSwap: ClassVar[str] = "VarianceSwap"
    VolatilitySwap: ClassVar[str] = "VolatilitySwap"


# Import after class definition to avoid circular imports
StandardizedScheduleProductClassEnum.model_rebuild()
