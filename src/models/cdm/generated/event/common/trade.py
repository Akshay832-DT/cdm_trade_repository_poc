from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.account import Account
    from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
    from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.event.common.contract_details import ContractDetails
    from src.models.cdm.generated.event.common.execution_details import ExecutionDetails
    from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.metafields.field_with_meta_time_zone import FieldWithMetaTimeZone
    from src.models.cdm.generated.product.collateral.collateral import Collateral
    from src.models.cdm.generated.product.common.notional_adjustment_enum import NotionalAdjustmentEnum
    from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct
    from src.models.cdm.generated.product.template.trade_lot import TradeLot

class Trade(CdmModelBase):
    """Defines the output of a financial transaction between parties - a Business Event. A Trade impacts the financial position (i.e. the balance sheet) of involved parties."""
    product: ForwardRef("NonTransferableProduct") = Field(None, description="The underlying product to be included in a contract or execution.")
    trade_lot: List[ForwardRef("TradeLot")] = Field(None, description="Specifies the price, quantity and effective date of each trade lot, when the same product may be traded multiple times in different lots with the same counterparty. In a trade increase, a new trade lot is added to the list, with the corresponding effective date. In a trade decrease, the existing trade lot(s) are decreased of the corresponding quantity (and an unwind fee may have to be settled). The multiple cardinality and the ability to increase existing trades is used for Equity Swaps in particular.")
    counterparty: List[ForwardRef("Counterparty")] = Field(None, description="Specifies the parties which are the two counterparties to the transaction.  The product is agnostic to the actual parties to the transaction, with the party references abstracted away from the product definition and replaced by the counterparty enum (e.g. CounterpartyEnum values Party1 or Party2). The counterparty enum can then be positioned in the product (e.g. to specify which counterparty is the payer, receiver etc) and this counterparties attribute, which is positioned outside of the product definition, allows the counterparty enum to be associated with an actual party reference.")
    ancillary_party: List[ForwardRef("AncillaryParty")] = Field(None, description="Specifies the parties with ancillary roles in the transaction. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and this AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference.")
    adjustment: ForwardRef("NotionalAdjustmentEnum") = Field(None, description="Specifies the conditions that govern the adjustment to the quantity of a product being traded: e.g. execution, portfolio rebalancing etc. It is typically used in the context of Equity Swaps.")
    trade_identifier: List[ForwardRef("TradeIdentifier")] = Field(None, description="Represents the identifier(s) that uniquely identify a trade for an identity issuer. A trade can include multiple identifiers, for example a trade that is reportable to both the CFTC and ESMA, and then has an associated USI (Unique Swap Identifier) UTI (Unique Trade Identifier).")
    trade_date: ForwardRef("FieldWithMetaString") = Field(description="Specifies the date which the trade was agreed.")
    trade_time: ForwardRef("FieldWithMetaTimeZone") = Field(None, description="Denotes the trade time and timezone as agreed by the parties to the trade.")
    party: List[ForwardRef("Party")] = Field(None, description="Represents the parties to the trade. The cardinality is optional to address the case where the trade is defined within a BusinessEvent data type, in which case the party is specified in BusinessEvent.")
    party_role: List[ForwardRef("PartyRole")] = Field(None, description="Represents the role each specified party takes in the trade. further to the principal roles, payer and receiver.")
    execution_details: ForwardRef("ExecutionDetails") = Field(None, description="Represents information specific to trades that arose from executions.")
    contract_details: ForwardRef("ContractDetails") = Field(None, description="Represents information specific to trades involving contractual products.")
    cleared_date: str = Field(None, description="Specifies the date on which a trade is cleared (novated) through a central counterparty clearing service.")
    collateral: ForwardRef("Collateral") = Field(None, description="Represents the collateral obligations of a party.")
    account: List[ForwardRef("Account")] = Field(None, description="Represents a party's granular account information, which may be used in subsequent internal processing.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.account import Account
from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.event.common.contract_details import ContractDetails
from src.models.cdm.generated.event.common.execution_details import ExecutionDetails
from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.metafields.field_with_meta_time_zone import FieldWithMetaTimeZone
from src.models.cdm.generated.product.collateral.collateral import Collateral
from src.models.cdm.generated.product.common.notional_adjustment_enum import NotionalAdjustmentEnum
from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct
from src.models.cdm.generated.product.template.trade_lot import TradeLot
Trade.model_rebuild()
