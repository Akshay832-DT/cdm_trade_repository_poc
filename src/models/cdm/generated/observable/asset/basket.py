from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.metafields.field_with_meta_basket_constituent import FieldWithMetaBasketConstituent

class Basket(CdmModelBase):
    """Defines a custom basket by referencing an identifier and its constituents."""
    identifier: List[Dict[str, Any]] = Field(None, description="Asset Identifiers are used to uniquely identify an Asset, using a specified Asset Identifier Type.")
    taxonomy: List[Dict[str, Any]] = Field(None, description="Defines the taxonomy of an object by combining a taxonomy source (i.e. the rules to classify the object) and a value (i.e. the output of those rules on the object.")
    is_exchange_listed: bool = Field(None, description="Defines whether the Asset is listed on a public exchange.")
    exchange: Dict[str, Any] = Field(None, description="If the Asset is listed, defines the public exchange of the listing.")
    related_exchange: List[Dict[str, Any]] = Field(None, description="Provides the related Exchanges, if applicable.")
    basket_constituent: List[Dict[str, Any]] = Field(None, description="Identifies the constituents of the basket")

    @model_validator(mode='after')
    def validate_types(cls, values):
        from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
        from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
        from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
        from src.models.cdm.generated.metafields.field_with_meta_basket_constituent import FieldWithMetaBasketConstituent

        if values.identifier is not None:
            for item in values.identifier:
                if not isinstance(item, AssetIdentifier):
                    raise ValueError("identifier items must be instances of AssetIdentifier")
        if values.taxonomy is not None:
            for item in values.taxonomy:
                if not isinstance(item, Taxonomy):
                    raise ValueError("taxonomy items must be instances of Taxonomy")
        if values.exchange is not None and not isinstance(values.exchange, LegalEntity):
            raise ValueError("exchange must be an instance of LegalEntity")
        if values.related_exchange is not None:
            for item in values.related_exchange:
                if not isinstance(item, LegalEntity):
                    raise ValueError("related_exchange items must be instances of LegalEntity")
        if values.basket_constituent is not None:
            for item in values.basket_constituent:
                if not isinstance(item, FieldWithMetaBasketConstituent):
                    raise ValueError("basket_constituent items must be instances of FieldWithMetaBasketConstituent")
        return values

Basket.model_rebuild()
