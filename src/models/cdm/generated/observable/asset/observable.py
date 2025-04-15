from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
    from src.models.cdm.generated.observable.asset.basket import Basket
    from src.models.cdm.generated.observable.asset.index import Index

class Observable(CdmModelBase):
    """Specifies the object to be observed for a price, it could be an asset or a reference."""
    asset: ForwardRef("Asset") = Field(None, description="The object to be observed is an Asset, ie something that can be owned and transferred in the financial markets.")
    basket: ForwardRef("Basket") = Field(None, description="The object to be observed is a Basket, ie a collection of Observables with an identifier and optional weightings.")
    index: ForwardRef("Index") = Field(None, description="The object to be observed is an Index, ie an observable computed on the prices, rates or valuations of a number of assets.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
from src.models.cdm.generated.observable.asset.basket import Basket
from src.models.cdm.generated.observable.asset.index import Index
Observable.model_rebuild()
