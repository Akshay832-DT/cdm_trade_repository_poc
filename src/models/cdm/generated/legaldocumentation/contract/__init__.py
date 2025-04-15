"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.contract.agreement import Agreement
    from src.models.cdm.generated.legaldocumentation.contract.broker_confirmation import BrokerConfirmation
    from src.models.cdm.generated.legaldocumentation.contract.broker_confirmation_type_enum import BrokerConfirmationTypeEnum
