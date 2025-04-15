from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.common.schedule.fx_linked_notional_schedule import FxLinkedNotionalSchedule

class QuantityMultiplier(CdmModelBase):
    """ Class to specify a mechanism for a quantity to be set as a multiplier to another (reference) quantity, based on a price observation. At the moment this class only supports FX or Equity-linked notional and re-uses existing building blocks for those 2 cases, until such time when component can be made more generic. This captures the case of resetting cross-currency swaps and resetting equity swaps."""
    fx_linked_notional_schedule: ForwardRef("FxLinkedNotionalSchedule") = Field(None, description="Multiplier specified as an FX-linked schedule, e.g. for a resetting cross-currency swap..")
    multiplier_value: float = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.common.schedule.fx_linked_notional_schedule import FxLinkedNotionalSchedule
QuantityMultiplier.model_rebuild()
