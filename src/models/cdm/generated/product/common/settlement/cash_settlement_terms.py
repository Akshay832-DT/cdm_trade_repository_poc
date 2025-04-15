from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.observable.asset.valuation_method import ValuationMethod
    from src.models.cdm.generated.product.common.settlement.cash_settlement_method_enum import CashSettlementMethodEnum
    from src.models.cdm.generated.product.common.settlement.valuation_date import ValuationDate

class CashSettlementTerms(CdmModelBase):
    """Defines the terms required to compute and settle a cash settlement amount according to a fixing value, including the fixing source, fixing method and fixing date. In FpML, PhysicalSettlementTerms and CashSettlementTerms extend SettlementTerms. In the CDM, this extension paradigm has not been used because SettlementTerms class has been used for purposes related to securities transactions, while it is not used as such in the FpML standard (i.e. only as an abstract construct."""
    cash_settlement_method: ForwardRef("CashSettlementMethodEnum") = Field(None, description="Specifies the type of cash settlement method: cash price, yield curve etc.")
    valuation_method: ForwardRef("ValuationMethod") = Field(None, description="Specifies the parameters required to obtain a valuation, including the source, quotation method (bid, mid etc.) and any applicable quotation amount.")
    valuation_date: ForwardRef("ValuationDate") = Field(None, description="Defines the different methods to specify a valuation date, as used for cash settlement. The Single / Multiple ValuationDate is used for the determination of recovery in a credit event, the RelativeDateOffset is used for cash-settled option, and FxFixingDate is used for cross-currency settlement.")
    valuation_time: ForwardRef("BusinessCenterTime") = Field(None, description="The time of the cash settlement valuation date when the cash settlement amount will be determined according to the cash settlement method, if the parties have not otherwise been able to agree the cash settlement amount. When using quations, this is the time of day in the specified business center when the calculation agent seeks quotations for an amount of the reference obligation for purposes of cash settlement. ISDA 2003 Term: Valuation Time.")
    cash_settlement_amount: ForwardRef("Money") = Field(None, description="The amount paid by the seller to the buyer for cash settlement on the cash settlement date. If not otherwise specified, would typically be calculated as 100 (or the Reference Price) minus the price of the Reference Obligation (all expressed as a percentage) times Floating Rate Payer Calculation Amount. ISDA 2003 Term: Cash Settlement Amount.")
    recovery_factor: float = Field(None, description="Used for fixed recovery, specifies the recovery level, determined at contract formation, to be applied on a default. Used to calculate the amount paid by the seller to the buyer for cash settlement on the cash settlement date. Amount calculation is (1 minus the Recovery Factor) multiplied by the Floating Rate Payer Calculation Amount. The currency will be derived from the Floating Rate Payer Calculation Amount.")
    fixed_settlement: bool = Field(None, description="Used for Recovery Lock, to indicate whether fixed Settlement is Applicable or Not Applicable. If Buyer fails to deliver an effective Notice of Physical Settlement on or before the Buyer NOPS Cut-off Date, and if Seller fails to deliver an effective Seller NOPS on or before the Seller NOPS Cut-off Date, then either: (a) if Fixed Settlement is specified in the related Confirmation as not applicable, then the Seller NOPS Cut-off Date shall be the Termination Date; or (b) if Fixed Settlement is specified in the related Confirmation as applicable, then: (i) if the Fixed Settlement Amount is a positive number, Seller shall, subject to Section 3.1 (except for the requirement of satisfaction of the Notice of Physical Settlement Condition to Settlement), pay the Fixed Settlement Amount to Buyer on the Fixed Settlement Payment Date; and (ii) if the Fixed Settlement Amount is a negative number, Buyer shall, subject to Section 3.1 (except for the requirement of satisfaction of the Notice of Physical Settlement Condition to Settlement), pay the absolute value of the Fixed Settlement Amount to Seller on the Fixed Settlement Payment Date.")
    accrued_interest: bool = Field(None, description="Indicates whether accrued interest is included (true) or not (false). For cash settlement this specifies whether quotations should be obtained inclusive or not of accrued interest. For physical settlement this specifies whether the buyer should deliver the obligation with an outstanding principal balance that includes or excludes accrued interest. ISDA 2003 Term: Include/Exclude Accrued Interest.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.observable.asset.valuation_method import ValuationMethod
from src.models.cdm.generated.product.common.settlement.cash_settlement_method_enum import CashSettlementMethodEnum
from src.models.cdm.generated.product.common.settlement.valuation_date import ValuationDate
CashSettlementTerms.model_rebuild()
