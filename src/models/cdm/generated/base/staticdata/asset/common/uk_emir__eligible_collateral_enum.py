from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class UK_EMIR_EligibleCollateralEnum(CdmModelBase):
    """Identifies United Kingdom Eligible Collateral Assets classification categories based on UK Onshored EMIR Uncleared Margin Rules. Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: UK EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM."""
    # Enum values
    UK_EMIRTypeA: ClassVar[str] = "UK_EMIRTypeA"
    UK_EMIRTypeB: ClassVar[str] = "UK_EMIRTypeB"
    UK_EMIRTypeC: ClassVar[str] = "UK_EMIRTypeC"
    UK_EMIRTypeD: ClassVar[str] = "UK_EMIRTypeD"
    UK_EMIRTypeE: ClassVar[str] = "UK_EMIRTypeE"
    UK_EMIRTypeF: ClassVar[str] = "UK_EMIRTypeF"
    UK_EMIRTypeG: ClassVar[str] = "UK_EMIRTypeG"
    UK_EMIRTypeH: ClassVar[str] = "UK_EMIRTypeH"
    UK_EMIRTypeI: ClassVar[str] = "UK_EMIRTypeI"
    UK_EMIRTypeJ: ClassVar[str] = "UK_EMIRTypeJ"
    UK_EMIRTypeK: ClassVar[str] = "UK_EMIRTypeK"
    UK_EMIRTypeL: ClassVar[str] = "UK_EMIRTypeL"
    UK_EMIRTypeM: ClassVar[str] = "UK_EMIRTypeM"
    UK_EMIRTypeN: ClassVar[str] = "UK_EMIRTypeN"
    UK_EMIRTypeO: ClassVar[str] = "UK_EMIRTypeO"
    UK_EMIRTypeP: ClassVar[str] = "UK_EMIRTypeP"
    UK_EMIRTypeQ: ClassVar[str] = "UK_EMIRTypeQ"
    UK_EMIRTypeR: ClassVar[str] = "UK_EMIRTypeR"


# Import after class definition to avoid circular imports
UK_EMIR_EligibleCollateralEnum.model_rebuild()
