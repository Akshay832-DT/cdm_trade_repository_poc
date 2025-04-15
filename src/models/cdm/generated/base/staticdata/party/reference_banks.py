from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.reference_bank import ReferenceBank

class ReferenceBanks(CdmModelBase):
    """A class defining the list of reference institutions polled for relevant rates or prices when determining the cash settlement amount for a product where cash settlement is applicable."""
    reference_bank: List[ForwardRef("ReferenceBank")] = Field(None, description="An institution (party) identified by means of a coding scheme and an optional name.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.reference_bank import ReferenceBank
ReferenceBanks.model_rebuild()
