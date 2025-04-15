from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DividendApplicability(CdmModelBase):
    """The parameters which define whether dividends are applicable"""
    options_exchange_dividends: bool = Field(None, description="If present and true, then options exchange dividends are applicable.")
    additional_dividends: bool = Field(None, description="If present and true, then additional dividends are applicable.")
    all_dividends: bool = Field(None, description="Represents the European Master Confirmation value of 'All Dividends' which, when applicable, signifies that, for a given Ex-Date, the daily observed Share Price for that day is adjusted (reduced) by the cash dividend and/or the cash value of any non cash dividend per Share (including Extraordinary Dividends) declared by the Issuer. All Dividends in accordance with the ISDA 2002 Equity Derivatives Definitions.")

# Import after class definition to avoid circular imports
DividendApplicability.model_rebuild()
