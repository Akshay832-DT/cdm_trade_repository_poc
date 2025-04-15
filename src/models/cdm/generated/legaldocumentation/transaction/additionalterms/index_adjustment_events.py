from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class IndexAdjustmentEvents(CdmModelBase):
    """Defines the specification of the consequences of Index Events as defined by the 2002 ISDA Equity Derivatives Definitions."""

# Import after class definition to avoid circular imports
IndexAdjustmentEvents.model_rebuild()
