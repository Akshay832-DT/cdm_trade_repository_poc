from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ValuationPostponement(CdmModelBase):
    """Specifies how long to wait to get a quote from a settlement rate option upon a price source disruption."""
    maximum_days_of_postponement: int = Field(description="The maximum number of days to wait for a quote from the disrupted settlement rate option before proceeding to the next method.")

# Import after class definition to avoid circular imports
ValuationPostponement.model_rebuild()
