"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.floatingrate.floating_amount_calculation_details import FloatingAmountCalculationDetails
    from src.models.cdm.generated.product.asset.floatingrate.floating_rate_index_processing_type_enum import FloatingRateIndexProcessingTypeEnum
    from src.models.cdm.generated.product.asset.floatingrate.floating_rate_processing_details import FloatingRateProcessingDetails
    from src.models.cdm.generated.product.asset.floatingrate.floating_rate_processing_parameters import FloatingRateProcessingParameters
    from src.models.cdm.generated.product.asset.floatingrate.floating_rate_setting_details import FloatingRateSettingDetails
