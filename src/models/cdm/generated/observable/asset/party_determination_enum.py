from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PartyDeterminationEnum(CdmModelBase):
    """The enumerated values to specify how a calculation agent will be determined."""
    # Enum values
    AsSpecifiedInMasterAgreement: ClassVar[str] = "AsSpecifiedInMasterAgreement"
    AsSpecifiedInStandardTermsSupplement: ClassVar[str] = "AsSpecifiedInStandardTermsSupplement"
    Both: ClassVar[str] = "Both"
    ExercisingParty: ClassVar[str] = "ExercisingParty"
    NonExercisingParty: ClassVar[str] = "NonExercisingParty"


# Import after class definition to avoid circular imports
PartyDeterminationEnum.model_rebuild()
