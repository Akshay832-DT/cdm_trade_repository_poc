from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.metafields.field_with_meta_information_provider_enum import FieldWithMetaInformationProviderEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class FxInformationSource(CdmModelBase):
    """Information source specific to Foreign Exchange products."""
    source_provider: ForwardRef("FieldWithMetaInformationProviderEnum") = Field(None, description="An information source for obtaining a market data point. For example Bloomberg, Reuters, Telerate, etc.")
    source_page: ForwardRef("FieldWithMetaString") = Field(None, description="A specific page for the source for obtaining a market data point. In FpML, this is specified as a scheme, rateSourcePageScheme, for which no coding Scheme or URI is specified.")
    source_page_heading: str = Field(None, description="The heading for the source on a given source page.")
    fixing_time: ForwardRef("BusinessCenterTime") = Field(None, description="The time that the fixing will be taken along with a business center to define the time zone.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.metafields.field_with_meta_information_provider_enum import FieldWithMetaInformationProviderEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
FxInformationSource.model_rebuild()
