from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_floating_rate_index_enum import FieldWithMetaFloatingRateIndexEnum
    from src.models.cdm.generated.product.asset.interest_shortfall_cap_enum import InterestShortfallCapEnum

class InterestShortFall(CdmModelBase):
    """A class to specify the interest shortfall floating rate payment event."""
    interest_shortfall_cap: ForwardRef("InterestShortfallCapEnum") = Field(description="Specifies the nature of the interest Shortfall cap (i.e. Fixed Cap or Variable Cap) in the case where it is applicable. ISDA 2003 Term: Interest Shortfall Cap.")
    compounding: bool = Field()
    rate_source: ForwardRef("FieldWithMetaFloatingRateIndexEnum") = Field(None, description="The rate source in the case of a variable cap.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_floating_rate_index_enum import FieldWithMetaFloatingRateIndexEnum
from src.models.cdm.generated.product.asset.interest_shortfall_cap_enum import InterestShortfallCapEnum
InterestShortFall.model_rebuild()
