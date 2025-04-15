from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FloatingRateIndexExternalMap(CdmModelBase):
    """A map for a single FRO to or from an equivalent or similar codes in a different standard such as ISO."""
    external_id: str = Field(description=" The FRO name that is being mapped to/from.")
    external_standard: str = Field(None, description="The standard/version to which the map applies.")

# Import after class definition to avoid circular imports
FloatingRateIndexExternalMap.model_rebuild()
