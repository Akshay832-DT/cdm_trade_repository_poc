from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CounterpartyOwnIssuePermitted(CdmModelBase):
    """"""
    counterparty_own_issue_permitted: bool = Field(description="Represents a filter based on whether it is permitted for the underlying asset to be issued by the posting entity or part of their corporate family.")

# Import after class definition to avoid circular imports
CounterpartyOwnIssuePermitted.model_rebuild()
