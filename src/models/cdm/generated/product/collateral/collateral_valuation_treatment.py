from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CollateralValuationTreatment(CdmModelBase):
    """Specification of the valuation treatment for the specified collateral."""
    haircut_percentage: float = Field(None, description="Specifies a haircut percentage to be applied to the value of asset and used as a discount factor to the value of the collateral asset,expressed as a percentage in decimal terms. As an example a 0.5% haircut would be represented as a decimal number 0.005.")
    margin_percentage: float = Field(None, description="Specifies a percentage value of transaction needing to be posted as collateral expressed as a valuation. As an example a 104% requirement would be represented as a decimal number 1.04.")
    fx_haircut_percentage: float = Field(None, description="Specifies an FX haircut applied to a specific asset which is agreed between the parties (for example, if pledgor eligible collateral is not denominated in the termination currency or under other specified cases in collateral support documents both for initial margin and variation margin).The percentage value is expressed as the discount haircut to the value of the collateral- as an example an 8% FX haircut would be expressed as 0.08.")
    additional_haircut_percentage: float = Field(None, description="Specifies a percentage value of any additional haircut to be applied to a collateral asset,the percentage value is expressed as the discount haircut to the value of the collateral- as an example a 5% haircut would be expressed as 0.05. ")

# Import after class definition to avoid circular imports
CollateralValuationTreatment.model_rebuild()
