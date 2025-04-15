from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.position.aggregation_parameters import AggregationParameters
    from src.models.cdm.generated.event.position.portfolio_state import PortfolioState

class Portfolio(CdmModelBase):
    """ A Portfolio represents an aggregation of multiple Positions, by describing the parameters that this Portfolio should be aggregated based on. The resulting PortfolioState is calculated using these aggregation parameters as inputs, by aggregating all the Events that are relevant to this Portfolio. The concept of Portfolio works at all levels in the model: from the highest for a given LegalEntity for instance, to the lowest to account for security substitutions in a secutity financing transaction. As such, Portfolio can be used either above or below the Contract level."""
    aggregation_parameters: ForwardRef("AggregationParameters") = Field(description="Describes the portfolio by describing how to aggregate all its relevant Events.")
    portfolio_state: ForwardRef("PortfolioState") = Field(description="Describes the state of the Portfolio as a list of Positions resulting from the aggregation.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.position.aggregation_parameters import AggregationParameters
from src.models.cdm.generated.event.position.portfolio_state import PortfolioState
Portfolio.model_rebuild()
