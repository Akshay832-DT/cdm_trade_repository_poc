from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class EventTimestampQualificationEnum(CdmModelBase):
    """The enumeration values to qualify the timestamps that can be associated with a lifecycle event. The reason for such approach is that the experience of integrating the DTCC and CME data representations suggests that a wide set of timestamps are currently utilized among service providers, while there is not at present an objective set of criteria that could help suggest a defined set of timestamps as part of the CDM. Implementers are expected to evaluate the current enumeration values to determine whether those meet their requirements. If not, they are expected to engage with the CDM team to evaluate the addition of further value(s) to this enumeration, which will then participate to the development of a compendium for further evaluation at a later point in order to determine whether this modeling is appropriate."""
    # Enum values
    clearingConfirmationDateTime: ClassVar[str] = "clearingConfirmationDateTime"
    clearingDateTime: ClassVar[str] = "clearingDateTime"
    clearingReceiptDateTime: ClassVar[str] = "clearingReceiptDateTime"
    clearingSubmissionDateTime: ClassVar[str] = "clearingSubmissionDateTime"
    confirmationDateTime: ClassVar[str] = "confirmationDateTime"
    eventCreationDateTime: ClassVar[str] = "eventCreationDateTime"
    eventExpirationDateTime: ClassVar[str] = "eventExpirationDateTime"
    eventProcessingDateTime: ClassVar[str] = "eventProcessingDateTime"
    eventSentDateTime: ClassVar[str] = "eventSentDateTime"
    eventSubmittedDateTime: ClassVar[str] = "eventSubmittedDateTime"
    executionDateTime: ClassVar[str] = "executionDateTime"
    transactionCreationDateTime: ClassVar[str] = "transactionCreationDateTime"


# Import after class definition to avoid circular imports
EventTimestampQualificationEnum.model_rebuild()
