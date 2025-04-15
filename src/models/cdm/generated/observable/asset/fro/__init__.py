"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.fro.business_day_offset import BusinessDayOffset
    from src.models.cdm.generated.observable.asset.fro.contractual_definition import ContractualDefinition
    from src.models.cdm.generated.observable.asset.fro.contractual_definition_identifier import ContractualDefinitionIdentifier
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_calculation_defaults import FloatingRateIndexCalculationDefaults
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_calculation_method_enum import FloatingRateIndexCalculationMethodEnum
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_category_enum import FloatingRateIndexCategoryEnum
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_definition import FloatingRateIndexDefinition
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_external_map import FloatingRateIndexExternalMap
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_external_mappings import FloatingRateIndexExternalMappings
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_fixing_details import FloatingRateIndexFixingDetails
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_fixing_offset import FloatingRateIndexFixingOffset
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_fixing_time import FloatingRateIndexFixingTime
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_identification import FloatingRateIndexIdentification
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_map import FloatingRateIndexMap
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_mappings import FloatingRateIndexMappings
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_style_enum import FloatingRateIndexStyleEnum
    from src.models.cdm.generated.observable.asset.fro.fro_history import FroHistory
