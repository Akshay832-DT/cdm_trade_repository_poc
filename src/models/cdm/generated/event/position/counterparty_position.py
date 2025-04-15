from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.event.common.position_identifier import PositionIdentifier
    from src.models.cdm.generated.metafields.reference_with_meta_collateral import ReferenceWithMetaCollateral
    from src.models.cdm.generated.metafields.reference_with_meta_contract_details import ReferenceWithMetaContractDetails
    from src.models.cdm.generated.metafields.reference_with_meta_execution_details import ReferenceWithMetaExecutionDetails
    from src.models.cdm.generated.metafields.reference_with_meta_trade_state import ReferenceWithMetaTradeState
    from src.models.cdm.generated.product.template.tradable_product import TradableProduct

class CounterpartyPosition(CdmModelBase):
    """A Position describes the accumulated effect of a set of securities or financial transactions."""
    contract_details: ForwardRef("ReferenceWithMetaContractDetails") = Field(None, description="Represents information specific to trades or positions involving contractual products.")
    execution_details: ForwardRef("ReferenceWithMetaExecutionDetails") = Field(None, description="Defines specific attributes that relate to trade or position executions.")
    collateral: ForwardRef("ReferenceWithMetaCollateral") = Field(None, description="Represents the collateral obligations of a party.")
    position_identifier: List[ForwardRef("PositionIdentifier")] = Field(None, description="Represents the identifier(s) that uniquely identify a position for an identity issuer. A position can include multiple identifiers, for example an internal position identifer and a UTI (Unique Trade Identifier).")
    open_date_time: str = Field(None, description="The date and time when the position was opened.")
    trade_reference: List[ForwardRef("ReferenceWithMetaTradeState")] = Field(None, description="Reference to all the trades that constitute the position.")
    party: List[ForwardRef("Party")] = Field(None, description="The parties involved in the position, including the Clearing Organization.")
    party_role: List[ForwardRef("PartyRole")] = Field(None, description="Represents the role each specified party takes in the position.")
    position_base: ForwardRef("TradableProduct") = Field(description="Encapsulates the core constituents that characterize a position.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.event.common.position_identifier import PositionIdentifier
from src.models.cdm.generated.metafields.reference_with_meta_collateral import ReferenceWithMetaCollateral
from src.models.cdm.generated.metafields.reference_with_meta_contract_details import ReferenceWithMetaContractDetails
from src.models.cdm.generated.metafields.reference_with_meta_execution_details import ReferenceWithMetaExecutionDetails
from src.models.cdm.generated.metafields.reference_with_meta_trade_state import ReferenceWithMetaTradeState
from src.models.cdm.generated.product.template.tradable_product import TradableProduct
CounterpartyPosition.model_rebuild()
