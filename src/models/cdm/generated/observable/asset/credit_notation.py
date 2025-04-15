from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.observable.asset.credit_rating_agency_enum import CreditRatingAgencyEnum
    from src.models.cdm.generated.observable.asset.credit_rating_credit_watch_enum import CreditRatingCreditWatchEnum
    from src.models.cdm.generated.observable.asset.credit_rating_debt import CreditRatingDebt
    from src.models.cdm.generated.observable.asset.credit_rating_outlook_enum import CreditRatingOutlookEnum

class CreditNotation(CdmModelBase):
    """Represents a class to specify the credit notation as the combination of agency, notation, scale and debt type qualifications."""
    agency: ForwardRef("CreditRatingAgencyEnum") = Field(description="Specifies The credit agency to which the other variables (notation, scale, debt type) refer to.")
    notation: ForwardRef("FieldWithMetaString") = Field(description="Specifies The credit rating notation. As it varies among credit rating agencies, FpML doesn't specify a default scheme.")
    scale: ForwardRef("FieldWithMetaString") = Field(None, description="Specifies the credit rating scale, with a typical distinction between short term, long term. FpML doesn't specify a default scheme, which is hence not specified as an enumeration as part of the CDM.")
    debt: ForwardRef("CreditRatingDebt") = Field(None, description="Specifies the credit rating debt type (e.g. long term, high yield, deposits, ...) associated with the credit rating notation and scale.")
    outlook: ForwardRef("CreditRatingOutlookEnum") = Field(None, description="Assesses the potential direction of a long-term credit rating over the intermediate term, which is generally up to two years for investment grade and generally up to one year for speculative grade.")
    credit_watch: ForwardRef("CreditRatingCreditWatchEnum") = Field(None, description="Indicates the potential direction of a short-term or long-term rating. It focuses on identifiable events and short-term trends that cause ratings to be placed under special surveillance.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.asset.credit_rating_agency_enum import CreditRatingAgencyEnum
from src.models.cdm.generated.observable.asset.credit_rating_credit_watch_enum import CreditRatingCreditWatchEnum
from src.models.cdm.generated.observable.asset.credit_rating_debt import CreditRatingDebt
from src.models.cdm.generated.observable.asset.credit_rating_outlook_enum import CreditRatingOutlookEnum
CreditNotation.model_rebuild()
