from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.arithmetic_operation_enum import ArithmeticOperationEnum
    from src.models.cdm.generated.observable.asset.price_operand_enum import PriceOperandEnum

class PriceComposite(CdmModelBase):
    """Defines the inputs required to calculate a price as a simple composite of 2 other values. The inputs consist of 2 numbers and a simple arithmetic operator. This generic data type applies to a variety of use cases where a price is obtained by simple composition, e.g. dirty = clean + accrued (Bond), forward rate = spot rate + forward point (FX) etc."""
    base_value: float = Field(description="The 1st value in the arithmetic operation, which may be non-commutative in some cases: Subtract, Divide). This 1st operand is called 'baseValue' as it refers to the price anchor in the arithmetic operation: e.g. the clean price (Bond) or the spot rate (FX).")
    operand: float = Field(description="The 2nd value in the arithmetic operation, which may be non-commutative in some cases: Subtract, Divide). The 2nd operand is called 'operand' to distinguish it from the 1st one which is the price anchor.")
    arithmetic_operator: ForwardRef("ArithmeticOperationEnum") = Field(description="Specifies the arithmetic operator via an enumeration.")
    operand_type: ForwardRef("PriceOperandEnum") = Field(None, description="Optionally qualifies the type of operand: e.g. accrued or forward point.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.arithmetic_operation_enum import ArithmeticOperationEnum
from src.models.cdm.generated.observable.asset.price_operand_enum import PriceOperandEnum
PriceComposite.model_rebuild()
