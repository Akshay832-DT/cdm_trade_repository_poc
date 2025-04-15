from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.iso_country_code_enum import ISOCountryCodeEnum

class AssetCountryOfOrigin(CdmModelBase):
    """"""
    asset_country_of_origin: ForwardRef("ISOCountryCodeEnum") = Field(description="Represents a filter on the asset country of origin based on the ISO Standard 3166.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.iso_country_code_enum import ISOCountryCodeEnum
AssetCountryOfOrigin.model_rebuild()
