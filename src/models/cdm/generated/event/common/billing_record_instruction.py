from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_trade_state import ReferenceWithMetaTradeState
    from src.models.cdm.generated.observable.event.observation import Observation

class BillingRecordInstruction(CdmModelBase):
    """Specifies the instructions for creation of a billing record."""
    trade_state: ForwardRef("ReferenceWithMetaTradeState") = Field(description="The trade for the individual billing record.")
    observation: List[ForwardRef("Observation")] = Field(None, description="The observations used to calculate the billing amount.")
    record_start_date: str = Field(description="The starting date of the period described by this record")
    record_end_date: str = Field(description="The ending date of the period described by this record")
    settlement_date: str = Field(description="The date for settlement of the transfer.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_trade_state import ReferenceWithMetaTradeState
from src.models.cdm.generated.observable.event.observation import Observation
BillingRecordInstruction.model_rebuild()
