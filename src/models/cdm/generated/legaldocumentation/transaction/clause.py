from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.transaction.clause import Clause

class Clause(CdmModelBase):
    """A type for documenting additional clause that cannot yet be represented with the model and yet needed for a digital representation of the agreement"""
    identifier: str = Field(None, description="The  name or identifier associated to this clause ")
    terms: str = Field(None, description="Content of this bespoke clause")
    subcomponents: List[ForwardRef("Clause")] = Field(None, description="Additional hierarchichal components of the clause if relevant")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.transaction.clause import Clause
Clause.model_rebuild()
