from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
    from src.models.cdm.generated.product.common.settlement.deliverable_obligations import DeliverableObligations
    from src.models.cdm.generated.product.common.settlement.physical_settlement_period import PhysicalSettlementPeriod

class PhysicalSettlementTerms(CdmModelBase):
    """Specifies Physical Settlement Terms characteristics for the settlement of a Credit Default Swap or Option."""
    cleared_physical_settlement: bool = Field(None, description="Specifies whether the swap resulting from physical settlement of the swaption transaction will clear through a clearing house. The meaning of Cleared Physical Settlement is defined in the 2006 ISDA Definitions, Section 15.2 (published in Supplement number 28).")
    predetermined_clearing_organization_party: ForwardRef("AncillaryRoleEnum") = Field(None, description="Specifies the clearing organization (CCP, DCO) to which the trade should be cleared.")
    physical_settlement_period: ForwardRef("PhysicalSettlementPeriod") = Field(None, description="The number of business days used in the determination of the physical settlement date. The physical settlement date is this number of business days after all applicable conditions to settlement are satisfied. If a number of business days is not specified fallback provisions apply for determining the number of business days. If Section 8.5/8.6 of the 1999/2003 ISDA Definitions are to apply the businessDaysNotSpecified element should be included. If a specified number of business days are to apply these should be specified in the businessDays element. If Section 8.5/8.6 of the 1999/2003 ISDA Definitions are to apply but capped at a maximum number of business days then the maximum number should be specified in the maximumBusinessDays element. ISDA 2003 Term: Physical Settlement Period.")
    deliverable_obligations: ForwardRef("DeliverableObligations") = Field(None, description="This element contains all the ISDA terms relevant to defining the deliverable obligations.")
    escrow: bool = Field(None, description="If this element is specified and set to 'true', indicates that physical settlement must take place through the use of an escrow agent. (For Canadian counterparties this is always 'Not Applicable'. ISDA 2003 Term: Escrow.")
    sixty_business_day_settlement_cap: bool = Field(None, description="If this element is specified and set to 'true', for a transaction documented under the 2003 ISDA Credit Derivatives Definitions, has the effect of incorporating the language set forth below into the confirmation. The section references are to the 2003 ISDA Credit Derivatives Definitions. Notwithstanding Section 1.7 or any provisions of Sections 9.9 or 9.10 to the contrary, but without prejudice to Section 9.3 and (where applicable) Sections 9.4, 9.5 and 9.6, if the Termination Date has not occurred on or prior to the date that is 60 Business Days following the Physical Settlement Date, such 60th Business Day shall be deemed to be the Termination Date with respect to this Transaction except in relation to any portion of the Transaction (an 'Affected Portion') in respect of which: (1) a valid notice of Buy-in Price has been delivered that is effective fewer than three Business Days prior to such 60th Business Day, in which case the Termination Date for that Affected Portion shall be the third Business Day following the date on which such notice is effective; or (2) Buyer has purchased but not Delivered Deliverable Obligations validly specified by Seller pursuant to Section 9.10(b), in which case the Termination Date for that Affected Portion shall be the tenth Business Day following the date on which Seller validly specified such Deliverable Obligations to Buyer.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
from src.models.cdm.generated.product.common.settlement.deliverable_obligations import DeliverableObligations
from src.models.cdm.generated.product.common.settlement.physical_settlement_period import PhysicalSettlementPeriod
PhysicalSettlementTerms.model_rebuild()
