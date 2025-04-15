from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MultipleValuationDates(CdmModelBase):
    """"""
    business_days: int = Field(None, description="A number of business days. Its precise meaning is dependant on the context in which this element is used. ISDA 2003 Term: Business Day.")
    business_days_thereafter: int = Field(None, description="The number of business days between successive valuation dates when multiple valuation dates are applicable for cash settlement. ISDA 2003 Term: Business Days thereafter.")
    number_valuation_dates: int = Field(None, description="Where multiple valuation dates are specified as being applicable for cash settlement, this element specifies (a) the number of applicable valuation dates, and (b) the number of business days after satisfaction of all conditions to settlement when the first such valuation date occurs, and (c) the number of business days thereafter of each successive valuation date. ISDA 2003 Term: Multiple Valuation Dates.")

# Import after class definition to avoid circular imports
MultipleValuationDates.model_rebuild()
