"""
FpML Complex Type - ReferenceInformationType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

class ReferenceInformationType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    referenceEntity: str = Field()
    referenceObligation: Optional[str] = Field(None)

# Update forward references
ReferenceInformationType.update_forward_refs()
