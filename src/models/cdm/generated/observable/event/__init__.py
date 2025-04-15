"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.event.credit_event_notice import CreditEventNotice
    from src.models.cdm.generated.observable.event.credit_events import CreditEvents
    from src.models.cdm.generated.observable.event.determination_methodology import DeterminationMethodology
    from src.models.cdm.generated.observable.event.failure_to_pay import FailureToPay
    from src.models.cdm.generated.observable.event.feature_payment import FeaturePayment
    from src.models.cdm.generated.observable.event.grace_period_extension import GracePeriodExtension
    from src.models.cdm.generated.observable.event.index_event_consequence_enum import IndexEventConsequenceEnum
    from src.models.cdm.generated.observable.event.market_disruption_enum import MarketDisruptionEnum
    from src.models.cdm.generated.observable.event.observation import Observation
    from src.models.cdm.generated.observable.event.observation_identifier import ObservationIdentifier
    from src.models.cdm.generated.observable.event.publicly_available_information import PubliclyAvailableInformation
    from src.models.cdm.generated.observable.event.restructuring import Restructuring
    from src.models.cdm.generated.observable.event.restructuring_enum import RestructuringEnum
    from src.models.cdm.generated.observable.event.share_extraordinary_event_enum import ShareExtraordinaryEventEnum
    from src.models.cdm.generated.observable.event.trigger import Trigger
    from src.models.cdm.generated.observable.event.trigger_event import TriggerEvent
    from src.models.cdm.generated.observable.event.trigger_time_type_enum import TriggerTimeTypeEnum
    from src.models.cdm.generated.observable.event.trigger_type_enum import TriggerTypeEnum
