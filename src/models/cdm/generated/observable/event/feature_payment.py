from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.base.staticdata.party.party_reference_payer_receiver import PartyReferencePayerReceiver
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.observable.common.time_type_enum import TimeTypeEnum

class FeaturePayment(CdmModelBase):
    """Payment made following trigger occurrence."""
    payer_receiver: ForwardRef("PartyReferencePayerReceiver") = Field(description="This attribute doesn't exist as part of the FpML construct, which makes use of the PayerReceiver.model group.")
    level_percentage: float = Field(None, description="The trigger level percentage.")
    amount: float = Field(None, description="The monetary quantity in currency units.")
    time: ForwardRef("TimeTypeEnum") = Field(None, description="The feature payment time.")
    currency: ForwardRef("FieldWithMetaString") = Field(None, description="The currency in which an amount is denominated.")
    payment_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="The feature payment date.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.staticdata.party.party_reference_payer_receiver import PartyReferencePayerReceiver
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.common.time_type_enum import TimeTypeEnum
FeaturePayment.model_rebuild()
