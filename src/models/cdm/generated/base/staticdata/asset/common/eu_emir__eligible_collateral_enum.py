from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class EU_EMIR_EligibleCollateralEnum(CdmModelBase):
    """Identifies European Union Eligible Collateral Assets classification categories based on EMIR Uncleared Margin Rules. Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM."""
    # Enum values
    EU_EMIRTypeA: ClassVar[str] = "EU_EMIRTypeA"
    EU_EMIRTypeB: ClassVar[str] = "EU_EMIRTypeB"
    EU_EMIRTypeC: ClassVar[str] = "EU_EMIRTypeC"
    EU_EMIRTypeD: ClassVar[str] = "EU_EMIRTypeD"
    EU_EMIRTypeE: ClassVar[str] = "EU_EMIRTypeE"
    EU_EMIRTypeF: ClassVar[str] = "EU_EMIRTypeF"
    EU_EMIRTypeG: ClassVar[str] = "EU_EMIRTypeG"
    EU_EMIRTypeH: ClassVar[str] = "EU_EMIRTypeH"
    EU_EMIRTypeI: ClassVar[str] = "EU_EMIRTypeI"
    EU_EMIRTypeJ: ClassVar[str] = "EU_EMIRTypeJ"
    EU_EMIRTypeK: ClassVar[str] = "EU_EMIRTypeK"
    EU_EMIRTypeL: ClassVar[str] = "EU_EMIRTypeL"
    EU_EMIRTypeM: ClassVar[str] = "EU_EMIRTypeM"
    EU_EMIRTypeN: ClassVar[str] = "EU_EMIRTypeN"
    EU_EMIRTypeO: ClassVar[str] = "EU_EMIRTypeO"
    EU_EMIRTypeP: ClassVar[str] = "EU_EMIRTypeP"
    EU_EMIRTypeQ: ClassVar[str] = "EU_EMIRTypeQ"
    EU_EMIRTypeR: ClassVar[str] = "EU_EMIRTypeR"


# Import after class definition to avoid circular imports
EU_EMIR_EligibleCollateralEnum.model_rebuild()
