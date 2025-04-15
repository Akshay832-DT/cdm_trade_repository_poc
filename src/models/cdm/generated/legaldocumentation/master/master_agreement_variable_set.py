from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_variable_set import MasterAgreementVariableSet

class MasterAgreementVariableSet(CdmModelBase):
    """Defines a type where additional variables associated to clauses and their variants can be described."""
    variable_set: List[ForwardRef("MasterAgreementVariableSet")] = Field(None, description="For some variants a table of variables is required. To support this use case we need to be able to specify variables within variables. Including a variable set here gives us infinite nesting opportunities - realistically we are only ever expecting that a table would need to be defined for any particular clause, so we would expect two levels of nesting as a maximum i.e. variableSet->variableSet->name/value.")
    name: str = Field(None, description="The name of the variable")
    value: str = Field(None, description="The value for this variable")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.master.master_agreement_variable_set import MasterAgreementVariableSet
MasterAgreementVariableSet.model_rebuild()
