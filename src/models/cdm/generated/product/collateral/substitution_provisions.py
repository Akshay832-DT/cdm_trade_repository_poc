from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period

class SubstitutionProvisions(CdmModelBase):
    """Defines collateral substitution provisions such as how many and with how much notice are substitutions allowed."""
    number_of_substitutions_allowed: int = Field(None, description="Specifies if 1 or more substitutions are allowed.")
    notice_deadline_period: ForwardRef("Period") = Field(None, description="Defines the min period for notify of a substitution.")
    notice_deadline_date_time: str = Field(None, description="A specific date and time for the notice deadline")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
SubstitutionProvisions.model_rebuild()
