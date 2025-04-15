from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class SingleValuationDate(CdmModelBase):
    """A class to specify the number of business days after satisfaction of all conditions to settlement."""
    business_days: int = Field(None, description="A number of business days. Its precise meaning is dependant on the context in which this element is used. ISDA 2003 Term: Business Day.")

# Import after class definition to avoid circular imports
SingleValuationDate.model_rebuild()
