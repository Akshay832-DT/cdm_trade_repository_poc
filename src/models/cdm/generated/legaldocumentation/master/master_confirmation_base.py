from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MasterConfirmationBase(CdmModelBase):
    """Legal agreement specification for General Terms and Elections that are applicable across multiple confirmations and are referenced by these confirmations."""

# Import after class definition to avoid circular imports
MasterConfirmationBase.model_rebuild()
