from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class EquityCorporateEvents(CdmModelBase):
    """A class for defining the merger events and their treatment."""

# Import after class definition to avoid circular imports
EquityCorporateEvents.model_rebuild()
