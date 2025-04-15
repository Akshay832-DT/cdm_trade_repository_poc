from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.common.schedule.observation_terms import ObservationTerms
    from src.models.cdm.generated.product.template.averaging_calculation import AveragingCalculation

class AveragingStrikeFeature(CdmModelBase):
    """Defines the terms required to calculate the average observations associated with an averaging strike."""
    averaging_calculation: ForwardRef("AveragingCalculation") = Field(description="Defines parameters for use in cases when a valuation or other term is based on an average of market observations.")
    observation_terms: ForwardRef("ObservationTerms") = Field(description="Class containing terms that are associated with observing a price/benchmark/index across either single or multple observations. ")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.common.schedule.observation_terms import ObservationTerms
from src.models.cdm.generated.product.template.averaging_calculation import AveragingCalculation
AveragingStrikeFeature.model_rebuild()
