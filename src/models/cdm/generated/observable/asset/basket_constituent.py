from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
    from src.models.cdm.generated.metafields.reference_with_meta_non_negative_quantity_schedule import ReferenceWithMetaNonNegativeQuantitySchedule
    from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
    from src.models.cdm.generated.observable.asset.basket import Basket
    from src.models.cdm.generated.observable.asset.index import Index

class BasketConstituent(CdmModelBase):
    """Identifies the constituents of the basket"""
    asset: Dict[str, Any] = Field(None, description="The object to be observed is an Asset, ie something that can be owned and transferred in the financial markets.")
    basket: Dict[str, Any] = Field(None, description="The object to be observed is a Basket, ie a collection of Observables with an identifier and optional weightings.")
    index: Dict[str, Any] = Field(None, description="The object to be observed is an Index, ie an observable computed on the prices, rates or valuations of a number of assets.")
    quantity: List[Dict[str, Any]] = Field(None, description="Specifies a quantity schedule to be associated to an individual underlier that is a basket constituent.")
    initial_valuation_price: List[Dict[str, Any]] = Field(None, description="Specifies an initial price schedule to be associated to an individual underlier that is a basket constituent.")
    interim_valuation_price: List[Dict[str, Any]] = Field(None, description="Specifies an interim price schedule to be associated to an individual underlier that is a basket constituent.")
    final_valuation_price: List[Dict[str, Any]] = Field(None, description="Specifies a final price schedule to be associated to an individual underlier that is a basket constituent.")

    @model_validator(mode='after')
    def validate_types(cls, values):
        from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
        from src.models.cdm.generated.metafields.reference_with_meta_non_negative_quantity_schedule import ReferenceWithMetaNonNegativeQuantitySchedule
        from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
        from src.models.cdm.generated.observable.asset.basket import Basket
        from src.models.cdm.generated.observable.asset.index import Index

        if values.asset is not None and not isinstance(values.asset, Asset):
            raise ValueError("asset must be an instance of Asset")
        if values.basket is not None and not isinstance(values.basket, Basket):
            raise ValueError("basket must be an instance of Basket")
        if values.index is not None and not isinstance(values.index, Index):
            raise ValueError("index must be an instance of Index")
        if values.quantity is not None:
            for item in values.quantity:
                if not isinstance(item, ReferenceWithMetaNonNegativeQuantitySchedule):
                    raise ValueError("quantity items must be instances of ReferenceWithMetaNonNegativeQuantitySchedule")
        if values.initial_valuation_price is not None:
            for item in values.initial_valuation_price:
                if not isinstance(item, ReferenceWithMetaPriceSchedule):
                    raise ValueError("initial_valuation_price items must be instances of ReferenceWithMetaPriceSchedule")
        if values.interim_valuation_price is not None:
            for item in values.interim_valuation_price:
                if not isinstance(item, ReferenceWithMetaPriceSchedule):
                    raise ValueError("interim_valuation_price items must be instances of ReferenceWithMetaPriceSchedule")
        if values.final_valuation_price is not None:
            for item in values.final_valuation_price:
                if not isinstance(item, ReferenceWithMetaPriceSchedule):
                    raise ValueError("final_valuation_price items must be instances of ReferenceWithMetaPriceSchedule")
        return values

BasketConstituent.model_rebuild()
