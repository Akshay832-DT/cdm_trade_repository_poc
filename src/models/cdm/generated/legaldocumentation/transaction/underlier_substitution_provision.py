from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.legaldocumentation.transaction.clause import Clause
    from src.models.cdm.generated.legaldocumentation.transaction.extraordinary_events import ExtraordinaryEvents

class UnderlierSubstitutionProvision(CdmModelBase):
    """Where parties describe any substitution terms."""
    who_may_substitute: List[ForwardRef("CounterpartyRoleEnum")] = Field(None, description="Designates which Counterparty to the transaction who has the right to trigger a substitution or to provide related determination e.g. for instance to qualify the effectiveness of an Event which may be a trigger for substitution, determine the replacement Share to substitute, etc. ; cardinality of this object is 2, in case parties jointly have this role.")
    substitution_be_spoke_terms: List[ForwardRef("Clause")] = Field(None, description="Where parties describe any substitution terms e.g. for instance the election criteria for an Asset to be eligible as the Substitute Asset to the prior Affected Asset in terms of sector of activity, currency, market capitalisation, liquidity, volatility, or any additional features that parties would agree to take into considerations, etc.")
    substitution_trigger_events: List[ForwardRef("ExtraordinaryEvents")] = Field(None, description="Where the parties may optionnally explictly specify the list of Events to be considered as a trigger for a Substitution.")
    disputing_party: ForwardRef("CounterpartyRoleEnum") = Field(None, description="Where the party who is not granted with the substitution role at least has a right to dispute the determination given by the counterparty with such role. As an example, a given PartyA is the unique Counterparty with the Role of WhoMaySubstitute, yet PartyB could be Disputing Party in regard of such Role.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.legaldocumentation.transaction.clause import Clause
from src.models.cdm.generated.legaldocumentation.transaction.extraordinary_events import ExtraordinaryEvents
UnderlierSubstitutionProvision.model_rebuild()
