from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MasterAgreementTypeEnum(CdmModelBase):
    """The enumerated values to specify the type of the master agreement governing the transaction."""
    # Enum values
    AFB: ClassVar[str] = "AFB"
    Bespoke: ClassVar[str] = "Bespoke"
    CMA: ClassVar[str] = "CMA"
    CMOF: ClassVar[str] = "CMOF"
    EEIPower: ClassVar[str] = "EEIPower"
    EFETElectricity: ClassVar[str] = "EFETElectricity"
    EFETGas: ClassVar[str] = "EFETGas"
    EMA: ClassVar[str] = "EMA"
    FBF: ClassVar[str] = "FBF"
    GMRA: ClassVar[str] = "GMRA"
    GMSLA: ClassVar[str] = "GMSLA"
    GTMA: ClassVar[str] = "GTMA"
    GasEDI: ClassVar[str] = "GasEDI"
    German: ClassVar[str] = "German"
    ICOM: ClassVar[str] = "ICOM"
    IETA_ERPA: ClassVar[str] = "IETA-ERPA"
    IETA_ETMA: ClassVar[str] = "IETA-ETMA"
    IETA_IETMA: ClassVar[str] = "IETA-IETMA"
    IFEMA: ClassVar[str] = "IFEMA"
    IFEOMA: ClassVar[str] = "IFEOMA"
    ISDAFIA_CDEA: ClassVar[str] = "ISDAFIA-CDEA"
    ISDAIIFM_TMA: ClassVar[str] = "ISDAIIFM-TMA"
    ISDAMaster: ClassVar[str] = "ISDAMaster"
    JSCC: ClassVar[str] = "JSCC"
    LBMA: ClassVar[str] = "LBMA"
    LEAP: ClassVar[str] = "LEAP"
    MCPSA: ClassVar[str] = "MCPSA"
    NAESBGas: ClassVar[str] = "NAESBGas"
    NBP: ClassVar[str] = "NBP"
    RussianDerivatives: ClassVar[str] = "RussianDerivatives"
    RussianRepo: ClassVar[str] = "RussianRepo"
    SCoTA: ClassVar[str] = "SCoTA"
    Swiss: ClassVar[str] = "Swiss"
    TTF: ClassVar[str] = "TTF"
    ZBT: ClassVar[str] = "ZBT"


# Import after class definition to avoid circular imports
MasterAgreementTypeEnum.model_rebuild()
