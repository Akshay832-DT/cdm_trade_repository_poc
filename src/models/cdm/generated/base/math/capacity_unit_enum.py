from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CapacityUnitEnum(CdmModelBase):
    """Provides enumerated values for capacity units, generally used in the context of defining quantities for commodities."""
    # Enum values
    ALW: ClassVar[str] = "ALW"
    BBL: ClassVar[str] = "BBL"
    BCF: ClassVar[str] = "BCF"
    BDFT: ClassVar[str] = "BDFT"
    CBM: ClassVar[str] = "CBM"
    CER: ClassVar[str] = "CER"
    CRT: ClassVar[str] = "CRT"
    DAG: ClassVar[str] = "DAG"
    DAY: ClassVar[str] = "DAY"
    DMTU: ClassVar[str] = "DMTU"
    ENVCRD: ClassVar[str] = "ENVCRD"
    ENVOFST: ClassVar[str] = "ENVOFST"
    FEU: ClassVar[str] = "FEU"
    G: ClassVar[str] = "G"
    GBBSH: ClassVar[str] = "GBBSH"
    GBBTU: ClassVar[str] = "GBBTU"
    GBCWT: ClassVar[str] = "GBCWT"
    GBGAL: ClassVar[str] = "GBGAL"
    GBMBTU: ClassVar[str] = "GBMBTU"
    GBMMBTU: ClassVar[str] = "GBMMBTU"
    GBT: ClassVar[str] = "GBT"
    GBTHM: ClassVar[str] = "GBTHM"
    GJ: ClassVar[str] = "GJ"
    GW: ClassVar[str] = "GW"
    GWH: ClassVar[str] = "GWH"
    HL: ClassVar[str] = "HL"
    HOGB: ClassVar[str] = "HOGB"
    ISOBTU: ClassVar[str] = "ISOBTU"
    ISOMBTU: ClassVar[str] = "ISOMBTU"
    ISOMMBTU: ClassVar[str] = "ISOMMBTU"
    ISOTHM: ClassVar[str] = "ISOTHM"
    J: ClassVar[str] = "J"
    KG: ClassVar[str] = "KG"
    KL: ClassVar[str] = "KL"
    KW: ClassVar[str] = "KW"
    KWD: ClassVar[str] = "KWD"
    KWH: ClassVar[str] = "KWH"
    KWM: ClassVar[str] = "KWM"
    KWMIN: ClassVar[str] = "KWMIN"
    KWY: ClassVar[str] = "KWY"
    L: ClassVar[str] = "L"
    LB: ClassVar[str] = "LB"
    MB: ClassVar[str] = "MB"
    MBF: ClassVar[str] = "MBF"
    MJ: ClassVar[str] = "MJ"
    MMBBL: ClassVar[str] = "MMBBL"
    MMBF: ClassVar[str] = "MMBF"
    MSF: ClassVar[str] = "MSF"
    MT: ClassVar[str] = "MT"
    MW: ClassVar[str] = "MW"
    MWD: ClassVar[str] = "MWD"
    MWH: ClassVar[str] = "MWH"
    MWM: ClassVar[str] = "MWM"
    MWMIN: ClassVar[str] = "MWMIN"
    MWY: ClassVar[str] = "MWY"
    OZT: ClassVar[str] = "OZT"
    SGB: ClassVar[str] = "SGB"
    TEU: ClassVar[str] = "TEU"
    USBSH: ClassVar[str] = "USBSH"
    USBTU: ClassVar[str] = "USBTU"
    USCWT: ClassVar[str] = "USCWT"
    USGAL: ClassVar[str] = "USGAL"
    USMBTU: ClassVar[str] = "USMBTU"
    USMMBTU: ClassVar[str] = "USMMBTU"
    UST: ClassVar[str] = "UST"
    USTHM: ClassVar[str] = "USTHM"


# Import after class definition to avoid circular imports
CapacityUnitEnum.model_rebuild()
