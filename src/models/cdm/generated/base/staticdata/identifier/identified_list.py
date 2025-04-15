from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.observable.asset.price import Price

class IdentifiedList(CdmModelBase):
    """Attaches an identifier to a collection of objects, when those objects themselves can each be represented by an identifier. One use case is the representation of package transactions, where each component is a separate trade with its own identifier, and those trades are linked together as a package with its own identifier. The data type has been named generically rather than referring to 'packages' as it may have a number of other uses."""
    list_id: ForwardRef("Identifier") = Field(description="The identifier for the list. In the case of a package transaction, this would be the package identifier. This attribute is mandatory to allow the list itself to be identified.")
    component_id: List[ForwardRef("Identifier")] = Field(None, description="Identifiers for each component of the list. Since the data type is used to link multiple identified objects together, at least 2 components are required in the list. Creating an identified list with only 1 identified component has been deemed unnecessary, because it would just create a redundant identifier.")
    price: ForwardRef("Price") = Field(None, description="The price of the package.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.observable.asset.price import Price
IdentifiedList.model_rebuild()
