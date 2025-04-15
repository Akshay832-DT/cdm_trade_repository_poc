from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.observable.asset.credit_index import CreditIndex
    from src.models.cdm.generated.product.asset.basket_reference_information import BasketReferenceInformation
    from src.models.cdm.generated.product.asset.reference_information import ReferenceInformation

class GeneralTerms(CdmModelBase):
    """ A class specifying a set of non-monetary terms for the Credit Derivative Transaction, including the buyer and seller and selected items from the ISDA 2014 Credit Definition article II, such as the reference obligation and related terms. The CDM GeneralTerms class corresponds to the FpML GeneralTerms complex type, except that the effectiveDate and scheduledTerminationDate have been positioned as part of the InterestRatePayout class in the CDM instead of in GeneralTerms."""
    reference_information: ForwardRef("ReferenceInformation") = Field(None, description="This attribute contains all the terms relevant to defining the reference entity and reference obligation(s).")
    index_reference_information: ForwardRef("CreditIndex") = Field(None, description="This attribute contains all the terms relevant to the underlying Index.")
    basket_reference_information: ForwardRef("BasketReferenceInformation") = Field(None, description="This attribute contains all the terms relevant to defining the Credit Default Swap Basket.")
    additional_term: List[ForwardRef("FieldWithMetaString")] = Field(None, description="This attribute is used for representing information contained in the Additional Terms field of the 2003 Master Credit Derivatives confirm.")
    substitution: bool = Field(None, description="Value of this attribute set to 'true' indicates that substitution is applicable.")
    modified_equity_delivery: bool = Field(None, description="Value of this attribute set to 'true' indicates that modified equity delivery is applicable.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.asset.credit_index import CreditIndex
from src.models.cdm.generated.product.asset.basket_reference_information import BasketReferenceInformation
from src.models.cdm.generated.product.asset.reference_information import ReferenceInformation
GeneralTerms.model_rebuild()
