from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class WorkflowStatusEnum(CdmModelBase):
    """"""
    # Enum values
    Accepted: ClassVar[str] = "Accepted"
    Affirmed: ClassVar[str] = "Affirmed"
    Alleged: ClassVar[str] = "Alleged"
    Amended: ClassVar[str] = "Amended"
    Cancelled: ClassVar[str] = "Cancelled"
    Certain: ClassVar[str] = "Certain"
    Cleared: ClassVar[str] = "Cleared"
    Confirmed: ClassVar[str] = "Confirmed"
    Pending: ClassVar[str] = "Pending"
    Rejected: ClassVar[str] = "Rejected"
    Submitted: ClassVar[str] = "Submitted"
    Terminated: ClassVar[str] = "Terminated"
    Uncertain: ClassVar[str] = "Uncertain"
    Unconfirmed: ClassVar[str] = "Unconfirmed"


# Import after class definition to avoid circular imports
WorkflowStatusEnum.model_rebuild()
