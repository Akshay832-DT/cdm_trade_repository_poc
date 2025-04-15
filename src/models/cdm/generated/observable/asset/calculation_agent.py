from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
    from src.models.cdm.generated.metafields.field_with_meta_business_center_enum import FieldWithMetaBusinessCenterEnum
    from src.models.cdm.generated.observable.asset.party_determination_enum import PartyDeterminationEnum

class CalculationAgent(CdmModelBase):
    """A class defining the ISDA calculation agent responsible for performing duties as defined in the applicable product definitions."""
    calculation_agent_party: ForwardRef("AncillaryRoleEnum") = Field(None, description="Specifies the party which is the ISDA Calculation Agent for the trade. If more than one party is referenced then the parties are assumed to be co-calculation agents, i.e. they have joint responsibility.")
    calculation_agent_party_enum: ForwardRef("PartyDeterminationEnum") = Field(None, description="Specifies the ISDA calculation agent responsible for performing duties as defined in the applicable product definitions. For example, the Calculation Agent may be defined as being the Non-exercising Party.")
    calculation_agent_business_center: ForwardRef("FieldWithMetaBusinessCenterEnum") = Field(None, description="The city in which the office through which ISDA Calculation Agent is acting for purposes of the transaction is located The short-form confirm for a trade that is executed under a Sovereign or Asia Pacific Master Confirmation Agreement ( MCA ), does not need to specify the Calculation Agent. However, the confirm does need to specify the Calculation Agent City. This is due to the fact that the MCA sets the value for Calculation Agent but does not set the value for Calculation Agent City.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
from src.models.cdm.generated.metafields.field_with_meta_business_center_enum import FieldWithMetaBusinessCenterEnum
from src.models.cdm.generated.observable.asset.party_determination_enum import PartyDeterminationEnum
CalculationAgent.model_rebuild()
