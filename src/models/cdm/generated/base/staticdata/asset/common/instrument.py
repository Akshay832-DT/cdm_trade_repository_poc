from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.listed_derivative import ListedDerivative
    from src.models.cdm.generated.base.staticdata.asset.common.loan import Loan
    from src.models.cdm.generated.base.staticdata.asset.common.security import Security

class Instrument(CdmModelBase):
    """A type of Asset that is issued by one party to one or more others."""
    listed_derivative: ForwardRef("ListedDerivative") = Field(None, description="A securitized derivative on another asset that is created by an exchange.")
    loan: ForwardRef("Loan") = Field(None, description="An Asset that represents a loan or borrow obligation.")
    security: ForwardRef("Security") = Field(None, description="An Asset that is issued by a party to be held by or transferred to others.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.listed_derivative import ListedDerivative
from src.models.cdm.generated.base.staticdata.asset.common.loan import Loan
from src.models.cdm.generated.base.staticdata.asset.common.security import Security
Instrument.model_rebuild()
