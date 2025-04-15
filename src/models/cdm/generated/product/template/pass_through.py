from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.pass_through_item import PassThroughItem

class PassThrough(CdmModelBase):
    """Type which contains pass through payments."""
    pass_through_item: List[ForwardRef("PassThroughItem")] = Field(None, description="One to many pass through payment items.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.pass_through_item import PassThroughItem
PassThrough.model_rebuild()
