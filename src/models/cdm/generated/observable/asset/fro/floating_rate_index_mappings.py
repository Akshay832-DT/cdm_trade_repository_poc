from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_map import FloatingRateIndexMap

class FloatingRateIndexMappings(CdmModelBase):
    """This type defines mappings between FROs in different definitional versions."""
    maps_to: ForwardRef("FloatingRateIndexMap") = Field(None, description="The successor FRO that this index maps to.")
    maps_from: List[ForwardRef("FloatingRateIndexMap")] = Field(None, description="The predecessor FRO(s) that this index maps to.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_map import FloatingRateIndexMap
FloatingRateIndexMappings.model_rebuild()
