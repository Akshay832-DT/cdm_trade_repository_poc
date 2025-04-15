from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period
    from src.models.cdm.generated.metafields.field_with_meta_floating_rate_index_enum import FieldWithMetaFloatingRateIndexEnum

class InterestRateCurve(CdmModelBase):
    """"""
    floating_rate_index: ForwardRef("FieldWithMetaFloatingRateIndexEnum") = Field()
    tenor: ForwardRef("Period") = Field()

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
from src.models.cdm.generated.metafields.field_with_meta_floating_rate_index_enum import FieldWithMetaFloatingRateIndexEnum
InterestRateCurve.model_rebuild()
