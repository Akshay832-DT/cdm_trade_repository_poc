from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money

class ShapingProvision(CdmModelBase):
    """Defines the applicable settlement limits that may require a settlement to be 'shaped', i.e. broken-down into smaller amounts."""
    shape_schedule: List[ForwardRef("Money")] = Field(None, description="Defines applicable settlement limits in each currency.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
ShapingProvision.model_rebuild()
