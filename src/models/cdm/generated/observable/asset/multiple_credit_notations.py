from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.quantifier_enum import QuantifierEnum
    from src.models.cdm.generated.metafields.field_with_meta_credit_notation import FieldWithMetaCreditNotation
    from src.models.cdm.generated.observable.asset.credit_notation_mismatch_resolution_enum import CreditNotationMismatchResolutionEnum
    from src.models.cdm.generated.observable.asset.credit_rating_agency_enum import CreditRatingAgencyEnum

class MultipleCreditNotations(CdmModelBase):
    """Represetns a class to specify multiple credit notations alongside a conditional 'any' or 'all' qualifier."""
    condition: ForwardRef("QuantifierEnum") = Field(description="An enumerated element, to qualify whether All or Any credit notation applies.")
    credit_notation: List[ForwardRef("FieldWithMetaCreditNotation")] = Field(None, description="At least two credit notations much be specified.")
    mismatch_resolution: ForwardRef("CreditNotationMismatchResolutionEnum") = Field(None)
    reference_agency: ForwardRef("CreditRatingAgencyEnum") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.quantifier_enum import QuantifierEnum
from src.models.cdm.generated.metafields.field_with_meta_credit_notation import FieldWithMetaCreditNotation
from src.models.cdm.generated.observable.asset.credit_notation_mismatch_resolution_enum import CreditNotationMismatchResolutionEnum
from src.models.cdm.generated.observable.asset.credit_rating_agency_enum import CreditRatingAgencyEnum
MultipleCreditNotations.model_rebuild()
