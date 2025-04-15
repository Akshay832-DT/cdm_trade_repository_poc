from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.credit.obligations import Obligations
    from src.models.cdm.generated.observable.event.credit_events import CreditEvents
    from src.models.cdm.generated.product.asset.floating_amount_events import FloatingAmountEvents

class ProtectionTerms(CdmModelBase):
    """A class to specify the terms for calculating a payout to protect the buyer of the swap in the case of a qualified credit event. These terms include the applicable credit events, the reference obligation, and in the case of a CDS on mortgage-backed securities, the floatingAmountEvents."""
    credit_events: ForwardRef("CreditEvents") = Field(None, description="Specifies the applicable Credit Events that would trigger a settlement, as specified in the related Confirmation and defined in the ISDA 2014 Credit Definition article IV section 4.1.")
    obligations: ForwardRef("Obligations") = Field(None, description="The underlying obligations of the reference entity on which you are buying or selling protection. The credit events Failure to Pay, Obligation Acceleration, Obligation Default, Restructuring, Repudiation/Moratorium are defined with respect to these obligations.")
    floating_amount_events: ForwardRef("FloatingAmountEvents") = Field(None, description="This element contains the ISDA terms relating to the floating rate payment events and the implied additional fixed payments, applicable to the credit derivatives transactions on mortgage-backed securities with pay-as-you-go or physical settlement.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.credit.obligations import Obligations
from src.models.cdm.generated.observable.event.credit_events import CreditEvents
from src.models.cdm.generated.product.asset.floating_amount_events import FloatingAmountEvents
ProtectionTerms.model_rebuild()
