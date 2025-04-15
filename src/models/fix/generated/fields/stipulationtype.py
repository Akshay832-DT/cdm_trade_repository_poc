"""
FIX StipulationType field (tag 233).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class StipulationTypeValues:
    """Enumerated values for StipulationType."""
    AMT = "AMT"  # ALTERNATIVE_MINIMUM_TAX
    AUTOREINV = "AUTOREINV"  # AUTO_REINVESTMENT
    BANKQUAL = "BANKQUAL"  # BANK_QUALIFIED
    BGNCON = "BGNCON"  # BARGAIN_CONDITIONS
    COUPON = "COUPON"  # COUPON_RANGE
    CURRENCY = "CURRENCY"  # ISO_CURRENCY_CODE
    CUSTOMDATE = "CUSTOMDATE"  # CUSTOM_START
    GEOG = "GEOG"  # GEOGRAPHICS
    HAIRCUT = "HAIRCUT"  # VALUATION_DISCOUNT
    INSURED = "INSURED"  # INSURED
    ISSUE = "ISSUE"  # ISSUE_DATE
    ISSUER = "ISSUER"  # ISSUER
    ISSUESIZE = "ISSUESIZE"  # ISSUE_SIZE_RANGE
    LOOKBACK = "LOOKBACK"  # LOOKBACK_DAYS
    LOT = "LOT"  # EXPLICIT_LOT_IDENTIFIER
    LOTVAR = "LOTVAR"  # LOT_VARIANCE
    MAT = "MAT"  # MATURITY_YEAR_AND_MONTH
    MATURITY = "MATURITY"  # MATURITY_RANGE
    MAXSUBS = "MAXSUBS"  # MAXIMUM_SUBSTITUTIONS
    MINQTY = "MINQTY"  # MINIMUM_QUANTITY
    MININCR = "MININCR"  # MINIMUM_INCREMENT
    MINDNOM = "MINDNOM"  # MINIMUM_DENOMINATION
    PAYFREQ = "PAYFREQ"  # PAYMENT_FREQUENCY
    PIECES = "PIECES"  # NUMBER_OF_PIECES
    PMAX = "PMAX"  # POOLS_MAXIMUM
    PPM = "PPM"  # POOLS_PER_MILLION
    PPL = "PPL"  # POOLS_PER_LOT
    PPT = "PPT"  # POOLS_PER_TRADE
    PRICE = "PRICE"  # PRICE_RANGE
    PRICEFREQ = "PRICEFREQ"  # PRICING_FREQUENCY
    PROD = "PROD"  # PRODUCTION_YEAR
    PROTECT = "PROTECT"  # CALL_PROTECTION
    PURPOSE = "PURPOSE"  # PURPOSE
    PXSOURCE = "PXSOURCE"  # BENCHMARK_PRICE_SOURCE
    RATING = "RATING"  # RATING_SOURCE_AND_RANGE
    REDEMPTION = "REDEMPTION"  # TYPE_OF_REDEMPTION
    RESTRICTED = "RESTRICTED"  # RESTRICTED
    SECTOR = "SECTOR"  # MARKET_SECTOR
    SECTYPE = "SECTYPE"  # SECURITY_TYPE_INCLUDED_OR_EXCLUDED
    STRUCT = "STRUCT"  # STRUCTURE
    SUBSFREQ = "SUBSFREQ"  # SUBSTITUTIONS_FREQUENCY
    SUBSLEFT = "SUBSLEFT"  # SUBSTITUTIONS_LEFT
    TEXT = "TEXT"  # FREEFORM_TEXT
    TRDVAR = "TRDVAR"  # TRADE_VARIANCE
    WAC = "WAC"  # WEIGHTED_AVERAGE_COUPON
    WAL = "WAL"  # WEIGHTED_AVERAGE_LIFE_COUPON
    WALA = "WALA"  # WEIGHTED_AVERAGE_LOAN_AGE
    WAM = "WAM"  # WEIGHTED_AVERAGE_MATURITY
    WHOLE = "WHOLE"  # WHOLE_POOL
    YIELD = "YIELD"  # YIELD_RANGE

class StipulationTypeField(FIXFieldBase):
    """"""
    tag: str = "233"
    name: str = "StipulationType"
    type: str = "STRING"
    value: Literal["AMT", "AUTOREINV", "BANKQUAL", "BGNCON", "COUPON", "CURRENCY", "CUSTOMDATE", "GEOG", "HAIRCUT", "INSURED", "ISSUE", "ISSUER", "ISSUESIZE", "LOOKBACK", "LOT", "LOTVAR", "MAT", "MATURITY", "MAXSUBS", "MINQTY", "MININCR", "MINDNOM", "PAYFREQ", "PIECES", "PMAX", "PPM", "PPL", "PPT", "PRICE", "PRICEFREQ", "PROD", "PROTECT", "PURPOSE", "PXSOURCE", "RATING", "REDEMPTION", "RESTRICTED", "SECTOR", "SECTYPE", "STRUCT", "SUBSFREQ", "SUBSLEFT", "TEXT", "TRDVAR", "WAC", "WAL", "WALA", "WAM", "WHOLE", "YIELD"]

    # Helper methods for enum values
    @property
    def is_amt(self) -> bool:
        return self.value == "AMT"
    @property
    def is_autoreinv(self) -> bool:
        return self.value == "AUTOREINV"
    @property
    def is_bankqual(self) -> bool:
        return self.value == "BANKQUAL"
    @property
    def is_bgncon(self) -> bool:
        return self.value == "BGNCON"
    @property
    def is_coupon(self) -> bool:
        return self.value == "COUPON"
    @property
    def is_currency(self) -> bool:
        return self.value == "CURRENCY"
    @property
    def is_customdate(self) -> bool:
        return self.value == "CUSTOMDATE"
    @property
    def is_geog(self) -> bool:
        return self.value == "GEOG"
    @property
    def is_haircut(self) -> bool:
        return self.value == "HAIRCUT"
    @property
    def is_insured(self) -> bool:
        return self.value == "INSURED"
    @property
    def is_issue(self) -> bool:
        return self.value == "ISSUE"
    @property
    def is_issuer(self) -> bool:
        return self.value == "ISSUER"
    @property
    def is_issuesize(self) -> bool:
        return self.value == "ISSUESIZE"
    @property
    def is_lookback(self) -> bool:
        return self.value == "LOOKBACK"
    @property
    def is_lot(self) -> bool:
        return self.value == "LOT"
    @property
    def is_lotvar(self) -> bool:
        return self.value == "LOTVAR"
    @property
    def is_mat(self) -> bool:
        return self.value == "MAT"
    @property
    def is_maturity(self) -> bool:
        return self.value == "MATURITY"
    @property
    def is_maxsubs(self) -> bool:
        return self.value == "MAXSUBS"
    @property
    def is_minqty(self) -> bool:
        return self.value == "MINQTY"
    @property
    def is_minincr(self) -> bool:
        return self.value == "MININCR"
    @property
    def is_mindnom(self) -> bool:
        return self.value == "MINDNOM"
    @property
    def is_payfreq(self) -> bool:
        return self.value == "PAYFREQ"
    @property
    def is_pieces(self) -> bool:
        return self.value == "PIECES"
    @property
    def is_pmax(self) -> bool:
        return self.value == "PMAX"
    @property
    def is_ppm(self) -> bool:
        return self.value == "PPM"
    @property
    def is_ppl(self) -> bool:
        return self.value == "PPL"
    @property
    def is_ppt(self) -> bool:
        return self.value == "PPT"
    @property
    def is_price(self) -> bool:
        return self.value == "PRICE"
    @property
    def is_pricefreq(self) -> bool:
        return self.value == "PRICEFREQ"
    @property
    def is_prod(self) -> bool:
        return self.value == "PROD"
    @property
    def is_protect(self) -> bool:
        return self.value == "PROTECT"
    @property
    def is_purpose(self) -> bool:
        return self.value == "PURPOSE"
    @property
    def is_pxsource(self) -> bool:
        return self.value == "PXSOURCE"
    @property
    def is_rating(self) -> bool:
        return self.value == "RATING"
    @property
    def is_redemption(self) -> bool:
        return self.value == "REDEMPTION"
    @property
    def is_restricted(self) -> bool:
        return self.value == "RESTRICTED"
    @property
    def is_sector(self) -> bool:
        return self.value == "SECTOR"
    @property
    def is_sectype(self) -> bool:
        return self.value == "SECTYPE"
    @property
    def is_struct(self) -> bool:
        return self.value == "STRUCT"
    @property
    def is_subsfreq(self) -> bool:
        return self.value == "SUBSFREQ"
    @property
    def is_subsleft(self) -> bool:
        return self.value == "SUBSLEFT"
    @property
    def is_text(self) -> bool:
        return self.value == "TEXT"
    @property
    def is_trdvar(self) -> bool:
        return self.value == "TRDVAR"
    @property
    def is_wac(self) -> bool:
        return self.value == "WAC"
    @property
    def is_wal(self) -> bool:
        return self.value == "WAL"
    @property
    def is_wala(self) -> bool:
        return self.value == "WALA"
    @property
    def is_wam(self) -> bool:
        return self.value == "WAM"
    @property
    def is_whole(self) -> bool:
        return self.value == "WHOLE"
    @property
    def is_yield(self) -> bool:
        return self.value == "YIELD"
