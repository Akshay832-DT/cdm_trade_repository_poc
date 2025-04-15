from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_source_enum import TaxonomySourceEnum
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_value import TaxonomyValue
    from src.models.cdm.generated.metafields.field_with_meta_asset_class_enum import FieldWithMetaAssetClassEnum

class ProductTaxonomy(CdmModelBase):
    """Specifies the product taxonomy, which is composed of a taxonomy value and a taxonomy source."""
    source: ForwardRef("TaxonomySourceEnum") = Field(None, description="The source of the taxonomy that defines the rules for classifying the object. The taxonomy source is taken from a enumerated list of taxonomy names. Optional as the taxonomy source may not be provided.")
    value: ForwardRef("TaxonomyValue") = Field(None, description="The value according to that taxonomy. Optional as it may not be possible to classify the object in that taxonomy.")
    primary_asset_class: ForwardRef("FieldWithMetaAssetClassEnum") = Field(None, description="Classifies the most important risk class of the trade.")
    secondary_asset_class: List[ForwardRef("FieldWithMetaAssetClassEnum")] = Field(None, description=" Classifies additional risk classes of the trade, if any.")
    product_qualifier: str = Field(None, description="Derived from the product payout features using a CDM product qualification function that determines the product type based on the product payout features.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_source_enum import TaxonomySourceEnum
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_value import TaxonomyValue
from src.models.cdm.generated.metafields.field_with_meta_asset_class_enum import FieldWithMetaAssetClassEnum
ProductTaxonomy.model_rebuild()
