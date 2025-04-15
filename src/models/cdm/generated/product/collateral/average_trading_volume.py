from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period
    from src.models.cdm.generated.product.collateral.average_trading_volume_methodology_enum import AverageTradingVolumeMethodologyEnum

class AverageTradingVolume(CdmModelBase):
    """Represents the average trading volume of an Equity product upon an exchange or set of exchanges."""
    period: ForwardRef("Period") = Field(description="Represents the period of the equities average trading volume on the exchange/s.")
    methodology: ForwardRef("AverageTradingVolumeMethodologyEnum") = Field(description="Indicates the type of equity average trading volume being stated (single) the highest amount on one exchange, or (consolidated) volumes across multiple exchanges.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
from src.models.cdm.generated.product.collateral.average_trading_volume_methodology_enum import AverageTradingVolumeMethodologyEnum
AverageTradingVolume.model_rebuild()
