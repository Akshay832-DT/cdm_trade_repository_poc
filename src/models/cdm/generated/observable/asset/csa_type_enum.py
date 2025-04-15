from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CsaTypeEnum(CdmModelBase):
    """How is the Creadit Support Annex defined for this transaction as defined in the 2021 ISDA Definitions, section 18.2.1 """
    # Enum values
    ExistingCSA: ClassVar[str] = "ExistingCSA"
    NoCSA: ClassVar[str] = "NoCSA"
    ReferenceVMCSA: ClassVar[str] = "ReferenceVMCSA"


# Import after class definition to avoid circular imports
CsaTypeEnum.model_rebuild()
