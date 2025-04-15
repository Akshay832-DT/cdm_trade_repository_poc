from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class LimitLevelEnum(CdmModelBase):
    """The enumeration values to specify the level at which the limit is set: customer business, proprietary business or account level. This is part of the CME specification for clearing credit limits, although not specified as a set of enumerated values as part of the clearing confirmation specification."""
    # Enum values
    Account: ClassVar[str] = "Account"
    Customer: ClassVar[str] = "Customer"
    House: ClassVar[str] = "House"


# Import after class definition to avoid circular imports
LimitLevelEnum.model_rebuild()
