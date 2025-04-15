from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditLimitUtilisationPosition(CdmModelBase):
    """"""
    short_position: float = Field(None, description="Credit limit utilisation attributable to short positions.")
    long_position: float = Field(None, description="Credit limit utilisation attributable to long positions.")
    global_: float = Field(None, description="Global credit limit utilisation amount, agnostic of long/short position direction.")

# Import after class definition to avoid circular imports
CreditLimitUtilisationPosition.model_rebuild()
