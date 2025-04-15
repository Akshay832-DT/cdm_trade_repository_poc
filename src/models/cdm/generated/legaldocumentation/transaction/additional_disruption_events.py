from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
    from src.models.cdm.generated.legaldocumentation.transaction.clause import Clause

class AdditionalDisruptionEvents(CdmModelBase):
    """A type for defining the Additional Disruption Events."""
    change_in_law: bool = Field(None, description="Per 2002 ISDA Equity Derivatives Definitions: ")
    failure_to_deliver: bool = Field(None, description="Per 2002 ISDA Equity Derivatives Definitions")
    insolvency_filing: bool = Field(None, description="Per 2002 ISDA Equity Derivatives Definitions")
    hedging_disruption: bool = Field(None, description="Per 2002 ISDA Equity Derivatives Definitions")
    increased_cost_of_hedging: bool = Field(None, description="Per 2002 ISDA Equity Derivatives Definitions")
    foreign_ownership_event: bool = Field(None, description="Per ISDA Def ")
    loss_of_stock_borrow: bool = Field(None, description="Per 2002 ISDA Equity Derivatives Definitions:")
    maximum_stock_loan_rate: float = Field(None, description="Specifies the maximum stock loan rate for Loss of Stock Borrow. A percentage of 5% is represented as 0.05.")
    increased_cost_of_stock_borrow: bool = Field(None, description="Per 2002 ISDA Equity Derivatives Definitions")
    initial_stock_loan_rate: float = Field(None, description="Specifies the initial stock loan per ISDA Def. A percentage of 5% is represented as 0.05.")
    determining_party: ForwardRef("AncillaryRoleEnum") = Field(None, description="Specifies the party which determines additional disruption events.")
    additional_bespoke_terms: List[ForwardRef("Clause")] = Field(None, description="Where parties may optionnaly describe any extra bespoke agreements, in regards of the standardized Extraordinary Events.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
from src.models.cdm.generated.legaldocumentation.transaction.clause import Clause
AdditionalDisruptionEvents.model_rebuild()
