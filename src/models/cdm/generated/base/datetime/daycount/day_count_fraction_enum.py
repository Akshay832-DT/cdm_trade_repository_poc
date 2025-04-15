from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DayCountFractionEnum(CdmModelBase):
    """The enumerated values to specify the day count fraction."""
    # Enum values
    ACT_360: ClassVar[str] = "ACT/360"
    ACT_364: ClassVar[str] = "ACT/364"
    ACT_365L: ClassVar[str] = "ACT/365L"
    ACT_365_FIXED: ClassVar[str] = "ACT/365.FIXED"
    ACT_ACT_AFB: ClassVar[str] = "ACT/ACT.AFB"
    ACT_ACT_ICMA: ClassVar[str] = "ACT/ACT.ICMA"
    ACT_ACT_ISDA: ClassVar[str] = "ACT/ACT.ISDA"
    ACT_ACT_ISMA: ClassVar[str] = "ACT/ACT.ISMA"
    CAL_252: ClassVar[str] = "CAL/252"
    RBA_Bond_Basis: ClassVar[str] = "RBA Bond Basis"
    _1_1: ClassVar[str] = "1/1"
    _30E_360: ClassVar[str] = "30E/360"
    _30E_360_ISDA: ClassVar[str] = "30E/360.ISDA"
    _30_360: ClassVar[str] = "30/360"


# Import after class definition to avoid circular imports
DayCountFractionEnum.model_rebuild()
