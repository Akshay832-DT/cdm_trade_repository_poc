from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CallingPartyEnum(CdmModelBase):
    """Identifies a party to the on-demand repo transaction that has a right to demand for termination of the Security Finance transaction."""
    # Enum values
    AsDefinedInMasterAgreement: ClassVar[str] = "AsDefinedInMasterAgreement"
    Either: ClassVar[str] = "Either"
    InitialBuyer: ClassVar[str] = "InitialBuyer"
    InitialSeller: ClassVar[str] = "InitialSeller"


# Import after class definition to avoid circular imports
CallingPartyEnum.model_rebuild()
