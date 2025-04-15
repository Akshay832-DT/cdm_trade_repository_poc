from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identified_list import IdentifiedList
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.event.common.execution_type_enum import ExecutionTypeEnum

class ExecutionDetails(CdmModelBase):
    """Defines specific attributes that relate to trade executions."""
    execution_type: ForwardRef("ExecutionTypeEnum") = Field(description="Identifies the type of execution, e.g. via voice, electronically...")
    execution_venue: ForwardRef("LegalEntity") = Field(None, description="Represents the venue on which a trade was executed.")
    package_reference: ForwardRef("IdentifiedList") = Field(None, description="A reference to the package linking the trade with other trades, in case the trade was executed as part of a package (hence this attribute is optional).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identified_list import IdentifiedList
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.event.common.execution_type_enum import ExecutionTypeEnum
ExecutionDetails.model_rebuild()
