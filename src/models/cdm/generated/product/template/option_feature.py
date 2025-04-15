from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.averaging_calculation import AveragingCalculation
    from src.models.cdm.generated.product.template.barrier import Barrier
    from src.models.cdm.generated.product.template.fx_feature import FxFeature
    from src.models.cdm.generated.product.template.knock import Knock
    from src.models.cdm.generated.product.template.pass_through import PassThrough
    from src.models.cdm.generated.product.template.strategy_feature import StrategyFeature

class OptionFeature(CdmModelBase):
    """Defines additional optional features that can be included in an option contract."""
    fx_feature: List[ForwardRef("FxFeature")] = Field(None, description="Describes a quanto or composite FX feature.")
    strategy_feature: ForwardRef("StrategyFeature") = Field(None, description="Defines a simple strategy feature.")
    averaging_feature: ForwardRef("AveragingCalculation") = Field(None, description="Defines an option feature in which an average market observation price is determined on valuation and compared to the strike to determine a settlement amount.")
    barrier: ForwardRef("Barrier") = Field(None, description="Specifies a barrier feature.")
    knock: ForwardRef("Knock") = Field(None, description="Specifies a knock in or knock out feature.")
    pass_through: ForwardRef("PassThrough") = Field(None, description="Specifies the rules for pass-through payments from the underlier, such as dividends.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.averaging_calculation import AveragingCalculation
from src.models.cdm.generated.product.template.barrier import Barrier
from src.models.cdm.generated.product.template.fx_feature import FxFeature
from src.models.cdm.generated.product.template.knock import Knock
from src.models.cdm.generated.product.template.pass_through import PassThrough
from src.models.cdm.generated.product.template.strategy_feature import StrategyFeature
OptionFeature.model_rebuild()
