from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
    from src.models.cdm.generated.product.common.notional_adjustment_enum import NotionalAdjustmentEnum
    from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct

class TermsChangeInstruction(CdmModelBase):
    """Specifies instructions for terms change consisting of the new transaction terms, and the renegotiation fee."""
    product: ForwardRef("NonTransferableProduct") = Field(None, description="product to be changed")
    ancillary_party: List[ForwardRef("AncillaryParty")] = Field(None, description="ancillary party to be changed")
    adjustment: ForwardRef("NotionalAdjustmentEnum") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
from src.models.cdm.generated.product.common.notional_adjustment_enum import NotionalAdjustmentEnum
from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct
TermsChangeInstruction.model_rebuild()
