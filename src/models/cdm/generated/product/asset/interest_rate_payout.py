from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.metafields.field_with_meta_day_count_fraction_enum import FieldWithMetaDayCountFractionEnum
    from src.models.cdm.generated.product.asset.bond_reference import BondReference
    from src.models.cdm.generated.product.asset.cashflow_representation import CashflowRepresentation
    from src.models.cdm.generated.product.asset.compounding_method_enum import CompoundingMethodEnum
    from src.models.cdm.generated.product.asset.discounting_method import DiscountingMethod
    from src.models.cdm.generated.product.asset.rate_specification import RateSpecification
    from src.models.cdm.generated.product.asset.spread_calculation_method_enum import SpreadCalculationMethodEnum
    from src.models.cdm.generated.product.common.schedule.calculation_period_dates import CalculationPeriodDates
    from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
    from src.models.cdm.generated.product.common.schedule.reset_dates import ResetDates
    from src.models.cdm.generated.product.common.schedule.stub_period import StubPeriod
    from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
    from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
    from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms

class InterestRatePayout(CdmModelBase):
    """ A class to specify all of the terms necessary to define and calculate a cash flow based on a fixed, a floating or an inflation index rate. The interest rate payout can be applied to interest rate swaps and FRA (which both have two associated interest rate payouts), credit default swaps (to represent the fee leg when subject to periodic payments) and equity swaps (to represent the funding leg). The associated globalKey denotes the ability to associate a hash value to the InterestRatePayout instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage."""
    payer_receiver: ForwardRef("PayerReceiver") = Field(None, description="Canonical representation of the payer and receiver parties applicable to each payout leg.")
    price_quantity: ForwardRef("ResolvablePriceQuantity") = Field(None, description="Each payout leg must implement the quantity concept as a 'resolvable' type, which allows for different payout legs to be linked to each other (e.g. in the case of cross-curreny products).")
    principal_payment: ForwardRef("PrincipalPayments") = Field(None, description="The specification of the principal exchange. Optional as only applicable in the case of cross-currency or zero-coupon swaps with a final payment.")
    settlement_terms: ForwardRef("SettlementTerms") = Field(None, description="Each payout leg must specifies its settlement terms, including the delivery type (i.e. cash vs physical, and their respective terms), the transfer type (DvP etc.) and settlement date, if any.")
    rate_specification: ForwardRef("RateSpecification") = Field(None, description="The specification of the rate value(s) applicable to the contract using either a floating rate calculation, a single fixed rate, a fixed rate schedule, or an inflation rate calculation.")
    day_count_fraction: ForwardRef("FieldWithMetaDayCountFractionEnum") = Field(None, description="The day count fraction. The cardinality has been relaxed when compared with the FpML interest rate swap for the purpose of accommodating standardized credit default swaps which DCF is not explicitly stated as part of the economic terms. The data rule InterestRatePayout_dayCountFraction requires that the DCF be stated for interest rate products.")
    calculation_period_dates: ForwardRef("CalculationPeriodDates") = Field(None, description="The parameters used to generate the calculation period dates schedule, including the specification of any initial or final stub calculation periods.")
    payment_dates: ForwardRef("PaymentDates") = Field(None, description="The payment date schedule, as defined by the parameters that are needed to specify it, either in a parametric way or by reference to another schedule of dates (e.g. the reset dates).")
    payment_date: ForwardRef("AdjustableDate") = Field(None, description="The payment date, where only one date is specified, as for the FRA product.")
    payment_delay: bool = Field(None, description="Applicable to CDS on MBS to specify whether payment delays are applicable to the fixed Amount. RMBS typically have a payment delay of 5 days between the coupon date of the reference obligation and the payment date of the synthetic swap. CMBS do not, on the other hand, with both payment dates being on the 25th of each month.")
    reset_dates: ForwardRef("ResetDates") = Field(None, description="The reset dates schedule, i.e. the dates on which the new observed index value is applied for each period and the interest rate hence begins to accrue.")
    discounting_method: ForwardRef("DiscountingMethod") = Field(None, description="The parameters specifying any discounting conventions that may apply. This element must only be included if discounting applies.")
    compounding_method: ForwardRef("CompoundingMethodEnum") = Field(None, description="If one or more calculation period contributes to a single payment amount this element specifies whether compounding is applicable and, if so, what compounding method is to be used. This element must only be included when more than one calculation period contributes to a single payment amount.")
    cashflow_representation: ForwardRef("CashflowRepresentation") = Field(None, description="The cashflow representation of the swap stream.")
    stub_period: ForwardRef("StubPeriod") = Field(None, description="The stub calculation period amount parameters. This element must only be included if there is an initial or final stub calculation period. Even then, it must only be included if either the stub references a different floating rate tenor to the regular calculation periods, or if the stub is calculated as a linear interpolation of two different floating rate tenors, or if a specific stub rate or stub amount has been negotiated.")
    bond_reference: ForwardRef("BondReference") = Field(None, description="Reference to a bond underlier to represent an asset swap or Condition Precedent Bond.")
    fixed_amount: str = Field(None, description="Fixed Amount Calculation")
    floating_amount: str = Field(None, description="Floating Amount Calculation")
    spread_calculation_method: ForwardRef("SpreadCalculationMethodEnum") = Field(None, description="Method by which spread is calculated. For example on an asset swap: 'ParPar' or 'Proceeds' may be the method indicated.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.metafields.field_with_meta_day_count_fraction_enum import FieldWithMetaDayCountFractionEnum
from src.models.cdm.generated.product.asset.bond_reference import BondReference
from src.models.cdm.generated.product.asset.cashflow_representation import CashflowRepresentation
from src.models.cdm.generated.product.asset.compounding_method_enum import CompoundingMethodEnum
from src.models.cdm.generated.product.asset.discounting_method import DiscountingMethod
from src.models.cdm.generated.product.asset.rate_specification import RateSpecification
from src.models.cdm.generated.product.asset.spread_calculation_method_enum import SpreadCalculationMethodEnum
from src.models.cdm.generated.product.common.schedule.calculation_period_dates import CalculationPeriodDates
from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
from src.models.cdm.generated.product.common.schedule.reset_dates import ResetDates
from src.models.cdm.generated.product.common.schedule.stub_period import StubPeriod
from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
InterestRatePayout.model_rebuild()
