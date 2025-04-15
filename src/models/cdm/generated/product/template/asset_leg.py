from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.product.common.settlement.delivery_method_enum import DeliveryMethodEnum

class AssetLeg(CdmModelBase):
    """Defines each asset movement of an asset payout."""
    settlement_date: ForwardRef("AdjustableOrRelativeDate") = Field(description="Specifies the settlement date of securities.  In a repo transaction the purchase date would always be the effective date as specified under Economic Terms, the repurchase date would always be the termination date as specified under Economic Terms.")
    delivery_method: ForwardRef("DeliveryMethodEnum") = Field(description="Specifies a delivery method for the security transaction.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.product.common.settlement.delivery_method_enum import DeliveryMethodEnum
AssetLeg.model_rebuild()
