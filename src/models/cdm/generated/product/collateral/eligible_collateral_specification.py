from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.product.collateral.eligible_collateral_criteria import EligibleCollateralCriteria

class EligibleCollateralSpecification(CdmModelBase):
    """Represents a set of criteria used to specify eligible collateral."""
    identifier: List[ForwardRef("Identifier")] = Field(None, description="Specifies the identifier(s) to uniquely identify eligible collateral or a set of eligible collateral, such as a schedule or equivalant for an identity issuer.")
    party: List[ForwardRef("Party")] = Field(None, description="The parties associated with the specification.")
    counterparty: List[ForwardRef("Counterparty")] = Field(None, description="Specification of the roles of the counterparties to the specification.")
    criteria: List[ForwardRef("EligibleCollateralCriteria")] = Field(None, description="Represents a set of criteria used to specify eligible collateral.")
    party_role: List[ForwardRef("PartyRole")] = Field(None, description="Specifies the role(s) that each of the party(s) is playing in the context of the specification, eg Payor or Receiver.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.product.collateral.eligible_collateral_criteria import EligibleCollateralCriteria
EligibleCollateralSpecification.model_rebuild()
