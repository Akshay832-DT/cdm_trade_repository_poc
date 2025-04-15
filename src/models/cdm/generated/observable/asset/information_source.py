from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_information_provider_enum import FieldWithMetaInformationProviderEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class InformationSource(CdmModelBase):
    """A class defining the source for a piece of information (e.g. a rate fix or an FX fixing). The attribute names have been adjusted from FpML to address the fact that the information is not limited to rates."""
    source_provider: ForwardRef("FieldWithMetaInformationProviderEnum") = Field(description="An information source for obtaining a market data point. For example Bloomberg, Reuters, Telerate, etc.")
    source_page: ForwardRef("FieldWithMetaString") = Field(None, description="A specific page for the source for obtaining a market data point. In FpML, this is specified as a scheme, rateSourcePageScheme, for which no coding Scheme or URI is specified.")
    source_page_heading: str = Field(None, description="The heading for the source on a given source page.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_information_provider_enum import FieldWithMetaInformationProviderEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
InformationSource.model_rebuild()
