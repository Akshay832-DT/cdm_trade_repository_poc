from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.product.asset.reference_pool import ReferencePool
    from src.models.cdm.generated.product.asset.tranche import Tranche

class BasketReferenceInformation(CdmModelBase):
    """CDS Basket Reference Information."""
    basket_name: ForwardRef("FieldWithMetaString") = Field(None, description="The name of the basket expressed as a free format string. FpML does not define usage rules for this element.")
    basket_id: List[ForwardRef("FieldWithMetaString")] = Field(None, description="A CDS basket identifier.")
    reference_pool: ForwardRef("ReferencePool") = Field(description="This element contains all the reference pool items to define the reference entity and reference obligation(s) in the basket.")
    nth_to_default: int = Field(None, description="N th reference obligation to default triggers payout.")
    mth_to_default: int = Field(None, description="M th reference obligation to default to allow representation of N th to M th defaults.")
    tranche: ForwardRef("Tranche") = Field(None, description="This element contains CDS tranche terms.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.product.asset.reference_pool import ReferencePool
from src.models.cdm.generated.product.asset.tranche import Tranche
BasketReferenceInformation.model_rebuild()
