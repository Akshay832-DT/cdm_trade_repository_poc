from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RollConventionEnum(CdmModelBase):
    """The enumerated values to specify the period term as part of a periodic schedule, i.e. the calculation period end date within the regular part of the calculation period. The value could be a rule, e.g. IMM Settlement Dates, which is the 3rd Wednesday of the month, or it could be a specific day of the month, such as the first day of the applicable month."""
    # Enum values
    EOM: ClassVar[str] = "EOM"
    FRI: ClassVar[str] = "FRI"
    FRN: ClassVar[str] = "FRN"
    IMM: ClassVar[str] = "IMM"
    IMMAUD: ClassVar[str] = "IMMAUD"
    IMMCAD: ClassVar[str] = "IMMCAD"
    IMMNZD: ClassVar[str] = "IMMNZD"
    MON: ClassVar[str] = "MON"
    NONE: ClassVar[str] = "NONE"
    SAT: ClassVar[str] = "SAT"
    SFE: ClassVar[str] = "SFE"
    SUN: ClassVar[str] = "SUN"
    TBILL: ClassVar[str] = "TBILL"
    THU: ClassVar[str] = "THU"
    TUE: ClassVar[str] = "TUE"
    WED: ClassVar[str] = "WED"
    _1: ClassVar[str] = "1"
    _10: ClassVar[str] = "10"
    _11: ClassVar[str] = "11"
    _12: ClassVar[str] = "12"
    _13: ClassVar[str] = "13"
    _14: ClassVar[str] = "14"
    _15: ClassVar[str] = "15"
    _16: ClassVar[str] = "16"
    _17: ClassVar[str] = "17"
    _18: ClassVar[str] = "18"
    _19: ClassVar[str] = "19"
    _2: ClassVar[str] = "2"
    _20: ClassVar[str] = "20"
    _21: ClassVar[str] = "21"
    _22: ClassVar[str] = "22"
    _23: ClassVar[str] = "23"
    _24: ClassVar[str] = "24"
    _25: ClassVar[str] = "25"
    _26: ClassVar[str] = "26"
    _27: ClassVar[str] = "27"
    _28: ClassVar[str] = "28"
    _29: ClassVar[str] = "29"
    _3: ClassVar[str] = "3"
    _30: ClassVar[str] = "30"
    _4: ClassVar[str] = "4"
    _5: ClassVar[str] = "5"
    _6: ClassVar[str] = "6"
    _7: ClassVar[str] = "7"
    _8: ClassVar[str] = "8"
    _9: ClassVar[str] = "9"


# Import after class definition to avoid circular imports
RollConventionEnum.model_rebuild()
