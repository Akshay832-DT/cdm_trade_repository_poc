from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.arithmetic_operation_enum import ArithmeticOperationEnum
    from src.models.cdm.generated.base.math.dated_value import DatedValue
    from src.models.cdm.generated.base.math.unit_type import UnitType
    from src.models.cdm.generated.observable.asset.cash_price import CashPrice
    from src.models.cdm.generated.observable.asset.price_composite import PriceComposite
    from src.models.cdm.generated.observable.asset.price_expression_enum import PriceExpressionEnum
    from src.models.cdm.generated.observable.asset.price_type_enum import PriceTypeEnum

class PriceSchedule(CdmModelBase):
    """Specifies the price of a financial instrument in a trade as a schedule of measures. A price generically expresses the value of an exchange as a ratio: it measures the amount of one thing needed to be exchanged for 1 unit of another thing (e.g. cash in a specific currency in exchange for a bond or share). This generic representation can be used to support any type of financial price beyond just cash price: e.g. an interest rate, a foreign exchange rate, etc. This data type is generically based on a schedule and can also be used to represent a price as a single value."""
    value: float = Field(None, description="Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.")
    unit: ForwardRef("UnitType") = Field(None, description="Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).")
    dated_value: List[ForwardRef("DatedValue")] = Field(None, description="A schedule of step date and value pairs. On each step date the associated step value becomes effective. The step dates are used to order the steps by ascending order. This attribute is optional so the data type may be used to define a schedule with a single value.")
    per_unit_of: ForwardRef("UnitType") = Field(None, description="Provides an attribute to define the unit of the thing being priced. For example, {amount, unitOfAmount, PerUnitOfAmount} = [10, EUR, Shares] = (10.00 EUR/SHARE) * (300,000 SHARES) = EUR 3,000,000.00 (Shares cancel out in the calculation).")
    price_type: ForwardRef("PriceTypeEnum") = Field(description="Specifies the price type as an enumeration: interest rate, exchange rate, asset price etc. This attribute is mandatory so that prices can always be clasiffied according to their type. The price type implies some constraints on the price's units.")
    price_expression: ForwardRef("PriceExpressionEnum") = Field(None, description="(Optionally) Specifies whether the price is expressed in absolute or percentage terms.")
    composite: ForwardRef("PriceComposite") = Field(None, description="(Optionally) Specifies the underlying price components if the price can be expressed as a composite: e.g. dirty price = clean price + accrued.")
    arithmetic_operator: ForwardRef("ArithmeticOperationEnum") = Field(None, description="(Optionally) When the price is to be understood as an operator to apply to an observable, i.e. a spread, multiplier or min/max.")
    cash_price: ForwardRef("CashPrice") = Field(None, description="(Optionally when the price type is cash) Additional attributes that further define a cash price, e.g. what type of fee it is.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.arithmetic_operation_enum import ArithmeticOperationEnum
from src.models.cdm.generated.base.math.dated_value import DatedValue
from src.models.cdm.generated.base.math.unit_type import UnitType
from src.models.cdm.generated.observable.asset.cash_price import CashPrice
from src.models.cdm.generated.observable.asset.price_composite import PriceComposite
from src.models.cdm.generated.observable.asset.price_expression_enum import PriceExpressionEnum
from src.models.cdm.generated.observable.asset.price_type_enum import PriceTypeEnum
PriceSchedule.model_rebuild()
