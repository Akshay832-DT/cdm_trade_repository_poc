from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

# Import all dependencies before class definition
from src.models.cdm.generated.base.staticdata.asset.common.asset_type import AssetType
from src.models.cdm.generated.base.staticdata.asset.common.collateral_issuer_type import CollateralIssuerType
from src.models.cdm.generated.base.staticdata.asset.common.collateral_taxonomy import CollateralTaxonomy
from src.models.cdm.generated.base.staticdata.asset.common.currency_code_enum import CurrencyCodeEnum
from src.models.cdm.generated.observable.asset.index import Index
from src.models.cdm.generated.product.collateral.asset_agency_rating import AssetAgencyRating
from src.models.cdm.generated.product.collateral.asset_country_of_origin import AssetCountryOfOrigin
from src.models.cdm.generated.product.collateral.asset_maturity import AssetMaturity
from src.models.cdm.generated.product.collateral.counterparty_own_issue_permitted import CounterpartyOwnIssuePermitted
from src.models.cdm.generated.product.collateral.domestic_currency_issued import DomesticCurrencyIssued
from src.models.cdm.generated.product.collateral.issuer_agency_rating import IssuerAgencyRating
from src.models.cdm.generated.product.collateral.issuer_country_of_origin import IssuerCountryOfOrigin
from src.models.cdm.generated.product.collateral.issuer_name import IssuerName
from src.models.cdm.generated.product.collateral.listing_exchange import ListingExchange
from src.models.cdm.generated.product.collateral.listing_sector import ListingSector
from src.models.cdm.generated.product.collateral.specific_asset import SpecificAsset

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.all_criteria import AllCriteria
    from src.models.cdm.generated.product.collateral.any_criteria import AnyCriteria
    from src.models.cdm.generated.product.collateral.negative_criteria import NegativeCriteria
    from src.models.cdm.generated.product.collateral.sovereign_agency_rating import SovereignAgencyRating

class CollateralCriteria(CdmModelBase):
    """The possible different terms that can be combined, using AND, OR and NOT logic, to define the issuers and/or assets that meet a given criteria for collateral."""
    all_criteria: Optional[Any] = Field(None, description="Enables two or more Collateral Criteria to be combined using AND logic.")
    any_criteria: Optional[Any] = Field(None, description="Enables two or more Collateral Criteria to be combined using OR logic.")
    negative_criteria: Optional[Any] = Field(None, description="Enables a single Collateral Criteria to be excluded using NOT logic.")
    collateral_issuer_type: Optional[CollateralIssuerType] = Field(None, description="Criteria is the type of entity issuing the asset.")
    asset_type: Optional[AssetType] = Field(None, description="Criteria is the asset type of the collateral.")
    issuer_country_of_origin: Optional[IssuerCountryOfOrigin] = Field(None, description="Criteria is the issuing entity country of origin.")
    asset_country_of_origin: Optional[AssetCountryOfOrigin] = Field(None, description="Criteria is the collateral asset country of origin.")
    currency_code_enum: Optional[CurrencyCodeEnum] = Field(None, description="Criteria is the denominated currency of the collateral.")
    issuer_name: Optional[IssuerName] = Field(None, description="Criteria is a specific named issuer entity.")
    issuer_agency_rating: Optional[IssuerAgencyRating] = Field(None, description="Criteria is the agency rating(s) of the issuer.")
    sovereign_agency_rating: Optional["SovereignAgencyRating"] = Field(None, description="Criteria is the agency rating(s) of the country of the issuer.")
    asset_agency_rating: Optional[AssetAgencyRating] = Field(None, description="Criteria is the agency rating(s) of the collateral asset.")
    asset_maturity: Optional[AssetMaturity] = Field(None, description="Criteria is the maturity characteristics of the collateral asset.")
    specific_asset: Optional[SpecificAsset] = Field(None, description="Criteria is a specifically identified asset")
    collateral_taxonomy: Optional[CollateralTaxonomy] = Field(None, description="Criteria is the taxonomy characteristics of an collateral.")
    listing_exchange: Optional[ListingExchange] = Field(None, description="Criteria is that the collateral is listed on a specific exchange.")
    listing_sector: Optional[ListingSector] = Field(None, description="Criteria is the industry sector of the collateral asset.")
    index: Optional[Index] = Field(None, description="Criteria is that the collateral is a constituent of a specific index.")
    counterparty_own_issue_permitted: Optional[CounterpartyOwnIssuePermitted] = Field(None, description="Criteria includes collateral issued by the counterparty.")
    domestic_currency_issued: Optional[DomesticCurrencyIssued] = Field(None, description="Criteria is that collateral must be denominated in the domestic currency of the issuer.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.all_criteria import AllCriteria
from src.models.cdm.generated.product.collateral.any_criteria import AnyCriteria
from src.models.cdm.generated.product.collateral.negative_criteria import NegativeCriteria
from src.models.cdm.generated.product.collateral.sovereign_agency_rating import SovereignAgencyRating

# Update field types after importing circular dependencies
CollateralCriteria.__annotations__["all_criteria"] = Optional[AllCriteria]
CollateralCriteria.__annotations__["any_criteria"] = Optional[AnyCriteria]
CollateralCriteria.__annotations__["negative_criteria"] = Optional[NegativeCriteria]
CollateralCriteria.__annotations__["sovereign_agency_rating"] = Optional[SovereignAgencyRating]

CollateralCriteria.model_rebuild()
