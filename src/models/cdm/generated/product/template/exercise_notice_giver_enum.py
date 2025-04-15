from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ExerciseNoticeGiverEnum(CdmModelBase):
    """Defines the principal party to the trade that has the right to exercise."""
    # Enum values
    AsSpecifiedInMasterAgreement: ClassVar[str] = "AsSpecifiedInMasterAgreement"
    Both: ClassVar[str] = "Both"
    Buyer: ClassVar[str] = "Buyer"
    Seller: ClassVar[str] = "Seller"


# Import after class definition to avoid circular imports
ExerciseNoticeGiverEnum.model_rebuild()
