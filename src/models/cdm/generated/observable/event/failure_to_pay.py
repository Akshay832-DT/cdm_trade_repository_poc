from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.observable.event.grace_period_extension import GracePeriodExtension

class FailureToPay(CdmModelBase):
    """"""
    applicable: bool = Field(description="Indicates whether the failure to pay provision is applicable.")
    grace_period_extension: ForwardRef("GracePeriodExtension") = Field(None, description="If this element is specified, indicates whether or not a grace period extension is applicable. ISDA 2003 Term: Grace Period Extension Applicable.")
    payment_requirement: ForwardRef("Money") = Field(None, description="Specifies a threshold for the failure to pay credit event. Market standard is USD 1,000,000 (JPY 100,000,000 for Japanese Yen trades) or its equivalent in the relevant obligation currency. This is applied on an aggregate basis across all Obligations of the Reference Entity. Intended to prevent technical/operational errors from triggering credit events. ISDA 2003 Term: Payment Requirement")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.observable.event.grace_period_extension import GracePeriodExtension
FailureToPay.model_rebuild()
