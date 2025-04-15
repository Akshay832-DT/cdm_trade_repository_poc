from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_enum import BusinessCenterEnum
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.observable.event.publicly_available_information import PubliclyAvailableInformation

class CreditEventNotice(CdmModelBase):
    """"""
    notifying_party: List[ForwardRef("CounterpartyRoleEnum")] = Field(None, description="The notifying party is the party that notifies the other party when a credit event has occurred by means of a credit event notice. If more than one party is referenced as being the notifying party then either party may notify the other of a credit event occurring. ISDA 2003 Term: Notifying Party.")
    business_center: ForwardRef("BusinessCenterEnum") = Field(None, description="Inclusion of this business center element implies that Greenwich Mean Time in Section 3.3 of the 2003 ISDA Credit Derivatives Definitions is replaced by the local time of the city indicated by the businessCenter element value.")
    publicly_available_information: ForwardRef("PubliclyAvailableInformation") = Field(None, description="A specified condition to settlement. Publicly available information means information that reasonably confirms any of the facts relevant to determining that a credit event or potential repudiation/moratorium, as applicable, has occurred. The ISDA defined list (2003) is the market standard and is considered comprehensive, and a minimum of two differing public sources must have published the relevant information, to declare a Credit Event. ISDA 2003 Term: Notice of Publicly Available Information Applicable.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_enum import BusinessCenterEnum
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.observable.event.publicly_available_information import PubliclyAvailableInformation
CreditEventNotice.model_rebuild()
