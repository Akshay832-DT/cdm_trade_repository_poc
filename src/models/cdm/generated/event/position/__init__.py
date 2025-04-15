"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.event.position.aggregation_parameters import AggregationParameters
    from src.models.cdm.generated.event.position.available_inventory import AvailableInventory
    from src.models.cdm.generated.event.position.available_inventory_record import AvailableInventoryRecord
    from src.models.cdm.generated.event.position.available_inventory_type_enum import AvailableInventoryTypeEnum
    from src.models.cdm.generated.event.position.contract_base import ContractBase
    from src.models.cdm.generated.event.position.counterparty_position import CounterpartyPosition
    from src.models.cdm.generated.event.position.inventory import Inventory
    from src.models.cdm.generated.event.position.inventory_record import InventoryRecord
    from src.models.cdm.generated.event.position.portfolio import Portfolio
    from src.models.cdm.generated.event.position.portfolio_state import PortfolioState
    from src.models.cdm.generated.event.position.position import Position
    from src.models.cdm.generated.event.position.position_status_enum import PositionStatusEnum
    from src.models.cdm.generated.event.position.security_locate import SecurityLocate
