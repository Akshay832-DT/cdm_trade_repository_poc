from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_portfolio_state import ReferenceWithMetaPortfolioState
    from src.models.cdm.generated.observable.asset.money import Money

class Exposure(CdmModelBase):
    """Represents the current mark to market value or IM calculation value of the trade portfolio as recorded by the principle (in base currency)."""
    trade_portfolio: ForwardRef("ReferenceWithMetaPortfolioState") = Field(description="Represents a Portfolio that describes all the positions held at a given time, in various states which can be either traded, settled, etc., with lineage information to the previous state.")
    aggregate_value: ForwardRef("Money") = Field(description="Represents the aggregate value of the portfolio in base currency.")
    calculation_date_time: str = Field(None, description="Indicates the date when the exposure is calculated if different from valuation date.")
    valuation_date_time: str = Field(description="Indicates the valuation date of the exposure underlying the calculation.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_portfolio_state import ReferenceWithMetaPortfolioState
from src.models.cdm.generated.observable.asset.money import Money
Exposure.model_rebuild()
