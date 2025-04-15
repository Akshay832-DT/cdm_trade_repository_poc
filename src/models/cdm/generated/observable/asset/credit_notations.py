from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.credit_notation import CreditNotation
    from src.models.cdm.generated.observable.asset.multiple_credit_notations import MultipleCreditNotations

class CreditNotations(CdmModelBase):
    """Represents the credit rating notation higher level construct, which provides the ability to specify multiple rating notations."""
    credit_notation: ForwardRef("CreditNotation") = Field(None, description="Specifies only one credit notation is determined.")
    credit_notations: ForwardRef("MultipleCreditNotations") = Field(None, description="Specifies if several credit notations exist, alongside an 'any' or 'all' or all condition.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.credit_notation import CreditNotation
from src.models.cdm.generated.observable.asset.multiple_credit_notations import MultipleCreditNotations
CreditNotations.model_rebuild()
