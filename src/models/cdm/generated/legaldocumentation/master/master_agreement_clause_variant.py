from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_variable_set import MasterAgreementVariableSet
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_variant_identifier_enum import MasterAgreementVariantIdentifierEnum

class MasterAgreementClauseVariant(CdmModelBase):
    """Sets the details for a specific variant associated to a clause in a Master Agreement"""
    identifier: ForwardRef("MasterAgreementVariantIdentifierEnum") = Field(description="Unique identifier for this variant")
    name: str = Field(None, description="Optional textual description of the variant.")
    counterparty: List[ForwardRef("CounterpartyRoleEnum")] = Field(None, description="Optional counterparty role. This can be used where a clause needs to assign a different variant to the different parties on the agreement based upon their role i.e. Party A or Party B.")
    other_party: List[ForwardRef("PartyRoleEnum")] = Field(None, description="Optional party. This can be used where a clause needs to assign different variants to different parties who may or may not be on the agreement.")
    variable_set: List[ForwardRef("MasterAgreementVariableSet")] = Field(None, description="For some variants of some clauses additional details are required to work out what has been elected. This array can be used to define the name and value of these variables. Please refer to the agreement documentation for more details of the variables that are available for any clause.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
from src.models.cdm.generated.legaldocumentation.master.master_agreement_variable_set import MasterAgreementVariableSet
from src.models.cdm.generated.legaldocumentation.master.master_agreement_variant_identifier_enum import MasterAgreementVariantIdentifierEnum
MasterAgreementClauseVariant.model_rebuild()
