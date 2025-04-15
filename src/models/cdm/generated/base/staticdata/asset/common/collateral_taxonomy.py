from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.collateral_taxonomy_value import CollateralTaxonomyValue
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_source_enum import TaxonomySourceEnum

class CollateralTaxonomy(CdmModelBase):
    """Specifies the collateral taxonomy, which is composed of a taxonomy value and a taxonomy source."""
    taxonomy_value: ForwardRef("CollateralTaxonomyValue") = Field(description="Specifies the taxonomy value.")
    taxonomy_source: ForwardRef("TaxonomySourceEnum") = Field(description="Specifies the taxonomy source.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.collateral_taxonomy_value import CollateralTaxonomyValue
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_source_enum import TaxonomySourceEnum
CollateralTaxonomy.model_rebuild()
