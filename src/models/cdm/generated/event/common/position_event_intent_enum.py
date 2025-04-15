from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PositionEventIntentEnum(CdmModelBase):
    """"""
    # Enum values
    CorporateActionAdjustment: ClassVar[str] = "CorporateActionAdjustment"
    Decrease: ClassVar[str] = "Decrease"
    Increase: ClassVar[str] = "Increase"
    OptionExercise: ClassVar[str] = "OptionExercise"
    PositionCreation: ClassVar[str] = "PositionCreation"
    Transfer: ClassVar[str] = "Transfer"
    Valuation: ClassVar[str] = "Valuation"


# Import after class definition to avoid circular imports
PositionEventIntentEnum.model_rebuild()
