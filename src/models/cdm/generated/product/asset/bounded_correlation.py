from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class BoundedCorrelation(CdmModelBase):
    """Describes correlation bounds, which form a cap and a floor on the realized correlation."""
    minimum_boundary_percent: float = Field(None, description="Minimum Boundary as a percentage of the Strike Price.")
    maximum_boundary_percent: float = Field(None, description="Maximum Boundary as a percentage of the Strike Price.")

# Import after class definition to avoid circular imports
BoundedCorrelation.model_rebuild()
