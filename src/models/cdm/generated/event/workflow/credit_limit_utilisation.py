from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.workflow.credit_limit_utilisation_position import CreditLimitUtilisationPosition

class CreditLimitUtilisation(CdmModelBase):
    """Credit limit utilisation breakdown by executed trades and pending orders."""
    executed: ForwardRef("CreditLimitUtilisationPosition") = Field(None, description="Credit limit utilisation attributable to executed trades.")
    pending: ForwardRef("CreditLimitUtilisationPosition") = Field(None, description="Credit limit utilisation attributable to pending unexecuted orders.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.workflow.credit_limit_utilisation_position import CreditLimitUtilisationPosition
CreditLimitUtilisation.model_rebuild()
