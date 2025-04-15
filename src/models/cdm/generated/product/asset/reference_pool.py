from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.reference_pool_item import ReferencePoolItem

class ReferencePool(CdmModelBase):
    """This type contains all the reference pool items to define the reference entity and reference obligation(s) in the basket."""
    reference_pool_item: List[ForwardRef("ReferencePoolItem")] = Field(None, description="This type contains all the constituent weight and reference information.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.asset.reference_pool_item import ReferencePoolItem
ReferencePool.model_rebuild()
