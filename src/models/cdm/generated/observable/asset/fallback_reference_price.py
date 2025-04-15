from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_settlement_rate_option_enum import FieldWithMetaSettlementRateOptionEnum
    from src.models.cdm.generated.observable.asset.calculation_agent import CalculationAgent
    from src.models.cdm.generated.observable.asset.valuation_postponement import ValuationPostponement

class FallbackReferencePrice(CdmModelBase):
    """The method, prioritised by the order it is listed in this element, to get a replacement rate for the disrupted settlement rate option."""
    valuation_postponement: ForwardRef("ValuationPostponement") = Field(None, description="Specifies how long to wait to get a quote from a settlement rate option upon a price source disruption.")
    fall_back_settlement_rate_option: List[ForwardRef("FieldWithMetaSettlementRateOptionEnum")] = Field(None, description="This settlement rate option will be used in its place.")
    fallback_survey_valuation_postponement: bool = Field(None, description="Request rate quotes from the market. This element is set as type Empty in FpML. When present, the FpML synonym is mapped to a value True in the CDM.")
    calculation_agent_determination: ForwardRef("CalculationAgent") = Field(None, description="The calculation agent will decide the rate.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_settlement_rate_option_enum import FieldWithMetaSettlementRateOptionEnum
from src.models.cdm.generated.observable.asset.calculation_agent import CalculationAgent
from src.models.cdm.generated.observable.asset.valuation_postponement import ValuationPostponement
FallbackReferencePrice.model_rebuild()
