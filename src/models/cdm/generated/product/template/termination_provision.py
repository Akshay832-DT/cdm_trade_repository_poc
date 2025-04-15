from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.cancelable_provision import CancelableProvision
    from src.models.cdm.generated.product.template.early_termination_provision import EarlyTerminationProvision
    from src.models.cdm.generated.product.template.evergreen_provision import EvergreenProvision
    from src.models.cdm.generated.product.template.extendible_provision import ExtendibleProvision

class TerminationProvision(CdmModelBase):
    """A class for defining option provisions."""
    cancelable_provision: ForwardRef("CancelableProvision") = Field(None, description="A provision that allows the specification of an embedded option within a swap giving the buyer of the option the right to terminate the swap, in whole or in part, on the early termination date.")
    early_termination_provision: ForwardRef("EarlyTerminationProvision") = Field(None, description="Parameters specifying provisions relating to the optional and mandatory early termination of a swap transaction.")
    evergreen_provision: ForwardRef("EvergreenProvision") = Field(None, description="A data defining: the right of a party to exercise an Evergreen option")
    extendible_provision: ForwardRef("ExtendibleProvision") = Field(None, description="A provision that allows the specification of an embedded option with a swap giving the buyer of the option the right to extend the swap, in whole or in part, to the extended termination date.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.cancelable_provision import CancelableProvision
from src.models.cdm.generated.product.template.early_termination_provision import EarlyTerminationProvision
from src.models.cdm.generated.product.template.evergreen_provision import EvergreenProvision
from src.models.cdm.generated.product.template.extendible_provision import ExtendibleProvision
TerminationProvision.model_rebuild()
