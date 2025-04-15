from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.transfer import Transfer
    from src.models.cdm.generated.metafields.reference_with_meta_trade_state import ReferenceWithMetaTradeState
    from src.models.cdm.generated.observable.asset.money import Money

class BillingRecord(CdmModelBase):
    """Specifies individual records within a billing invoice."""
    trade_state: ForwardRef("ReferenceWithMetaTradeState") = Field(description="The trade for the individual billing record.")
    record_transfer: ForwardRef("Transfer") = Field(description="The settlement terms for the billing record")
    record_start_date: str = Field(description="The starting date of the period described by this record")
    record_end_date: str = Field(description="The ending date of the period described by this record")
    minimum_fee: ForwardRef("Money") = Field(None, description="Indicates the minimum fee amount applied to the billing record, if any.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.transfer import Transfer
from src.models.cdm.generated.metafields.reference_with_meta_trade_state import ReferenceWithMetaTradeState
from src.models.cdm.generated.observable.asset.money import Money
BillingRecord.model_rebuild()
