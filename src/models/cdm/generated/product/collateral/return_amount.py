from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ReturnAmount(CdmModelBase):
    """A class to specify the application of Interest Amount with respect the Return Amount."""
    includes_default_language: bool = Field(None, description="Default language is included when True, and excluded when False.")
    custom_election: str = Field(None, description="Custom election that might be specified by the parties to the agreement.")

# Import after class definition to avoid circular imports
ReturnAmount.model_rebuild()
