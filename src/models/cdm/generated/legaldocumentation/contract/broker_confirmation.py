from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_broker_confirmation_type_enum import FieldWithMetaBrokerConfirmationTypeEnum

class BrokerConfirmation(CdmModelBase):
    """Identifies the market sector in which the trade has been arranged."""
    broker_confirmation_type: ForwardRef("FieldWithMetaBrokerConfirmationTypeEnum") = Field(description="The type of broker confirmation executed between the parties.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_broker_confirmation_type_enum import FieldWithMetaBrokerConfirmationTypeEnum
BrokerConfirmation.model_rebuild()
