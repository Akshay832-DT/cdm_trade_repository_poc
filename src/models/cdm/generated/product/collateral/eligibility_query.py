from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_type import AssetType
    from src.models.cdm.generated.base.staticdata.asset.common.collateral_issuer_type import CollateralIssuerType
    from src.models.cdm.generated.base.staticdata.asset.common.currency_code_enum import CurrencyCodeEnum
    from src.models.cdm.generated.base.staticdata.asset.common.iso_country_code_enum import ISOCountryCodeEnum
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.product.collateral.agency_rating_criteria import AgencyRatingCriteria

class EligibilityQuery(CdmModelBase):
    """Query to check against an EligibleCollateralSpecification"""
    maturity: float = Field(description="Maturity in years")
    collateral_asset_type: ForwardRef("AssetType") = Field(description="The asset product type.")
    asset_country_of_origin: ForwardRef("ISOCountryCodeEnum") = Field(description="The asset country of origin.")
    denominated_currency: ForwardRef("CurrencyCodeEnum") = Field(description="The underlying asset denominated currency.")
    agency_rating: ForwardRef("AgencyRatingCriteria") = Field(description="The agency rating based on default risk and creditors claim in event of default associated with specific instrument.")
    issuer_type: ForwardRef("CollateralIssuerType") = Field(description="Represents a filter based on the type of entity issuing the asset.")
    issuer_name: ForwardRef("LegalEntity") = Field(description="Specifies the issuing entity name or LEI.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset_type import AssetType
from src.models.cdm.generated.base.staticdata.asset.common.collateral_issuer_type import CollateralIssuerType
from src.models.cdm.generated.base.staticdata.asset.common.currency_code_enum import CurrencyCodeEnum
from src.models.cdm.generated.base.staticdata.asset.common.iso_country_code_enum import ISOCountryCodeEnum
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.product.collateral.agency_rating_criteria import AgencyRatingCriteria
EligibilityQuery.model_rebuild()
