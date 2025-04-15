from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
    from src.models.cdm.generated.observable.asset.fx_settlement_rate_source import FxSettlementRateSource

class FxRateSourceFixing(CdmModelBase):
    """Describes a rate source to be fixed and the date the fixing occurs"""
    settlement_rate_source: ForwardRef("FxSettlementRateSource") = Field()
    fixing_date: ForwardRef("AdjustableDate") = Field(description="The date on which the fixing is scheduled to occur.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
from src.models.cdm.generated.observable.asset.fx_settlement_rate_source import FxSettlementRateSource
FxRateSourceFixing.model_rebuild()
