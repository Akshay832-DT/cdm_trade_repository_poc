from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.metafields.reference_with_meta_string import ReferenceWithMetaString
    from src.models.cdm.generated.observable.common.determination_method_enum import DeterminationMethodEnum

class DividendCurrency(CdmModelBase):
    """A class to specify the currency in which the dividends will be denominated, i.e. either in the dividend currency or in a currency specified as part of the contract."""
    currency: ForwardRef("FieldWithMetaString") = Field(None, description="The currency in which the dividend is denominated. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
    determination_method: ForwardRef("DeterminationMethodEnum") = Field(None, description="Specifies the method according to which the dividend is determined, e.g. the dividend currency.")
    currency_reference: ForwardRef("ReferenceWithMetaString") = Field(None, description="Reference to a currency specified elsewhere in the document")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.metafields.reference_with_meta_string import ReferenceWithMetaString
from src.models.cdm.generated.observable.common.determination_method_enum import DeterminationMethodEnum
DividendCurrency.model_rebuild()
