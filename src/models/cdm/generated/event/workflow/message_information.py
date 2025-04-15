from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class MessageInformation(CdmModelBase):
    """This class corresponds to the components of the FpML MessageHeader.model."""
    message_id: ForwardRef("FieldWithMetaString") = Field(description="A unique identifier assigned to the message.")
    sent_by: ForwardRef("FieldWithMetaString") = Field(None, description="The identifier for the originator of a message instance.")
    sent_to: List[ForwardRef("FieldWithMetaString")] = Field(None, description="The identifier(s) for the recipient(s) of a message instance.")
    copy_to: List[ForwardRef("FieldWithMetaString")] = Field(None, description="A unique identifier (within the specified coding scheme) giving the details of some party to whom a copy of this message will be sent for reference.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
MessageInformation.model_rebuild()
