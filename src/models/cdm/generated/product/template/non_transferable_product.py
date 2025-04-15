from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.product_identifier import ProductIdentifier
    from src.models.cdm.generated.base.staticdata.asset.common.product_taxonomy import ProductTaxonomy
    from src.models.cdm.generated.product.template.economic_terms import EconomicTerms

class NonTransferableProduct(CdmModelBase):
    """A data type to specify the financial product's economic terms, alongside the product identification and product taxonomy. The non-transferable product data type represents a product that can be traded (as part of a TradableProduct) but cannot be transferred to others.  It is meant to be used across the pre-execution, execution and (as part of the Contract) post-execution lifecycle contexts."""
    identifier: Optional[List[ForwardRef("ProductIdentifier")]] = Field(None, description="Comprises a identifier and a source to uniquely identify the nonTransferableProduct. ")
    taxonomy: Optional[List[ForwardRef("ProductTaxonomy")]] = Field(None, description="Specifies the product taxonomy, which is composed of a taxonomy value and a taxonomy source.")
    economic_terms: Optional[ForwardRef("EconomicTerms")] = Field(None, description="The price forming features, including payouts and provisions.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.product_identifier import ProductIdentifier
from src.models.cdm.generated.base.staticdata.asset.common.product_taxonomy import ProductTaxonomy
from src.models.cdm.generated.product.template.economic_terms import EconomicTerms
NonTransferableProduct.model_rebuild()
