from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DomesticCurrencyIssued(CdmModelBase):
    """"""
    domestic_currency_issued: bool = Field(description="Identifies that the Security must be denominated in the domestic currency of the issuer.")

# Import after class definition to avoid circular imports
DomesticCurrencyIssued.model_rebuild()
