from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.meta_fields import MetaFields
    from src.models.cdm.generated.observable.asset.basket_constituent import BasketConstituent

class FieldWithMetaBasketConstituent(CdmModelBase):
    """A class to represent a basket constituent with metadata."""
    value: Dict[str, Any] = Field(None, description="The basket constituent value.")
    meta: Dict[str, Any] = Field(None, description="The metadata associated with the basket constituent.")

    @model_validator(mode='after')
    def validate_types(cls, values):
        from src.models.cdm.generated.metafields.meta_fields import MetaFields
        from src.models.cdm.generated.observable.asset.basket_constituent import BasketConstituent

        if values.value is not None and not isinstance(values.value, BasketConstituent):
            raise ValueError("value must be an instance of BasketConstituent")
        if values.meta is not None and not isinstance(values.meta, MetaFields):
            raise ValueError("meta must be an instance of MetaFields")
        return values

FieldWithMetaBasketConstituent.model_rebuild()
