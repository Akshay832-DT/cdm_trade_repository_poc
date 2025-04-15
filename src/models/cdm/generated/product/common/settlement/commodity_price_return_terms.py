from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.rounding import Rounding
    from src.models.cdm.generated.product.asset.spread_schedule import SpreadSchedule
    from src.models.cdm.generated.product.common.settlement.roll_feature import RollFeature

class CommodityPriceReturnTerms(CdmModelBase):
    """Defines parameters in which the commodity price is assessed."""
    rounding: ForwardRef("Rounding") = Field(None, description="Defines rounding rules and precision to be used in the rounding of a number.")
    spread: ForwardRef("SpreadSchedule") = Field(None, description="Defines a spread value for one or more defined dates.")
    roll_feature: ForwardRef("RollFeature") = Field(None, description="Used in conjunction with an exchange-based pricing source. Identifies a way in which the futures contracts referenced will roll between periods. ")
    conversion_factor: float = Field(None, description="Defines the conversion applied if the quantity unit on contract is different from unit on referenced underlier.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.rounding import Rounding
from src.models.cdm.generated.product.asset.spread_schedule import SpreadSchedule
from src.models.cdm.generated.product.common.settlement.roll_feature import RollFeature
CommodityPriceReturnTerms.model_rebuild()
