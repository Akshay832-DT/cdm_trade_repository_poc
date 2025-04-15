from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity

class Cash(CdmModelBase):
    """An Asset that consists solely of a monetary holding in a currency. The currency of the Cash asset is held in the string Identifier (from AssetBase) and the AssetIdTypeEnum must be set to define that a CurrencyCode is set.  The function SetCashCurrency can be used to create (or update) a Cash object and the function GetCashCurrency can be used to retrieve the currency of a Cash object."""
    identifier: List[ForwardRef("AssetIdentifier")] = Field(None, description="Asset Identifiers are used to uniquely identify an Asset, using a specified Asset Identifier Type.")
    taxonomy: List[ForwardRef("Taxonomy")] = Field(None, description="Defines the taxonomy of an object by combining a taxonomy source (i.e. the rules to classify the object) and a value (i.e. the output of those rules on the object.")
    is_exchange_listed: bool = Field(None, description="Defines whether the Asset is listed on a public exchange.")
    exchange: ForwardRef("LegalEntity") = Field(None, description="If the Asset is listed, defines the public exchange of the listing.")
    related_exchange: List[ForwardRef("LegalEntity")] = Field(None, description="Provides the related Exchanges, if applicable.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
Cash.model_rebuild()
