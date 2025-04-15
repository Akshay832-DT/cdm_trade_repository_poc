from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.observable.asset.quote_basis_enum import QuoteBasisEnum

class QuotedCurrencyPair(CdmModelBase):
    """A class that describes the composition of a rate that has been quoted or is to be quoted. This includes the two currencies and the quotation relationship between the two currencies and is used as a building block throughout the FX specification."""
    currency1: ForwardRef("FieldWithMetaString") = Field(description="The first currency specified when a pair of currencies is to be evaluated.")
    currency2: ForwardRef("FieldWithMetaString") = Field(description="The second currency specified when a pair of currencies is to be evaluated.")
    quote_basis: ForwardRef("QuoteBasisEnum") = Field(description="The method by which the exchange rate is quoted.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.asset.quote_basis_enum import QuoteBasisEnum
QuotedCurrencyPair.model_rebuild()
