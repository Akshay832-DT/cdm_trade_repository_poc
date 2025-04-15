from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.return_type_enum import ReturnTypeEnum

class PriceReturnTerms(CdmModelBase):
    """"""
    return_type: ForwardRef("ReturnTypeEnum") = Field(description="The type of return associated with the equity swap.")
    conversion_factor: float = Field(None, description="Defines the conversion applied if the quantity unit on contract is different from unit on referenced underlier.")
    performance: str = Field(None, description="Performance calculation, in accordance with Part 1 Section 12 of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap, Para 75. 'Equity Performance'. Cumulative performance is used as a notional multiplier factor on both legs of an Equity Swap.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.asset.return_type_enum import ReturnTypeEnum
PriceReturnTerms.model_rebuild()
