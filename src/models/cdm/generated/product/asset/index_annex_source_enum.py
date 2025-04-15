from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class IndexAnnexSourceEnum(CdmModelBase):
    """The enumerated values to specify the CDX index annex source."""
    # Enum values
    MasterConfirmation: ClassVar[str] = "MasterConfirmation"
    Publisher: ClassVar[str] = "Publisher"


# Import after class definition to avoid circular imports
IndexAnnexSourceEnum.model_rebuild()
