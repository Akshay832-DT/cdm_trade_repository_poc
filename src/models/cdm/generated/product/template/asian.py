from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.common.schedule.averaging_period import AveragingPeriod
    from src.models.cdm.generated.product.template.averaging_in_out_enum import AveragingInOutEnum

class Asian(CdmModelBase):
    """As per ISDA 2002 Definitions."""
    averaging_in_out: ForwardRef("AveragingInOutEnum") = Field()
    strike_factor: float = Field(None, description="The factor of strike.")
    averaging_period_in: ForwardRef("AveragingPeriod") = Field(None, description="The averaging in period.")
    averaging_period_out: ForwardRef("AveragingPeriod") = Field(None, description="The averaging out period.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.common.schedule.averaging_period import AveragingPeriod
from src.models.cdm.generated.product.template.averaging_in_out_enum import AveragingInOutEnum
Asian.model_rebuild()
