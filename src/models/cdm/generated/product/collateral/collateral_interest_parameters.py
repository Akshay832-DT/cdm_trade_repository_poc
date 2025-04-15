from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.calculation_frequency import CalculationFrequency
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.product.collateral.collateral_interest_calculation_parameters import CollateralInterestCalculationParameters
    from src.models.cdm.generated.product.collateral.collateral_interest_handling_parameters import CollateralInterestHandlingParameters
    from src.models.cdm.generated.product.collateral.collateral_margin_type_enum import CollateralMarginTypeEnum

class CollateralInterestParameters(CdmModelBase):
    """Represents the floating interest calculation and distribution parameters for a single currency."""
    posting_party: ForwardRef("CounterpartyRoleEnum") = Field(None, description="Represents the party to which these parameters apply (the applicable party).  In other words, if the parameters are different depending on which party is posting/holding the collateral, for which party to the Collateral Agreement (Party 1 or Party 2) that is posting the collateral do these parameters apply?")
    margin_type: ForwardRef("CollateralMarginTypeEnum") = Field(None, description="Specifies the type of margin for which interest is being calculated, if the parameters are different depending on type of margin (initial or variation).")
    currency: str = Field(None, description="Specifies the currency for which the parameters are captured.")
    interest_calculation_parameters: ForwardRef("CollateralInterestCalculationParameters") = Field(None, description="Represents the basic interest calculation parameters.")
    interest_calculation_frequency: ForwardRef("CalculationFrequency") = Field(None, description="Represents how often and when interest is calculated.")
    interest_handling_parameters: ForwardRef("CollateralInterestHandlingParameters") = Field(None, description="Represents the parameters describing how and when interest transfer occurs.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.calculation_frequency import CalculationFrequency
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.product.collateral.collateral_interest_calculation_parameters import CollateralInterestCalculationParameters
from src.models.cdm.generated.product.collateral.collateral_interest_handling_parameters import CollateralInterestHandlingParameters
from src.models.cdm.generated.product.collateral.collateral_margin_type_enum import CollateralMarginTypeEnum
CollateralInterestParameters.model_rebuild()
