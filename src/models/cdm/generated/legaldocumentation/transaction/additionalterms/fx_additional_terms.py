from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FxAdditionalTerms(CdmModelBase):
    """TransactionAdditionalTerms which apply to the CurrencyPair asset class."""

# Import after class definition to avoid circular imports
FxAdditionalTerms.model_rebuild()
