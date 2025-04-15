from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class US_CFTC_PR_EligibleCollateralEnum(CdmModelBase):
    """Identifies US Eligible Collateral Assets classification categories based on Uncleared Margin Rules published by the CFTC and the US Prudential Regulator. Note: While the same basic categories exist in the CFTC and US Prudential Regulators margin rules, the precise definitions or application of those rules could differ between the two rules."""
    # Enum values
    US_CFTC_PRType1: ClassVar[str] = "US_CFTC_PRType1"
    US_CFTC_PRType2: ClassVar[str] = "US_CFTC_PRType2"
    US_CFTC_PRType3: ClassVar[str] = "US_CFTC_PRType3"
    US_CFTC_PRType4: ClassVar[str] = "US_CFTC_PRType4"
    US_CFTC_PRType5A: ClassVar[str] = "US_CFTC_PRType5A"
    US_CFTC_PRType5B: ClassVar[str] = "US_CFTC_PRType5B"
    US_CFTC_PRType6: ClassVar[str] = "US_CFTC_PRType6"
    US_CFTC_PRType7: ClassVar[str] = "US_CFTC_PRType7"
    US_CFTC_PRType8A: ClassVar[str] = "US_CFTC_PRType8A"
    US_CFTC_PRType8B: ClassVar[str] = "US_CFTC_PRType8B"
    US_CFTC_PRType8C: ClassVar[str] = "US_CFTC_PRType8C"
    US_CFTC_PRType9: ClassVar[str] = "US_CFTC_PRType9"
    US_CTFC_PRType10: ClassVar[str] = "US_CTFC_PRType10"


# Import after class definition to avoid circular imports
US_CFTC_PR_EligibleCollateralEnum.model_rebuild()
