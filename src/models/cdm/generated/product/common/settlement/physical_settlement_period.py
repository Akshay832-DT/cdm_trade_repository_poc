from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PhysicalSettlementPeriod(CdmModelBase):
    """"""
    business_days_not_specified: bool = Field(None, description="An explicit indication that a number of business days are not specified and therefore ISDA fallback provisions should apply.")
    business_days: int = Field(None, description="A number of business days. Its precise meaning is dependant on the context in which this element is used. ISDA 2003 Term: Business Day.")
    maximum_business_days: int = Field(None, description="A maximum number of business days. Its precise meaning is dependant on the context in which this element is used. Intended to be used to limit a particular ISDA fallback provision.")

# Import after class definition to avoid circular imports
PhysicalSettlementPeriod.model_rebuild()
