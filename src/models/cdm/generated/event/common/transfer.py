from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_or_relative_date import AdjustableOrAdjustedOrRelativeDate
    from src.models.cdm.generated.base.math.non_negative_quantity import NonNegativeQuantity
    from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
    from src.models.cdm.generated.base.staticdata.party.party_reference_payer_receiver import PartyReferencePayerReceiver
    from src.models.cdm.generated.event.common.reset import Reset
    from src.models.cdm.generated.event.common.transfer_expression import TransferExpression
    from src.models.cdm.generated.metafields.field_with_meta_identifier import FieldWithMetaIdentifier
    from src.models.cdm.generated.metafields.reference_with_meta_payout import ReferenceWithMetaPayout

class Transfer(CdmModelBase):
    """Defines the movement of an Asset (eg cash, securities or commodities) between two parties on a date."""
    quantity: ForwardRef("NonNegativeQuantity") = Field(None, description="Represents the amount of the asset to be transferred. The cashflow amount is always a positive number, as the cashflow direction is implied by the payer/receiver attribute.")
    asset: ForwardRef("Asset") = Field(None, description="Represents the object that is subject to the transfer, it could be an asset or a reference.")
    settlement_date: ForwardRef("AdjustableOrAdjustedOrRelativeDate") = Field(None, description="Represents the date on which the transfer to due.")
    identifier: List[ForwardRef("FieldWithMetaIdentifier")] = Field(None, description="Represents a unique reference to the transfer.")
    payer_receiver: ForwardRef("PartyReferencePayerReceiver") = Field(description="Represents the parties to the transfer and their role.")
    settlement_origin: ForwardRef("ReferenceWithMetaPayout") = Field(None, description="Represents the origin to the transfer as a reference for lineage purposes, whether it originated from trade level settlement terms or from payment terms on an economic payout.")
    reset_origin: ForwardRef("Reset") = Field(None, description="Represents the reset and observation values that were used to determine the transfer amount.")
    transfer_expression: ForwardRef("TransferExpression") = Field(description="Specifies a transfer expression (cash price, performance amount, scheduled payment amount, etc.) to define the nature of the transfer amount and its source.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_or_relative_date import AdjustableOrAdjustedOrRelativeDate
from src.models.cdm.generated.base.math.non_negative_quantity import NonNegativeQuantity
from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
from src.models.cdm.generated.base.staticdata.party.party_reference_payer_receiver import PartyReferencePayerReceiver
from src.models.cdm.generated.event.common.reset import Reset
from src.models.cdm.generated.event.common.transfer_expression import TransferExpression
from src.models.cdm.generated.metafields.field_with_meta_identifier import FieldWithMetaIdentifier
from src.models.cdm.generated.metafields.reference_with_meta_payout import ReferenceWithMetaPayout
Transfer.model_rebuild()
