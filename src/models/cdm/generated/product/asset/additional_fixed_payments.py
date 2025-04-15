from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AdditionalFixedPayments(CdmModelBase):
    """A class to specify the events that will give rise to the payment additional fixed payments."""
    interest_shortfall_reimbursement: bool = Field(None, description="An additional Fixed Payment Event. Corresponds to the payment by or on behalf of the Issuer of an actual interest amount in respect to the reference obligation that is greater than the expected interest amount. ISDA 2003 Term: Interest Shortfall Reimbursement.")
    principal_shortfall_reimbursement: bool = Field(None, description="An additional Fixed Payment Event. Corresponds to the payment by or on behalf of the Issuer of an actual principal amount in respect to the reference obligation that is greater than the expected principal amount. ISDA 2003 Term: Principal Shortfall Reimbursement.")
    writedown_reimbursement: bool = Field(None, description="An Additional Fixed Payment. Corresponds to the payment by or on behalf of the issuer of an amount in respect to the reference obligation in reduction of the prior writedowns. ISDA 2003 Term: Writedown Reimbursement.")

# Import after class definition to avoid circular imports
AdditionalFixedPayments.model_rebuild()
