from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TaxonomySourceEnum(CdmModelBase):
    """Represents the enumerated values to specify taxonomy sources."""
    # Enum values
    CFI: ClassVar[str] = "CFI"
    EMIR: ClassVar[str] = "EMIR"
    EU_EMIR_EligibleCollateralAssetClass: ClassVar[str] = "EU_EMIR_EligibleCollateralAssetClass"
    ICAD: ClassVar[str] = "ICAD"
    ISDA: ClassVar[str] = "ISDA"
    MAS: ClassVar[str] = "MAS"
    Other: ClassVar[str] = "Other"
    UK_EMIR_EligibleCollateralAssetClass: ClassVar[str] = "UK_EMIR_EligibleCollateralAssetClass"
    US_CFTC_PR_EligibleCollateralAssetClass: ClassVar[str] = "US_CFTC_PR_EligibleCollateralAssetClass"


# Import after class definition to avoid circular imports
TaxonomySourceEnum.model_rebuild()
