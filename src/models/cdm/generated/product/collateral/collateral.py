from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.metafields.reference_with_meta_collateral_portfolio import ReferenceWithMetaCollateralPortfolio
    from src.models.cdm.generated.product.collateral.collateral_provisions import CollateralProvisions
    from src.models.cdm.generated.product.collateral.independent_amount import IndependentAmount

class Collateral(CdmModelBase):
    """A type for defining the obligations of the counterparty subject to credit support requirements."""
    independent_amount: ForwardRef("IndependentAmount") = Field(None, description="Independent Amount is an amount that usually less creditworthy counterparties are asked to provide. It can either be a fixed amount or a percentage of the Transaction's value. The Independent Amount can be: (i) transferred before any trading between the parties occurs (as a deposit at a third party's account or with the counterparty) or (ii) callable after trading has occurred (typically because a downgrade has occurred). In situation (i), the Independent Amount is not included in the calculation of Exposure, but in situation (ii), it is included in the calculation of Exposure. Thus, for situation (ii), the Independent Amount may be transferred along with any collateral call. Independent Amount is a defined term in the ISDA Credit Support Annex. ('with respect to a party, the amount specified as such for that party in Paragraph 13; if no amount is specified, zero').")
    portfolio_identifier: List[ForwardRef("Identifier")] = Field(None, description="A list of identifiers pointing to the collateral portfolios which contain the collateral which covers a trade.")
    collateral_portfolio: List[ForwardRef("ReferenceWithMetaCollateralPortfolio")] = Field(None, description="The collateral portfolios which contain the collateral which covers a trade. (NB: this can be provided by reference to a global key for each CollateralPortfolio object)")
    collateral_provisions: ForwardRef("CollateralProvisions") = Field(None, description="specifies the collateral provisions of the product.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.metafields.reference_with_meta_collateral_portfolio import ReferenceWithMetaCollateralPortfolio
from src.models.cdm.generated.product.collateral.collateral_provisions import CollateralProvisions
from src.models.cdm.generated.product.collateral.independent_amount import IndependentAmount
Collateral.model_rebuild()
