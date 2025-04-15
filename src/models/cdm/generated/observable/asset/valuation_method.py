from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.cash_collateral_valuation_method import CashCollateralValuationMethod
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.observable.asset.quotation_rate_type_enum import QuotationRateTypeEnum
    from src.models.cdm.generated.observable.asset.valuation_method_enum import ValuationMethodEnum
    from src.models.cdm.generated.observable.asset.valuation_source import ValuationSource

class ValuationMethod(CdmModelBase):
    """Specifies the parameters required to obtain a valuation, including the source, quotation method (bid, mid etc.) and any applicable quotation amount."""
    valuation_source: ForwardRef("ValuationSource") = Field(description="The source for obtaining a valuation. This may come from some information source (e.g. Reuters), from a rate option fixing (e.g. FX fixing for cross-currency settlement), or from a set of reference banks. This is a mandatory attribute as the valuation method relies on one of those sources to be specified.")
    quotation_method: ForwardRef("QuotationRateTypeEnum") = Field(None, description="The type of price quotations to be requested from dealers when determining the market value of the reference obligation for purposes of cash settlement, or which rate quote is to be observed for a fixing. For example, Bid, Offer, Mid-market or Exercising Party Pays. ISDA 2003 Term: Quotation Method. The meaning of Exercising Party Pays is defined in the 2000 ISDA Definitions, Section 17.2. Certain Definitions Relating to Cash Settlement, paragraph (j).")
    valuation_method: ForwardRef("ValuationMethodEnum") = Field(None, description="The ISDA defined methodology for determining the final price of the reference obligation for purposes of cash settlement. (ISDA 2003 Term: Valuation Method). For example, Market, Highest etc.")
    quotation_amount: ForwardRef("Money") = Field(None, description="In the determination of a cash settlement amount, if weighted average quotations are to be obtained, the quotation amount specifies an upper limit to the outstanding principal balance of the reference obligation for which the quote should be obtained. If not specified, the ISDA definitions provide for a fallback amount equal to the floating rate payer calculation amount. ISDA 2003 Term: Quotation Amount.")
    minimum_quotation_amount: ForwardRef("Money") = Field(None, description="In the determination of a cash settlement amount, if weighted average quotations are to be obtained, the minimum quotation amount specifies a minimum intended threshold amount of outstanding principal balance of the reference obligation for which the quote should be obtained. If not specified, the ISDA definitions provide for a fallback amount of the lower of either USD 1,000,000 (or its equivalent in the relevant obligation currency) or the quotation amount. ISDA 2003 Term: Minimum Quotation Amount.")
    cash_collateral_valuation_method: ForwardRef("CashCollateralValuationMethod") = Field(None, description="Specifies the parameters representing several mid-market valuation and replacement value methods.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.cash_collateral_valuation_method import CashCollateralValuationMethod
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.observable.asset.quotation_rate_type_enum import QuotationRateTypeEnum
from src.models.cdm.generated.observable.asset.valuation_method_enum import ValuationMethodEnum
from src.models.cdm.generated.observable.asset.valuation_source import ValuationSource
ValuationMethod.model_rebuild()
