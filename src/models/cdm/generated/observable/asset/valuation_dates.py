from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.performance_valuation_dates import PerformanceValuationDates

class ValuationDates(CdmModelBase):
    """Defines how and when a performance type option or performance type swap is to be valued, including initial, interim and final valuation dates."""
    initial_valuation_date: ForwardRef("PerformanceValuationDates") = Field(None, description="Specifies the initial valuation dates of the underlyer.")
    interim_valuation_date: ForwardRef("PerformanceValuationDates") = Field(None, description="Specifies the interim valuation dates of the underlyer.")
    final_valuation_date: ForwardRef("PerformanceValuationDates") = Field(description="Specifies the final valuation dates of the underlyer.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.performance_valuation_dates import PerformanceValuationDates
ValuationDates.model_rebuild()
