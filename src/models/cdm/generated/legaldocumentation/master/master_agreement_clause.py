from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_clause_identifier_enum import MasterAgreementClauseIdentifierEnum
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_clause_variant import MasterAgreementClauseVariant

class MasterAgreementClause(CdmModelBase):
    """Defines clauses that make up a Master Agreement"""
    identifer: ForwardRef("MasterAgreementClauseIdentifierEnum") = Field(description="Unique identifier for the clause")
    name: str = Field(None, description="Optional textual description of the clause.")
    counterparty: List[ForwardRef("CounterpartyRoleEnum")] = Field(None, description="Optional counterparty role. This can be used where a clause needs to be assigned to a specific party on the agreement based upon their role i.e. Party A or Party B.")
    other_party: List[ForwardRef("PartyRoleEnum")] = Field(None, description="Optional party. This can be required for umbrella agreements where a clause may need to be assigned to a specific party who may or may not be on the agreement.")
    variant: List[ForwardRef("MasterAgreementClauseVariant")] = Field(None, description="Allows multiple variants to be defined for a clause. This needs to be an array as some clauses can specify different variants for different parties. At least one variant must be specified for a clause.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
from src.models.cdm.generated.legaldocumentation.master.master_agreement_clause_identifier_enum import MasterAgreementClauseIdentifierEnum
from src.models.cdm.generated.legaldocumentation.master.master_agreement_clause_variant import MasterAgreementClauseVariant
MasterAgreementClause.model_rebuild()
