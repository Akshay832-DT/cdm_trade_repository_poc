from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditRatingAgencyEnum(CdmModelBase):
    """Represents the enumerated values to specify the rating agencies."""
    # Enum values
    AMBest: ClassVar[str] = "AMBest"
    CBRS: ClassVar[str] = "CBRS"
    DBRS: ClassVar[str] = "DBRS"
    Fitch: ClassVar[str] = "Fitch"
    Japanagency: ClassVar[str] = "Japanagency"
    Moodys: ClassVar[str] = "Moodys"
    RatingAndInvestmentInformation: ClassVar[str] = "RatingAndInvestmentInformation"
    StandardAndPoors: ClassVar[str] = "StandardAndPoors"


# Import after class definition to avoid circular imports
CreditRatingAgencyEnum.model_rebuild()
