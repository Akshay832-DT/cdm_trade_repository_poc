from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ObligationCategoryEnum(CdmModelBase):
    """The enumerated values used in both the obligations and deliverable obligations of the credit default swap to represent a class or type of securities which apply."""
    # Enum values
    Bond: ClassVar[str] = "Bond"
    BondOrLoan: ClassVar[str] = "BondOrLoan"
    BorrowedMoney: ClassVar[str] = "BorrowedMoney"
    Loan: ClassVar[str] = "Loan"
    Payment: ClassVar[str] = "Payment"
    ReferenceObligationsOnly: ClassVar[str] = "ReferenceObligationsOnly"


# Import after class definition to avoid circular imports
ObligationCategoryEnum.model_rebuild()
