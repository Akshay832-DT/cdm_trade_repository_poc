"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.assigned_identifier import AssignedIdentifier
    from src.models.cdm.generated.base.staticdata.identifier.commodity_location_identifier_type_enum import CommodityLocationIdentifierTypeEnum
    from src.models.cdm.generated.base.staticdata.identifier.identified_list import IdentifiedList
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.base.staticdata.identifier.location_identifier import LocationIdentifier
    from src.models.cdm.generated.base.staticdata.identifier.trade_identifier_type_enum import TradeIdentifierTypeEnum
