from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.delivery_amount import DeliveryAmount
    from src.models.cdm.generated.product.collateral.return_amount import ReturnAmount

class InterestAmountApplication(CdmModelBase):
    """A class to specify the application of Interest Amount with respect to the Delivery Amount and the Return Amount."""
    return_amount: ForwardRef("ReturnAmount") = Field(description="The application of Interest Amount with respect the Return Amount.")
    delivery_amount: ForwardRef("DeliveryAmount") = Field(description="The application of Interest Amount with respect the Delivery Amount.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.delivery_amount import DeliveryAmount
from src.models.cdm.generated.product.collateral.return_amount import ReturnAmount
InterestAmountApplication.model_rebuild()
