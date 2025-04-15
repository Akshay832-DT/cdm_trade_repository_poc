from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_or_relative_date import AdjustableOrAdjustedOrRelativeDate
    from src.models.cdm.generated.base.math.non_negative_quantity import NonNegativeQuantity
    from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.product.common.settlement.cashflow_type import CashflowType
    from src.models.cdm.generated.product.common.settlement.payment_discounting import PaymentDiscounting

class Cashflow(CdmModelBase):
    """Class to specify a cashflow, i.e. the outcome of either of computation (e.g. interest accrual) or an assessment of some sort (e.g. a fee). The cashflow can then be turned into a cash transfer, artefact to be used as the input to a payment system or the outcome of it. The associated globalKey denotes the ability to associate a hash value to the Cashflow instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage."""
    quantity: ForwardRef("NonNegativeQuantity") = Field(None, description="Represents the amount of the asset to be transferred. The cashflow amount is always a positive number, as the cashflow direction is implied by the payer/receiver attribute.")
    asset: ForwardRef("Asset") = Field(None, description="Represents the object that is subject to the transfer, it could be an asset or a reference.")
    settlement_date: ForwardRef("AdjustableOrAdjustedOrRelativeDate") = Field(None, description="Represents the date on which the transfer to due.")
    payer_receiver: ForwardRef("PayerReceiver") = Field(description="Specifies who pays / receives the cashflow, though a normalised Party1 / Party2 enumerator.")
    cashflow_type: ForwardRef("CashflowType") = Field(description="The qualification of the type of cashflow, e.g. brokerage fee, premium, upfront fee etc. Particularly relevant when it cannot be inferred directly through lineage.")
    payment_discounting: ForwardRef("PaymentDiscounting") = Field(None, description="FpML specifies the FpML PaymentDiscounting.model group for representing the discounting elements that can be associated with a payment.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_or_relative_date import AdjustableOrAdjustedOrRelativeDate
from src.models.cdm.generated.base.math.non_negative_quantity import NonNegativeQuantity
from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.product.common.settlement.cashflow_type import CashflowType
from src.models.cdm.generated.product.common.settlement.payment_discounting import PaymentDiscounting
Cashflow.model_rebuild()
