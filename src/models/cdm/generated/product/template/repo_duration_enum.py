from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RepoDurationEnum(CdmModelBase):
    """A duration code for a Repo (or Securities Lending) transaction. There are many business and market rules that are derived from the duration of the transaction."""
    # Enum values
    Overnight: ClassVar[str] = "Overnight"
    Term: ClassVar[str] = "Term"


# Import after class definition to avoid circular imports
RepoDurationEnum.model_rebuild()
