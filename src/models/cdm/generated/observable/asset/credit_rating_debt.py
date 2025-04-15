from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.observable.asset.multiple_debt_types import MultipleDebtTypes

class CreditRatingDebt(CdmModelBase):
    """Specifies the credit rating debt type(s) associated with the credit rating notation and scale. When several debt types are specified, they must be qualified through an 'any' or 'all'."""
    debt_type: ForwardRef("FieldWithMetaString") = Field(None, description="Specifies when there is only one debt type. FpML doesn't specify values in relation to the associated scheme, which is hence not specified as an enumeration as part of the CDM.")
    debt_types: ForwardRef("MultipleDebtTypes") = Field(None, description="Specifies if there are several debt types, alongside an 'any' or 'all' or all condition. As an example, Baa1 rating is required for any long term debt and deposit.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.asset.multiple_debt_types import MultipleDebtTypes
CreditRatingDebt.model_rebuild()
