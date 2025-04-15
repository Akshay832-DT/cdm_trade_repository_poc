from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.cash_price_type_enum import CashPriceTypeEnum
    from src.models.cdm.generated.observable.asset.fee_type_enum import FeeTypeEnum
    from src.models.cdm.generated.observable.asset.premium_expression import PremiumExpression

class CashPrice(CdmModelBase):
    """Specifies the nature of a cash price either as a fee type, cash price type, or premium expression."""
    cash_price_type: ForwardRef("CashPriceTypeEnum") = Field(description="Specifies the type of Cash Price.")
    premium_expression: ForwardRef("PremiumExpression") = Field(None, description="Specifies a premium when expressed in a way other than an amount, and any required forward starting price definition.")
    fee_type: ForwardRef("FeeTypeEnum") = Field(None, description="Specifies the event type associated with a fee.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.cash_price_type_enum import CashPriceTypeEnum
from src.models.cdm.generated.observable.asset.fee_type_enum import FeeTypeEnum
from src.models.cdm.generated.observable.asset.premium_expression import PremiumExpression
CashPrice.model_rebuild()
