from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_or_relative_date import AdjustableOrAdjustedOrRelativeDate
    from src.models.cdm.generated.base.math.non_negative_quantity import NonNegativeQuantity
    from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset

class AssetFlowBase(CdmModelBase):
    """Defines the basic parameters of an asset transfer, e.g. a cashflow: what (the asset), how much (the quantity) and when (the settlement date)."""
    quantity: ForwardRef("NonNegativeQuantity") = Field(description="Represents the amount of the asset to be transferred. The cashflow amount is always a positive number, as the cashflow direction is implied by the payer/receiver attribute.")
    asset: ForwardRef("Asset") = Field(description="Represents the object that is subject to the transfer, it could be an asset or a reference.")
    settlement_date: ForwardRef("AdjustableOrAdjustedOrRelativeDate") = Field(description="Represents the date on which the transfer to due.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_or_relative_date import AdjustableOrAdjustedOrRelativeDate
from src.models.cdm.generated.base.math.non_negative_quantity import NonNegativeQuantity
from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
AssetFlowBase.model_rebuild()
