from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class LoanParticipation(CdmModelBase):
    """A class to specify loan with a participation agreement whereby the buyer is capable of creating, or procuring the creation of, a contractual right in favour of the seller that provides the seller with recourse to the participation seller for a specified share in any payments due under the relevant loan which are received by the participation seller. ISDA 2003 Term: Direct Loan Participation."""
    applicable: bool = Field(None, description="Indicates whether the provision is applicable.")
    partial_cash_settlement: bool = Field(None, description="Specifies whether either 'Partial Cash Settlement of Assignable Loans', 'Partial Cash Settlement of Consent Required Loans' or 'Partial Cash Settlement of Participations' is applicable. If this element is specified and Assignable Loan is a Deliverable Obligation Characteristic, any Assignable Loan that is deliverable, but where a non-receipt of Consent by the Physical Settlement Date has occurred, the Loan can be cash settled rather than physically delivered. If this element is specified and Consent Required Loan is a Deliverable Obligation Characteristic, any Consent Required Loan that is deliverable, but where a non-receipt of Consent by the Physical Settlement Date has occurred, the Loan can be cash settled rather than physically delivered. If this element is specified and Direct Loan Participation is a Deliverable Obligation Characteristic, any Participation that is deliverable, but where this participation has not been effected (has not come into effect) by the Physical Settlement Date, the participation can be cash settled rather than physically delivered.")
    qualifying_participation_seller: str = Field(None, description="If Direct Loan Participation is specified as a deliverable obligation characteristic, this specifies any requirements for the Qualifying Participation Seller. The requirements may be listed free-form. ISDA 2003 Term: Qualifying Participation Seller.")

# Import after class definition to avoid circular imports
LoanParticipation.model_rebuild()
