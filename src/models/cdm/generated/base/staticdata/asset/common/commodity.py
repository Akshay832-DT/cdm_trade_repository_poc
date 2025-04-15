from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
    from src.models.cdm.generated.base.staticdata.asset.common.commodity_product_definition import CommodityProductDefinition
    from src.models.cdm.generated.base.staticdata.asset.common.delivery_date_parameters import DeliveryDateParameters
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.observable.asset.quotation_side_enum import QuotationSideEnum

class Commodity(CdmModelBase):
    """Identifies a specific commodity by referencing a product identifier or by a product definition."""
    identifier: List[ForwardRef("AssetIdentifier")] = Field(None, description="Asset Identifiers are used to uniquely identify an Asset, using a specified Asset Identifier Type.")
    taxonomy: List[ForwardRef("Taxonomy")] = Field(None, description="Defines the taxonomy of an object by combining a taxonomy source (i.e. the rules to classify the object) and a value (i.e. the output of those rules on the object.")
    is_exchange_listed: bool = Field(None, description="Defines whether the Asset is listed on a public exchange.")
    exchange: ForwardRef("LegalEntity") = Field(None, description="If the Asset is listed, defines the public exchange of the listing.")
    related_exchange: List[ForwardRef("LegalEntity")] = Field(None, description="Provides the related Exchanges, if applicable.")
    commodity_product_definition: ForwardRef("CommodityProductDefinition") = Field(None, description="Specifies the commodity underlier in the event that no ISDA Commodity Reference Benchmark exists.")
    price_quote_type: ForwardRef("QuotationSideEnum") = Field(description="Describes the required quote type of the underlying price that will be observed. Example values include 'Bid, 'Ask', 'Settlement' (for a futures contract) and 'WeightedAverage' (for some published prices and indices).")
    delivery_date_reference: ForwardRef("DeliveryDateParameters") = Field(None, description="Specifies the parameters for identifying the relevant contract date when the commodity reference price is a futures contract.")
    description: str = Field(None, description="Provides additional information about the commodity underlier.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
from src.models.cdm.generated.base.staticdata.asset.common.commodity_product_definition import CommodityProductDefinition
from src.models.cdm.generated.base.staticdata.asset.common.delivery_date_parameters import DeliveryDateParameters
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.observable.asset.quotation_side_enum import QuotationSideEnum
Commodity.model_rebuild()
