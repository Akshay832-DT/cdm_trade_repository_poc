from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RegIMRoleEnum(CdmModelBase):
    """Represents the enumeration values to specify the role of the party in relation to a regulatory initial margin call."""
    # Enum values
    Pledgor: ClassVar[str] = "Pledgor"
    Secured: ClassVar[str] = "Secured"


# Import after class definition to avoid circular imports
RegIMRoleEnum.model_rebuild()
