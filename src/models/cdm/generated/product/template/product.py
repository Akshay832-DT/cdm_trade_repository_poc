from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from .transferable_product import TransferableProduct
    from .non_transferable_product import NonTransferableProduct

# Forward references for types to avoid circular imports
TransferableProduct = ForwardRef('TransferableProduct')
NonTransferableProduct = ForwardRef('NonTransferableProduct')

class Product(CdmModelBase):
    """A class to represent a product that can be either transferable or non-transferable."""
    
    transferable_product: Optional[Any] = Field(None, alias="transferableProduct", description="A transferable product.")
    non_transferable_product: Optional[Any] = Field(None, alias="nonTransferableProduct", description="A non-transferable product.")
    
    @model_validator(mode='after')
    def validate_types(self) -> 'Product':
        """Validate that the types of the attributes are correct."""
        try:
            from .transferable_product import TransferableProduct
            from .non_transferable_product import NonTransferableProduct
            
            if self.transferable_product is not None:
                if isinstance(self.transferable_product, dict):
                    self.transferable_product = TransferableProduct(**self.transferable_product)
                elif not isinstance(self.transferable_product, TransferableProduct):
                    raise ValueError("transferable_product must be a valid TransferableProduct object or dictionary")
            
            if self.non_transferable_product is not None:
                if isinstance(self.non_transferable_product, dict):
                    self.non_transferable_product = NonTransferableProduct(**self.non_transferable_product)
                elif not isinstance(self.non_transferable_product, NonTransferableProduct):
                    raise ValueError("non_transferable_product must be a valid NonTransferableProduct object or dictionary")
        except Exception as e:
            raise ValueError(f"Error validating Product: {str(e)}")
        return self

Product.model_rebuild()
