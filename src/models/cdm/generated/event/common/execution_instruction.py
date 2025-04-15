from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
    from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.event.common.execution_details import ExecutionDetails
    from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.metafields.field_with_meta_time_zone import FieldWithMetaTimeZone
    from src.models.cdm.generated.observable.asset.price_quantity import PriceQuantity
    from src.models.cdm.generated.product.collateral.collateral import Collateral
    from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct

class ExecutionInstruction(CdmModelBase):
    """Specifies instructions for execution of a transaction, consisting of a product, price, quantity, parties, trade identifier, execution details, and settlement terms."""
    product: ForwardRef("NonTransferableProduct") = Field(description="Defines the financial product to be executed and contract formed.")
    price_quantity: List[ForwardRef("PriceQuantity")] = Field(None, description="Defines the prices (e.g. spread, equity price, FX rate), quantities (e.g. currency amount, no. shares) and settlement terms (e.g. initial fee, broker fee, up-front cds payment or option premium settlement) associated with the constituents of the transacted product.")
    counterparty: List[ForwardRef("Counterparty")] = Field(None, description="Maps two defined parties to counterparty enums for the transacted product.")
    ancillary_party: List[ForwardRef("AncillaryParty")] = Field(None, description="Maps any ancillary parties, e.g. parties involved in the transaction that are not one of the two principal parties.")
    parties: List[ForwardRef("Party")] = Field(None, description="Defines all parties to that execution, including agents and brokers.")
    party_roles: List[ForwardRef("PartyRole")] = Field(None, description="Defines the role(s) that party(ies) may have in relation to the execution.")
    execution_details: ForwardRef("ExecutionDetails") = Field(description="Specifies the type and venue of execution, e.g. via voice, or electronically.")
    trade_date: ForwardRef("FieldWithMetaString") = Field(description="Denotes the trade/execution date.")
    trade_time: ForwardRef("FieldWithMetaTimeZone") = Field(None, description="Denotes the trade time and timezone as agreed by the parties to the trade.")
    trade_identifier: List[ForwardRef("TradeIdentifier")] = Field(None, description="Denotes one or more identifiers associated with the transaction.")
    collateral: ForwardRef("Collateral") = Field(None, description="Detail the collateral requirement anticipated with the transaction.")
    lot_identifier: ForwardRef("Identifier") = Field(None, description="Lot Identifier associated with the transaction.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.event.common.execution_details import ExecutionDetails
from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.metafields.field_with_meta_time_zone import FieldWithMetaTimeZone
from src.models.cdm.generated.observable.asset.price_quantity import PriceQuantity
from src.models.cdm.generated.product.collateral.collateral import Collateral
from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct
ExecutionInstruction.model_rebuild()
