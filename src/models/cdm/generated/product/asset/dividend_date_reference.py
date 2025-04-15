from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.offset import Offset
    from src.models.cdm.generated.product.asset.dividend_date_reference_enum import DividendDateReferenceEnum

class DividendDateReference(CdmModelBase):
    """A class to specify the dividend date by reference to another date, with the ability to apply and offset. This class doesn't exist in FpML and is meant to simplify the choice constraint associated with the DividendPaymentDate class."""
    date_reference: ForwardRef("DividendDateReferenceEnum") = Field(description="Specification of the dividend date using an enumeration, with values such as the pay date, the ex-date or the record date.")
    payment_date_offset: ForwardRef("Offset") = Field(None, description="Only to be used when SharePayment has been specified in the dividendDateReference element. The number of Currency Business Days following the day on which the Issuer of the Shares pays the relevant dividend to holders of record of the Shares.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.offset import Offset
from src.models.cdm.generated.product.asset.dividend_date_reference_enum import DividendDateReferenceEnum
DividendDateReference.model_rebuild()
