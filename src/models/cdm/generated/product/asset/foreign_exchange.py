from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period
    from src.models.cdm.generated.product.common.settlement.cashflow import Cashflow

class ForeignExchange(CdmModelBase):
    """From FpML: A type defining either a spot or forward FX transactions."""
    exchanged_currency1: ForwardRef("Cashflow") = Field(description="This is the first of the two currency flows that define a single leg of a standard foreign exchange transaction.")
    exchanged_currency2: ForwardRef("Cashflow") = Field(description="This is the second of the two currency flows that define a single leg of a standard foreign exchange transaction.")
    tenor_period: ForwardRef("Period") = Field(None, description="A tenor expressed as a period type and multiplier (e.g. 1D, 1Y, etc.)")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
from src.models.cdm.generated.product.common.settlement.cashflow import Cashflow
ForeignExchange.model_rebuild()
