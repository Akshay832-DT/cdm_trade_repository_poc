from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.floatingrate.floating_rate_processing_parameters import FloatingRateProcessingParameters

class FloatingRateProcessingDetails(CdmModelBase):
    """Type for reporting the details of the rate treatment.  This could potentially be replaced by the existing FloatingRateDefinition type , but this is slightly more detailed."""
    raw_rate: float = Field(description="The raw or untreated rate, prior to any of the rate treatments.")
    processing_parameters: ForwardRef("FloatingRateProcessingParameters") = Field(None)
    processed_rate: float = Field(description="The value of the rate after processing.")
    spread_exclusive_rate: float = Field(description="The value of the processed rate without the spread applied, for subsequent compounding, etc.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.asset.floatingrate.floating_rate_processing_parameters import FloatingRateProcessingParameters
FloatingRateProcessingDetails.model_rebuild()
