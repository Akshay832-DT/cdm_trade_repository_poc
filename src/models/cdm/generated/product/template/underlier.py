from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_observable import ReferenceWithMetaObservable
    from .product import Product

class Underlier(CdmModelBase):
    """The underlying financial product that will be physically or cash settled, which can be of any type, eg an asset such as cash or a security, a product, or the cash settlement of an index rate.  Conditions are usually applied when used in a data type, such as a payout, to ensure this aligns with the use case."""
    observable: Optional[Dict[str, Any]] = Field(None, description="Specifies the object to be observed for a price, it could be an asset or a reference.")
    product: Optional[Dict[str, Any]] = Field(None, description="Enables either a TransferableProduct or a NonTransferableProduct to be used in an underlier.")

    @model_validator(mode='after')
    def validate_types(self) -> 'Underlier':
        """Validate that the types of the attributes are correct."""
        try:
            if self.observable is not None:
                if isinstance(self.observable, dict):
                    self.observable = ReferenceWithMetaObservable(**self.observable)
                elif not isinstance(self.observable, ReferenceWithMetaObservable):
                    raise ValueError("observable must be a valid ReferenceWithMetaObservable object or dictionary")
            
            if self.product is not None:
                from .product import Product
                if isinstance(self.product, dict):
                    self.product = Product(**self.product)
                elif not isinstance(self.product, Product):
                    raise ValueError("product must be a valid Product object or dictionary")
        except Exception as e:
            raise ValueError(f"Failed to validate Underlier: {str(e)}")
        return self

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_observable import ReferenceWithMetaObservable
from .product import Product
Underlier.model_rebuild()
