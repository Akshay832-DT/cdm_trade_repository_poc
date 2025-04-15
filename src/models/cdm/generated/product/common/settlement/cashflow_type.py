from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.cash_price import CashPrice
    from src.models.cdm.generated.observable.asset.price_expression_enum import PriceExpressionEnum
    from src.models.cdm.generated.product.common.settlement.scheduled_transfer_enum import ScheduledTransferEnum

class CashflowType(CdmModelBase):
    """Characterises the type of cashflow, which can result from either a scheduled or a non-scheduled lifecycle event."""
    cashflow_type: ForwardRef("ScheduledTransferEnum") = Field(None, description="Type of cashflow corresponding to a scheduled event.")
    cash_price: ForwardRef("CashPrice") = Field(None, description="Type of cashflow corresponding to a non-scheduled event, where a price must be agreed between the parties.")
    price_expression: ForwardRef("PriceExpressionEnum") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.cash_price import CashPrice
from src.models.cdm.generated.observable.asset.price_expression_enum import PriceExpressionEnum
from src.models.cdm.generated.product.common.settlement.scheduled_transfer_enum import ScheduledTransferEnum
CashflowType.model_rebuild()
