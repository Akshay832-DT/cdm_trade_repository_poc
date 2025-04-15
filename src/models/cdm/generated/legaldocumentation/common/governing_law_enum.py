from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class GoverningLawEnum(CdmModelBase):
    """The enumerated values to specify the law governing the contract or legal document."""
    # Enum values
    AsSpecifiedInMasterAgreement: ClassVar[str] = "AsSpecifiedInMasterAgreement"
    BE: ClassVar[str] = "BE"
    CAAB: ClassVar[str] = "CAAB"
    CABC: ClassVar[str] = "CABC"
    CAMN: ClassVar[str] = "CAMN"
    CAON: ClassVar[str] = "CAON"
    CAQC: ClassVar[str] = "CAQC"
    DE: ClassVar[str] = "DE"
    FR: ClassVar[str] = "FR"
    GBEN: ClassVar[str] = "GBEN"
    GBGY: ClassVar[str] = "GBGY"
    GBIM: ClassVar[str] = "GBIM"
    GBJY: ClassVar[str] = "GBJY"
    GBSC: ClassVar[str] = "GBSC"
    IE: ClassVar[str] = "IE"
    JP: ClassVar[str] = "JP"
    LU: ClassVar[str] = "LU"
    RelatedMasterAgreement: ClassVar[str] = "RelatedMasterAgreement"
    USCA: ClassVar[str] = "USCA"
    USDE: ClassVar[str] = "USDE"
    USIL: ClassVar[str] = "USIL"
    USNY: ClassVar[str] = "USNY"


# Import after class definition to avoid circular imports
GoverningLawEnum.model_rebuild()
