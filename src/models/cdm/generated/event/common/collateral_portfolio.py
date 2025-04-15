from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.event.common.collateral_balance import CollateralBalance
    from src.models.cdm.generated.event.common.collateral_position import CollateralPosition
    from src.models.cdm.generated.metafields.reference_with_meta_legal_agreement import ReferenceWithMetaLegalAgreement

class CollateralPortfolio(CdmModelBase):
    """Represents common attributes to define the details of collateral assets, to be used in margin call messaging and contribute to collateral balances e.g securities in a collateral account."""
    portfolio_identifier: ForwardRef("Identifier") = Field(None, description="Specifies a unique identifier for a set of collateral positions in a portfolio.")
    collateral_position: List[ForwardRef("CollateralPosition")] = Field(None, description="Specifies the individual components of the collateral positions in the collateral portfolio.")
    collateral_balance: List[ForwardRef("CollateralBalance")] = Field(None, description="Represents the populated or calculated collateral aggregate balance amount for the collateral portfolio.")
    legal_agreement: ForwardRef("ReferenceWithMetaLegalAgreement") = Field(None, description=" The specification of a legal agreement between two parties governing the collateral relationship such as Credit Support Agreement or Collateral Transfer Agreement etc. (NB: this can be provided by reference to a global key for each LegalAgreement object).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.event.common.collateral_balance import CollateralBalance
from src.models.cdm.generated.event.common.collateral_position import CollateralPosition
from src.models.cdm.generated.metafields.reference_with_meta_legal_agreement import ReferenceWithMetaLegalAgreement
CollateralPortfolio.model_rebuild()
