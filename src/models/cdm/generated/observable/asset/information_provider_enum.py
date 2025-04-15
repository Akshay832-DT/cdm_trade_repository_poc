from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class InformationProviderEnum(CdmModelBase):
    """The enumerated values to specify the list of information providers."""
    # Enum values
    AssocBanksSingapore: ClassVar[str] = "AssocBanksSingapore"
    BancoCentralChile: ClassVar[str] = "BancoCentralChile"
    BankOfCanada: ClassVar[str] = "BankOfCanada"
    BankOfEngland: ClassVar[str] = "BankOfEngland"
    BankOfJapan: ClassVar[str] = "BankOfJapan"
    Bloomberg: ClassVar[str] = "Bloomberg"
    EuroCentralBank: ClassVar[str] = "EuroCentralBank"
    FHLBSF: ClassVar[str] = "FHLBSF"
    FederalReserve: ClassVar[str] = "FederalReserve"
    ICESWAP: ClassVar[str] = "ICESWAP"
    ISDA: ClassVar[str] = "ISDA"
    Refinitiv: ClassVar[str] = "Refinitiv"
    ReserveBankAustralia: ClassVar[str] = "ReserveBankAustralia"
    ReserveBankNewZealand: ClassVar[str] = "ReserveBankNewZealand"
    Reuters: ClassVar[str] = "Reuters"
    SAFEX: ClassVar[str] = "SAFEX"
    TOKYOSWAP: ClassVar[str] = "TOKYOSWAP"
    Telerate: ClassVar[str] = "Telerate"


# Import after class definition to avoid circular imports
InformationProviderEnum.model_rebuild()
