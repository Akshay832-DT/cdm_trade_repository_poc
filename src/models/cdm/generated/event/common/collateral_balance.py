from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.party_reference_payer_receiver import PartyReferencePayerReceiver
    from src.models.cdm.generated.event.common.collateral_status_enum import CollateralStatusEnum
    from src.models.cdm.generated.event.common.haircut_indicator_enum import HaircutIndicatorEnum
    from src.models.cdm.generated.observable.asset.money import Money

class CollateralBalance(CdmModelBase):
    """Represents common attributes to define a collateral balance recorded by the principal as held or posted."""
    collateral_balance_status: ForwardRef("CollateralStatusEnum") = Field(None, description="Defines the collateral balance breakdown of settlement status.")
    haircut_indicator: ForwardRef("HaircutIndicatorEnum") = Field(None, description="Indicates if the collateral balance amount is based on pre or post haircut, if a haircut is associated with the collateral asset")
    amount_base_currency: ForwardRef("Money") = Field(description="Specifies the collateral balance amount in base currency determined within a collateral legal agreement, or defined for reporting purposes.")
    payer_receiver: ForwardRef("PartyReferencePayerReceiver") = Field(description="Specifies each of the parties in the collateral balance and its perspective with regards to the direction of the collateral balance, posted or received.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.party_reference_payer_receiver import PartyReferencePayerReceiver
from src.models.cdm.generated.event.common.collateral_status_enum import CollateralStatusEnum
from src.models.cdm.generated.event.common.haircut_indicator_enum import HaircutIndicatorEnum
from src.models.cdm.generated.observable.asset.money import Money
CollateralBalance.model_rebuild()
