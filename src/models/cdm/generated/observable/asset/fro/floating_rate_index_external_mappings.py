from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_external_map import FloatingRateIndexExternalMap

class FloatingRateIndexExternalMappings(CdmModelBase):
    """Represents the mappings of FRO codes to other."""
    iso_code: ForwardRef("FloatingRateIndexExternalMap") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_external_map import FloatingRateIndexExternalMap
FloatingRateIndexExternalMappings.model_rebuild()
