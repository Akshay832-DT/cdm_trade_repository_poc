from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_class_enum import AssetClassEnum
    from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.metafields.field_with_meta_quoted_currency_pair import FieldWithMetaQuotedCurrencyPair
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.observable.asset.information_source import InformationSource

class ForeignExchangeRateIndex(CdmModelBase):
    """Specification of a rate based on the exchange of a pair of cash assets in specific currencies, e.g. USD versus GBP."""
    identifier: List[ForwardRef("AssetIdentifier")] = Field(None, description="Asset Identifiers are used to uniquely identify an Asset, using a specified Asset Identifier Type.")
    taxonomy: List[ForwardRef("Taxonomy")] = Field(None, description="Defines the taxonomy of an object by combining a taxonomy source (i.e. the rules to classify the object) and a value (i.e. the output of those rules on the object.")
    is_exchange_listed: bool = Field(None, description="Defines whether the Asset is listed on a public exchange.")
    exchange: ForwardRef("LegalEntity") = Field(None, description="If the Asset is listed, defines the public exchange of the listing.")
    related_exchange: List[ForwardRef("LegalEntity")] = Field(None, description="Provides the related Exchanges, if applicable.")
    name: ForwardRef("FieldWithMetaString") = Field(None, description="A description of the Index.")
    provider: ForwardRef("LegalEntity") = Field(None, description="The organisation that creates or maintains the Index.")
    asset_class: ForwardRef("AssetClassEnum") = Field(None, description="The Asset Class of the Index.")
    quoted_currency_pair: ForwardRef("FieldWithMetaQuotedCurrencyPair") = Field(description="Describes the composition of a rate that has been quoted or is to be quoted.")
    primary_fx_spot_rate_source: ForwardRef("InformationSource") = Field(description="Specifies the primary source from which a rate should be observed.")
    secondary_fx_spot_rate_source: ForwardRef("InformationSource") = Field(None, description="Specifies an alternative, or secondary, source from which a rate should be observed.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset_class_enum import AssetClassEnum
from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.metafields.field_with_meta_quoted_currency_pair import FieldWithMetaQuotedCurrencyPair
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.asset.information_source import InformationSource
ForeignExchangeRateIndex.model_rebuild()
