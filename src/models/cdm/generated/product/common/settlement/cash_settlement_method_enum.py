from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CashSettlementMethodEnum(CdmModelBase):
    """Defines the different cash settlement methods for a product where cash settlement is applicable."""
    # Enum values
    CashPriceAlternateMethod: ClassVar[str] = "CashPriceAlternateMethod"
    CashPriceMethod: ClassVar[str] = "CashPriceMethod"
    CollateralizedCashPriceMethod: ClassVar[str] = "CollateralizedCashPriceMethod"
    CrossCurrencyMethod: ClassVar[str] = "CrossCurrencyMethod"
    MidMarketCalculationAgentDetermination: ClassVar[str] = "MidMarketCalculationAgentDetermination"
    MidMarketIndicativeQuotations: ClassVar[str] = "MidMarketIndicativeQuotations"
    MidMarketIndicativeQuotationsAlternate: ClassVar[str] = "MidMarketIndicativeQuotationsAlternate"
    ParYieldCurveAdjustedMethod: ClassVar[str] = "ParYieldCurveAdjustedMethod"
    ParYieldCurveUnadjustedMethod: ClassVar[str] = "ParYieldCurveUnadjustedMethod"
    ReplacementValueCalculationAgentDetermination: ClassVar[str] = "ReplacementValueCalculationAgentDetermination"
    ReplacementValueFirmQuotations: ClassVar[str] = "ReplacementValueFirmQuotations"
    ZeroCouponYieldAdjustedMethod: ClassVar[str] = "ZeroCouponYieldAdjustedMethod"


# Import after class definition to avoid circular imports
CashSettlementMethodEnum.model_rebuild()
