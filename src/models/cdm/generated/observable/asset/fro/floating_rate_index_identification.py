from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.iso_currency_code_enum import ISOCurrencyCodeEnum
    from src.models.cdm.generated.metafields.field_with_meta_floating_rate_index_enum import FieldWithMetaFloatingRateIndexEnum

class FloatingRateIndexIdentification(CdmModelBase):
    """"""
    floating_rate_index: ForwardRef("FieldWithMetaFloatingRateIndexEnum") = Field(None, description="The reference index that is used to specify the floating interest rate. The FpML standard maintains the list of such indices, which are positioned as enumeration values as part of the CDM.")
    currency: ForwardRef("ISOCurrencyCodeEnum") = Field(None, description="FRO currency - 3 character ISO currrency code")
    fro_type: str = Field(None, description="FRO type (e.g. OIS)")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.iso_currency_code_enum import ISOCurrencyCodeEnum
from src.models.cdm.generated.metafields.field_with_meta_floating_rate_index_enum import FieldWithMetaFloatingRateIndexEnum
FloatingRateIndexIdentification.model_rebuild()
