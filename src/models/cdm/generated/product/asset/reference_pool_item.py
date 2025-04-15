from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_cash_settlement_terms import ReferenceWithMetaCashSettlementTerms
    from src.models.cdm.generated.metafields.reference_with_meta_physical_settlement_terms import ReferenceWithMetaPhysicalSettlementTerms
    from src.models.cdm.generated.metafields.reference_with_meta_protection_terms import ReferenceWithMetaProtectionTerms
    from src.models.cdm.generated.product.asset.reference_pair import ReferencePair
    from src.models.cdm.generated.product.template.constituent_weight import ConstituentWeight

class ReferencePoolItem(CdmModelBase):
    """This type contains all the constituent weight and reference information."""
    constituent_weight: ForwardRef("ConstituentWeight") = Field(None, description="Describes the weight of each of the constituents within the basket. If not provided, it is assumed to be equal weighted.")
    reference_pair: ForwardRef("ReferencePair") = Field()
    protection_terms_reference: ForwardRef("ReferenceWithMetaProtectionTerms") = Field(None, description="Reference to the documentation terms applicable to this item.")
    cash_settlement_terms_reference: ForwardRef("ReferenceWithMetaCashSettlementTerms") = Field(None, description="Reference to the cash settlement terms applicable to this item.")
    physical_settlement_terms_reference: ForwardRef("ReferenceWithMetaPhysicalSettlementTerms") = Field(None, description="Reference to the physical settlement terms applicable to this item.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_cash_settlement_terms import ReferenceWithMetaCashSettlementTerms
from src.models.cdm.generated.metafields.reference_with_meta_physical_settlement_terms import ReferenceWithMetaPhysicalSettlementTerms
from src.models.cdm.generated.metafields.reference_with_meta_protection_terms import ReferenceWithMetaProtectionTerms
from src.models.cdm.generated.product.asset.reference_pair import ReferencePair
from src.models.cdm.generated.product.template.constituent_weight import ConstituentWeight
ReferencePoolItem.model_rebuild()
