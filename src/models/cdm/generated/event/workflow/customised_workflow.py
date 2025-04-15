from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CustomisedWorkflow(CdmModelBase):
    """In its initial iteration, this class is meant to support the DTCC TIW workflow information."""
    item_name: str = Field(description="In this initial iteration, this corresponds to the DTCC TIW element name.")
    item_value: str = Field(description="In this initial iteration, this corresponds to the DTCC value.")

# Import after class definition to avoid circular imports
CustomisedWorkflow.model_rebuild()
