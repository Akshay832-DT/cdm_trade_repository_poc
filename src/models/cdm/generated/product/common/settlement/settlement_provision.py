from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.common.settlement.shaping_provision import ShapingProvision

class SettlementProvision(CdmModelBase):
    """Defines parameters that regulate a settlement, for instance whether this settlement should be netted with other ones or broken-down into smaller amounts."""
    shaping_provisions: ForwardRef("ShapingProvision") = Field(None, description="Defines the parameters that are necessary to 'shape' a settlement, i.e. break it down into smaller amounts.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.common.settlement.shaping_provision import ShapingProvision
SettlementProvision.model_rebuild()
