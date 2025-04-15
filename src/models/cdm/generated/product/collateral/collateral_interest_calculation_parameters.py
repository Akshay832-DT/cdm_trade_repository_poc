from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_enum import BusinessCenterEnum
    from src.models.cdm.generated.base.datetime.compounding_type_enum import CompoundingTypeEnum
    from src.models.cdm.generated.base.datetime.daycount.day_count_fraction_enum import DayCountFractionEnum
    from src.models.cdm.generated.base.datetime.rounding_frequency_enum import RoundingFrequencyEnum
    from src.models.cdm.generated.base.math.rounding import Rounding
    from src.models.cdm.generated.product.collateral.collateral_agreement_floating_rate import CollateralAgreementFloatingRate

class CollateralInterestCalculationParameters(CdmModelBase):
    """Represents parameters for calculating the amount the floating interest calculation, e.g.  for a single currency or defaults for all currencies."""
    fixed_rate: float = Field(None, description="Specifies the applicable fixed rate  if used.")
    floating_rate: ForwardRef("CollateralAgreementFloatingRate") = Field(None, description="Specifies the floating interest rate to be used.")
    in_base_currency: bool = Field(description="If True, specifies that the interest transfers should be converted to base currency equivalent, or if False specifies that the transfer should be in the currency of the collateral.")
    compounding_type: ForwardRef("CompoundingTypeEnum") = Field(None, description="Specifies the type of compounding to be applied (None, Business, Calendar).")
    compounding_business_center: List[ForwardRef("BusinessCenterEnum")] = Field(None, description="Specifies the applicable business centers for compounding.")
    day_count_fraction: ForwardRef("DayCountFractionEnum") = Field(description="Specifies the day count fraction to use for that currency.")
    rounding: ForwardRef("Rounding") = Field(None, description="Specifies the rounding rules for settling in that currency.")
    rounding_frequency: ForwardRef("RoundingFrequencyEnum") = Field(None, description="Specifies when/how often is rounding applied?")
    withholding_tax_rate: float = Field(None, description="Specifies the withholding tax rate if a withholding tax is applicable.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_enum import BusinessCenterEnum
from src.models.cdm.generated.base.datetime.compounding_type_enum import CompoundingTypeEnum
from src.models.cdm.generated.base.datetime.daycount.day_count_fraction_enum import DayCountFractionEnum
from src.models.cdm.generated.base.datetime.rounding_frequency_enum import RoundingFrequencyEnum
from src.models.cdm.generated.base.math.rounding import Rounding
from src.models.cdm.generated.product.collateral.collateral_agreement_floating_rate import CollateralAgreementFloatingRate
CollateralInterestCalculationParameters.model_rebuild()
