from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.make_whole_amount import MakeWholeAmount
    from src.models.cdm.generated.observable.asset.swap_curve_valuation import SwapCurveValuation

class ReferenceSwapCurve(CdmModelBase):
    """A complex type used to specify the option and convertible bond option strike when expressed in reference to a swap curve."""
    swap_unwind_value: ForwardRef("SwapCurveValuation") = Field()
    make_whole_amount: ForwardRef("MakeWholeAmount") = Field(None, description="Amount to be paid by the buyer of the option if the option is exercised prior to the Early Call Date. (The market practice in the convertible bond option space being that the buyer should be penalised if he/she exercises the option early on.)")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.make_whole_amount import MakeWholeAmount
from src.models.cdm.generated.observable.asset.swap_curve_valuation import SwapCurveValuation
ReferenceSwapCurve.model_rebuild()
