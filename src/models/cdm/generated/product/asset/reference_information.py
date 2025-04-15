from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.product.asset.reference_obligation import ReferenceObligation

class ReferenceInformation(CdmModelBase):
    """A class specifying the Credit Default Swap Reference Information."""
    reference_entity: ForwardRef("LegalEntity") = Field(description="The corporate or sovereign entity which is subject to the swap transaction and any successor that assumes all or substantially all of its contractual and other obligations. Reference Entities cannot be senior or subordinated. It is the obligations of the Reference Entities that can be senior or subordinated. ISDA 2014 Credit definitions article II section 2.1: `Reference Entity` means the entity specified as such in the related Confirmation.")
    reference_obligation: List[ForwardRef("ReferenceObligation")] = Field(None, description="The Reference Obligation is a financial instrument that is either issued or guaranteed by the reference entity. It serves to clarify the precise reference entity protection is being offered upon, and its legal position with regard to other related firms (parents/subsidiaries). Furthermore the Reference Obligation is ALWAYS deliverable and establishes the Pari Passu ranking (as the deliverable bonds must rank equal to the reference obligation). ISDA 2003 Term: Reference Obligation.")
    no_reference_obligation: bool = Field(None, description="Used to indicate that there is no Reference Obligation associated with this Credit Default Swap and that there will never be one.")
    unknown_reference_obligation: bool = Field(None, description="Used to indicate that the Reference obligation associated with the Credit Default Swap is currently not known. This is not valid for Legal Confirmation purposes, but is valid for earlier stages in the trade life cycle (e.g. Broker Confirmation).")
    all_guarantees: bool = Field(None, description="Indicates whether an obligation of the Reference Entity, guaranteed by the Reference Entity on behalf of a non-Affiliate, is to be considered an Obligation for the purpose of the transaction. It will be considered an obligation if allGuarantees is applicable (true) and not if allGuarantees is inapplicable (false). ISDA 2003 Term: All Guarantees.")
    reference_price: ForwardRef("Price") = Field(None, description="Used to determine (a) for physically settled trades, the Physical Settlement Amount, which equals the Floating Rate Payer Calculation Amount times the Reference Price and (b) for cash settled trades, the Cash Settlement Amount, which equals the greater of (i) the difference between the Reference Price and the Final Price and (ii) zero. ISDA 2003 Term: Reference Price.")
    reference_policy: bool = Field(None, description="Applicable to the transactions on mortgage-backed security, which can make use of a reference policy. Presence of the element with value set to 'true' indicates that the reference policy is applicable; absence implies that it is not.")
    secured_list: bool = Field(None, description="With respect to any day, the list of Syndicated Secured Obligations of the Designated Priority of the Reference Entity published by Markit Group Limited or any successor thereto appointed by the Specified Dealers (the 'Secured List Publisher') on or most recently before such day, which list is currently available at [http://www.markit.com]. ISDA 2003 Term: Relevant Secured List.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.product.asset.reference_obligation import ReferenceObligation
ReferenceInformation.model_rebuild()
