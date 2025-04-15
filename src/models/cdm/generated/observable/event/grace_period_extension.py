from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.offset import Offset

class GracePeriodExtension(CdmModelBase):
    """"""
    applicable: bool = Field(description="Indicates whether the grace period extension provision is applicable.")
    grace_period: ForwardRef("Offset") = Field(None, description="The number of calendar or business days after any due date that the reference entity has to fulfil its obligations before a failure to pay credit event is deemed to have occurred. ISDA 2003 Term: Grace Period.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.offset import Offset
GracePeriodExtension.model_rebuild()
