from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period_range import PeriodRange
    from src.models.cdm.generated.base.staticdata.asset.common.maturity_type_enum import MaturityTypeEnum

class AssetMaturity(CdmModelBase):
    """"""
    maturity_type: ForwardRef("MaturityTypeEnum") = Field(description="Specifies whether the maturity range is the remaining or original maturity.")
    maturity_range: ForwardRef("PeriodRange") = Field(description="Represents a filter based on the underlying asset maturity.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period_range import PeriodRange
from src.models.cdm.generated.base.staticdata.asset.common.maturity_type_enum import MaturityTypeEnum
AssetMaturity.model_rebuild()
