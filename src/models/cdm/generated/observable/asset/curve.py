from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_commodity_reference_price_enum import FieldWithMetaCommodityReferencePriceEnum
    from src.models.cdm.generated.observable.asset.interest_rate_curve import InterestRateCurve

class Curve(CdmModelBase):
    """"""
    interest_rate_curve: ForwardRef("InterestRateCurve") = Field(None)
    commodity_curve: ForwardRef("FieldWithMetaCommodityReferencePriceEnum") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_commodity_reference_price_enum import FieldWithMetaCommodityReferencePriceEnum
from src.models.cdm.generated.observable.asset.interest_rate_curve import InterestRateCurve
Curve.model_rebuild()
