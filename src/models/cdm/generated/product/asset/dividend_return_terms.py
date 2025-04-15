from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
    from src.models.cdm.generated.product.asset.dividend_amount_type_enum import DividendAmountTypeEnum
    from src.models.cdm.generated.product.asset.dividend_composition_enum import DividendCompositionEnum
    from src.models.cdm.generated.product.asset.dividend_currency import DividendCurrency
    from src.models.cdm.generated.product.asset.dividend_entitlement_enum import DividendEntitlementEnum
    from src.models.cdm.generated.product.asset.dividend_payout_ratio import DividendPayoutRatio
    from src.models.cdm.generated.product.asset.dividend_period import DividendPeriod
    from src.models.cdm.generated.product.asset.dividend_period_enum import DividendPeriodEnum
    from src.models.cdm.generated.product.asset.non_cash_dividend_treatment_enum import NonCashDividendTreatmentEnum

class DividendReturnTerms(CdmModelBase):
    """A class describing the conditions governing the payment of dividends to the receiver of the equity return, with the exception of the dividend payout ratio, which is defined for each of the underlying components."""
    dividend_payout_ratio: List[ForwardRef("DividendPayoutRatio")] = Field(None, description="Specifies the dividend payout ratio associated with each underlier. In FpML 5.10 the payout is positioned at the underlier level, although there is an intent to reconsider this approach and position it at the leg level. This is approach adopted by the CDM.")
    dividend_reinvestment: bool = Field(None, description="Boolean element that defines whether the dividend will be reinvested or not.")
    dividend_entitlement: ForwardRef("DividendEntitlementEnum") = Field(None, description="Defines the date on which the receiver of the equity return is entitled to the dividend.")
    dividend_amount_type: ForwardRef("DividendAmountTypeEnum") = Field(None, description="Specifies whether the dividend is paid with respect to the Dividend Period.")
    performance: str = Field(None, description="Performance calculation, in accordance with Part 1 Section 12 of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap, Para 75. 'Equity Performance'. Cumulative performance is used as a notional multiplier factor on both legs of an Equity Swap.")
    first_or_second_period: ForwardRef("DividendPeriodEnum") = Field(None, description="2002 ISDA Equity Derivatives Definitions: Dividend Period as either the First Period or the Second Period. | ")
    extraordinary_dividends_party: ForwardRef("AncillaryRoleEnum") = Field(None, description="Specifies the party which determines if dividends are extraordinary in relation to normal levels.")
    excess_dividend_amount: ForwardRef("DividendAmountTypeEnum") = Field(None, description="Determination of Gross Cash Dividend per Share.")
    dividend_currency: ForwardRef("DividendCurrency") = Field(None, description="Specifies the currency in which the dividend will be denominated, e.g. the dividend currency, or a specified currency. This class is not specified as such in FpML, which makes use of the CurrencyAndDeterminationMethod.model to specify such terms.")
    non_cash_dividend_treatment: ForwardRef("NonCashDividendTreatmentEnum") = Field(None, description="Specifies the treatment of Non-Cash Dividends.")
    dividend_composition: ForwardRef("DividendCompositionEnum") = Field(None, description="Specifies how the composition of Dividends is to be determined.")
    special_dividends: bool = Field(None, description="Specifies the method according to which special dividends are determined.")
    material_dividend: bool = Field(None, description="If present and true, then material non cash dividends are applicable.")
    dividend_period: List[ForwardRef("DividendPeriod")] = Field(None, description="One to many time bounded dividend payment periods, each with a dividend payment date per period.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
from src.models.cdm.generated.product.asset.dividend_amount_type_enum import DividendAmountTypeEnum
from src.models.cdm.generated.product.asset.dividend_composition_enum import DividendCompositionEnum
from src.models.cdm.generated.product.asset.dividend_currency import DividendCurrency
from src.models.cdm.generated.product.asset.dividend_entitlement_enum import DividendEntitlementEnum
from src.models.cdm.generated.product.asset.dividend_payout_ratio import DividendPayoutRatio
from src.models.cdm.generated.product.asset.dividend_period import DividendPeriod
from src.models.cdm.generated.product.asset.dividend_period_enum import DividendPeriodEnum
from src.models.cdm.generated.product.asset.non_cash_dividend_treatment_enum import NonCashDividendTreatmentEnum
DividendReturnTerms.model_rebuild()
