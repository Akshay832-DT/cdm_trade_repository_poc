from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.collateral_valuation_treatment import CollateralValuationTreatment
    from src.models.cdm.generated.product.collateral.concentration_limit import ConcentrationLimit

class CollateralTreatment(CdmModelBase):
    """Specifies the treatment terms for the eligible collateral criteria specified."""
    valuation_treatment: ForwardRef("CollateralValuationTreatment") = Field(None, description="Specification of the valuation treatment for the specified collateral.")
    concentration_limit: List[ForwardRef("ConcentrationLimit")] = Field(None, description="Specification of concentration limits applicable to the collateral criteria.")
    is_included: bool = Field(description="A boolean attribute to specify whether collateral critieria are inclusion (True) or exclusion (False) criteria.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.collateral_valuation_treatment import CollateralValuationTreatment
from src.models.cdm.generated.product.collateral.concentration_limit import ConcentrationLimit
CollateralTreatment.model_rebuild()
