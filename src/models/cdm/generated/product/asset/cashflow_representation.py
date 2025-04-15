from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.common.schedule.payment_calculation_period import PaymentCalculationPeriod

class CashflowRepresentation(CdmModelBase):
    """A data defining:  the cashflow representation of a swap trade."""
    cashflows_match_parameters: bool = Field(description="A true/false flag to indicate whether the cashflows match the parametric definition of the stream, i.e. whether the cashflows could be regenerated from the parameters without loss of information.")
    payment_calculation_period: List[ForwardRef("PaymentCalculationPeriod")] = Field(None, description="The adjusted payment date and associated calculation period parameters required to calculate the actual or projected payment amount. A list of payment calculation period elements may be ordered in the document by ascending adjusted payment date. An FpML document containing an unordered list of payment calculation periods is still regarded as a conformant document.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.common.schedule.payment_calculation_period import PaymentCalculationPeriod
CashflowRepresentation.model_rebuild()
