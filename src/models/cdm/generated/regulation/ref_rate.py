from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RefRate(CdmModelBase):
    """"""
    indx: str = Field()
    nm: str = Field()

# Import after class definition to avoid circular imports
RefRate.model_rebuild()
