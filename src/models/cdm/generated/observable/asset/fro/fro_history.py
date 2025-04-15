from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.fro.contractual_definition import ContractualDefinition

class FroHistory(CdmModelBase):
    """FRO History"""
    start_date: str = Field(None, description="The date the Floating Rate Option was added to the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. 2017/04/06)")
    first_defined_in: ForwardRef("ContractualDefinition") = Field(None, description="The supplement or version the FRO was first added to the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. S52)")
    update_date: str = Field(None, description="The date the Floating Rate Option was last updated in the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. 2021/06/11)")
    last_updated_in: ForwardRef("ContractualDefinition") = Field(None, description="The supplement or version the FRO was last updated in the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. FRO-M-V1)")
    end_date: str = Field(None, description="The date the Floating Rate Option was removed from the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. 2014/01/01)")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.fro.contractual_definition import ContractualDefinition
FroHistory.model_rebuild()
