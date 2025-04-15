from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.commodity_payout import CommodityPayout
    from src.models.cdm.generated.product.asset.credit_default_payout import CreditDefaultPayout
    from src.models.cdm.generated.product.asset.interest_rate_payout import InterestRatePayout
    from src.models.cdm.generated.product.template.asset_payout import AssetPayout
    from src.models.cdm.generated.product.template.fixed_price_payout import FixedPricePayout
    from src.models.cdm.generated.product.template.option_payout import OptionPayout
    from src.models.cdm.generated.product.template.performance_payout import PerformancePayout
    from src.models.cdm.generated.product.template.settlement_payout import SettlementPayout

class Payout(CdmModelBase):
    """Represents the set of future cashflow methodologies in the form of specific payout data type(s) which result from the financial product.  Examples: a trade in a cash asset will use only a settlement payout; for derivatives, two interest rate payouts can be combined to specify an interest rate swap; one interest rate payout can be combined with a credit default payout to specify a credit default swap."""
    asset_payout: Optional[Dict[str, Any]] = Field(None, description="Defines the assets and movements in a security financing transaction.")
    commodity_payout: Optional[Dict[str, Any]] = Field(None, description="Defines the payout for the floating leg of a Commodity Swap.")
    credit_default_payout: Optional[Dict[str, Any]] = Field(None, description="The credit default payout, which provides the details necessary for determining when a credit payout will be triggered as well as the parameters for calculating the payout and the settlement terms.")
    fixed_price_payout: Optional[Dict[str, Any]] = Field(None, description="Defines a payout in which one or more payouts are defined as a fixed price.")
    interest_rate_payout: Optional[Dict[str, Any]] = Field(None, description="All of the terms necessary to define and calculate a cash flow based on a fixed, a floating or an inflation index rate. The interest rate payout can be applied to interest rate swaps and FRA (which both have two associated interest rate payouts), credit default swaps (to represent the fee leg when subject to periodic payments) and equity swaps (to represent the funding leg).")
    option_payout: Optional[Dict[str, Any]] = Field(None, description="The option payout.")
    performance_payout: Optional[Dict[str, Any]] = Field(None, description="The performance payout, which encompasses the equity price returns, dividend returns, volatility return, variance return and correlation provisions.")
    settlement_payout: Optional[Dict[str, Any]] = Field(None, description="Represents a forward settling payout. The 'Underlier' attribute captures the underlying payout, which is settled according to the 'SettlementTerms' attribute. Both FX Spot and FX Forward should use this component.")

    @model_validator(mode='after')
    def validate_types(cls, values):
        from src.models.cdm.generated.product.asset.commodity_payout import CommodityPayout
        from src.models.cdm.generated.product.asset.credit_default_payout import CreditDefaultPayout
        from src.models.cdm.generated.product.asset.interest_rate_payout import InterestRatePayout
        from src.models.cdm.generated.product.template.asset_payout import AssetPayout
        from src.models.cdm.generated.product.template.fixed_price_payout import FixedPricePayout
        from src.models.cdm.generated.product.template.option_payout import OptionPayout
        from src.models.cdm.generated.product.template.performance_payout import PerformancePayout
        from src.models.cdm.generated.product.template.settlement_payout import SettlementPayout

        if values.asset_payout is not None:
            try:
                values.asset_payout = AssetPayout(**values.asset_payout)
            except Exception as e:
                raise ValueError(f"asset_payout must be a valid AssetPayout: {str(e)}")
        if values.commodity_payout is not None:
            try:
                values.commodity_payout = CommodityPayout(**values.commodity_payout)
            except Exception as e:
                raise ValueError(f"commodity_payout must be a valid CommodityPayout: {str(e)}")
        if values.credit_default_payout is not None:
            try:
                values.credit_default_payout = CreditDefaultPayout(**values.credit_default_payout)
            except Exception as e:
                raise ValueError(f"credit_default_payout must be a valid CreditDefaultPayout: {str(e)}")
        if values.fixed_price_payout is not None:
            try:
                values.fixed_price_payout = FixedPricePayout(**values.fixed_price_payout)
            except Exception as e:
                raise ValueError(f"fixed_price_payout must be a valid FixedPricePayout: {str(e)}")
        if values.interest_rate_payout is not None:
            try:
                values.interest_rate_payout = InterestRatePayout(**values.interest_rate_payout)
            except Exception as e:
                raise ValueError(f"interest_rate_payout must be a valid InterestRatePayout: {str(e)}")
        if values.option_payout is not None:
            try:
                values.option_payout = OptionPayout(**values.option_payout)
            except Exception as e:
                raise ValueError(f"option_payout must be a valid OptionPayout: {str(e)}")
        if values.performance_payout is not None:
            try:
                values.performance_payout = PerformancePayout(**values.performance_payout)
            except Exception as e:
                raise ValueError(f"performance_payout must be a valid PerformancePayout: {str(e)}")
        if values.settlement_payout is not None:
            try:
                values.settlement_payout = SettlementPayout(**values.settlement_payout)
            except Exception as e:
                raise ValueError(f"settlement_payout must be a valid SettlementPayout: {str(e)}")
        return values

Payout.model_rebuild()
