from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.fro.contractual_definition import ContractualDefinition
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_calculation_defaults import FloatingRateIndexCalculationDefaults
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_external_mappings import FloatingRateIndexExternalMappings
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_identification import FloatingRateIndexIdentification
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_mappings import FloatingRateIndexMappings
    from src.models.cdm.generated.observable.asset.fro.fro_history import FroHistory

class FloatingRateIndexDefinition(CdmModelBase):
    """"""
    fro: ForwardRef("FloatingRateIndexIdentification") = Field(description="The underlying FRO name and designated maturity.")
    calculation_defaults: ForwardRef("FloatingRateIndexCalculationDefaults") = Field(None, description="Any calculation default values.")
    supported_definition: List[ForwardRef("ContractualDefinition")] = Field(None, description="The definition version or versions supported by the FRO.")
    definitional_source: str = Field(None, description="The source of an FRO, particularly if not a Contractual Definition (e.g. the broker rates matrix).")
    designated_maturity_applicable: bool = Field(None)
    mappings: ForwardRef("FloatingRateIndexMappings") = Field(None, description="Any mappings to other FRos.")
    external_mappings: ForwardRef("FloatingRateIndexExternalMappings") = Field(None, description="Any mappings to other codes for this index.")
    in_loan: bool = Field(None, description="YES / NO to flag FROs identified by the FpML Syndicated Loan WG as having underlying benchmark that may also be referenced in syndicated loans.")
    history: ForwardRef("FroHistory") = Field(None, description="FRO History")
    deprecation_reason: str = Field(None, description="Deprecation and Code Descriptions")
    fpml_description: str = Field(None, description="FpML Description")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.fro.contractual_definition import ContractualDefinition
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_calculation_defaults import FloatingRateIndexCalculationDefaults
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_external_mappings import FloatingRateIndexExternalMappings
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_identification import FloatingRateIndexIdentification
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_mappings import FloatingRateIndexMappings
from src.models.cdm.generated.observable.asset.fro.fro_history import FroHistory
FloatingRateIndexDefinition.model_rebuild()
