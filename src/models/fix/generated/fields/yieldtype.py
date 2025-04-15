"""
FIX YieldType field (tag 235).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class YieldTypeValues:
    """Enumerated values for YieldType."""
    AFTERTAX = "AFTERTAX"  # AFTER_TAX_YIELD
    ANNUAL = "ANNUAL"  # ANNUAL_YIELD
    ATISSUE = "ATISSUE"  # YIELD_AT_ISSUE
    AVGMATURITY = "AVGMATURITY"  # YIELD_TO_AVERAGE_MATURITY
    BOOK = "BOOK"  # BOOK_YIELD
    CALL = "CALL"  # YIELD_TO_NEXT_CALL
    CHANGE = "CHANGE"  # YIELD_CHANGE_SINCE_CLOSE
    CLOSE = "CLOSE"  # CLOSING_YIELD
    COMPOUND = "COMPOUND"  # COMPOUND_YIELD
    CURRENT = "CURRENT"  # CURRENT_YIELD
    GROSS = "GROSS"  # TRUE_GROSS_YIELD
    GOVTEQUIV = "GOVTEQUIV"  # GVNT_EQUIVALENT_YIELD
    INFLATION = "INFLATION"  # YIELD_WITH_INFLATION_ASSUMPTION
    INVERSEFLOATER = "INVERSEFLOATER"  # INVERSE_FLOATER_BOND_YIELD
    LASTCLOSE = "LASTCLOSE"  # MOST_RECENT_CLOSING_YIELD
    LASTMONTH = "LASTMONTH"  # CLOSING_YIELD_MOST_RECENT_MONTH
    LASTQUARTER = "LASTQUARTER"  # CLOSING_YIELD_MOST_RECENT_QUARTER
    LASTYEAR = "LASTYEAR"  # CLOSING_YIELD_MOST_RECENT_YEAR
    LONGAVGLIFE = "LONGAVGLIFE"  # YIELD_TO_LONGEST_AVERAGE_LIFE
    MARK = "MARK"  # MARK_TO_MARKET_YIELD
    MATURITY = "MATURITY"  # YIELD_TO_MATURITY
    NEXTREFUND = "NEXTREFUND"  # YIELD_TO_NEXT_REFUND
    OPENAVG = "OPENAVG"  # OPEN_AVERAGE_YIELD
    PUT = "PUT"  # YIELD_TO_NEXT_PUT
    PREVCLOSE = "PREVCLOSE"  # PREVIOUS_CLOSE_YIELD
    PROCEEDS = "PROCEEDS"  # PROCEEDS_YIELD
    SEMIANNUAL = "SEMIANNUAL"  # SEMI_ANNUAL_YIELD
    SHORTAVGLIFE = "SHORTAVGLIFE"  # YIELD_TO_SHORTEST_AVERAGE_LIFE
    SIMPLE = "SIMPLE"  # SIMPLE_YIELD
    TAXEQUIV = "TAXEQUIV"  # TAX_EQUIVALENT_YIELD
    TENDER = "TENDER"  # YIELD_TO_TENDER_DATE
    TRUE = "TRUE"  # TRUE_YIELD
    VALUE1_32 = "VALUE1/32"  # YIELD_VALUE_OF132
    WORST = "WORST"  # YIELD_TO_WORST

class YieldTypeField(FIXFieldBase):
    """"""
    tag: str = "235"
    name: str = "YieldType"
    type: str = "STRING"
    value: Literal["AFTERTAX", "ANNUAL", "ATISSUE", "AVGMATURITY", "BOOK", "CALL", "CHANGE", "CLOSE", "COMPOUND", "CURRENT", "GROSS", "GOVTEQUIV", "INFLATION", "INVERSEFLOATER", "LASTCLOSE", "LASTMONTH", "LASTQUARTER", "LASTYEAR", "LONGAVGLIFE", "MARK", "MATURITY", "NEXTREFUND", "OPENAVG", "PUT", "PREVCLOSE", "PROCEEDS", "SEMIANNUAL", "SHORTAVGLIFE", "SIMPLE", "TAXEQUIV", "TENDER", "TRUE", "VALUE1/32", "WORST"]

    # Helper methods for enum values
    @property
    def is_aftertax(self) -> bool:
        return self.value == "AFTERTAX"
    @property
    def is_annual(self) -> bool:
        return self.value == "ANNUAL"
    @property
    def is_atissue(self) -> bool:
        return self.value == "ATISSUE"
    @property
    def is_avgmaturity(self) -> bool:
        return self.value == "AVGMATURITY"
    @property
    def is_book(self) -> bool:
        return self.value == "BOOK"
    @property
    def is_call(self) -> bool:
        return self.value == "CALL"
    @property
    def is_change(self) -> bool:
        return self.value == "CHANGE"
    @property
    def is_close(self) -> bool:
        return self.value == "CLOSE"
    @property
    def is_compound(self) -> bool:
        return self.value == "COMPOUND"
    @property
    def is_current(self) -> bool:
        return self.value == "CURRENT"
    @property
    def is_gross(self) -> bool:
        return self.value == "GROSS"
    @property
    def is_govtequiv(self) -> bool:
        return self.value == "GOVTEQUIV"
    @property
    def is_inflation(self) -> bool:
        return self.value == "INFLATION"
    @property
    def is_inversefloater(self) -> bool:
        return self.value == "INVERSEFLOATER"
    @property
    def is_lastclose(self) -> bool:
        return self.value == "LASTCLOSE"
    @property
    def is_lastmonth(self) -> bool:
        return self.value == "LASTMONTH"
    @property
    def is_lastquarter(self) -> bool:
        return self.value == "LASTQUARTER"
    @property
    def is_lastyear(self) -> bool:
        return self.value == "LASTYEAR"
    @property
    def is_longavglife(self) -> bool:
        return self.value == "LONGAVGLIFE"
    @property
    def is_mark(self) -> bool:
        return self.value == "MARK"
    @property
    def is_maturity(self) -> bool:
        return self.value == "MATURITY"
    @property
    def is_nextrefund(self) -> bool:
        return self.value == "NEXTREFUND"
    @property
    def is_openavg(self) -> bool:
        return self.value == "OPENAVG"
    @property
    def is_put(self) -> bool:
        return self.value == "PUT"
    @property
    def is_prevclose(self) -> bool:
        return self.value == "PREVCLOSE"
    @property
    def is_proceeds(self) -> bool:
        return self.value == "PROCEEDS"
    @property
    def is_semiannual(self) -> bool:
        return self.value == "SEMIANNUAL"
    @property
    def is_shortavglife(self) -> bool:
        return self.value == "SHORTAVGLIFE"
    @property
    def is_simple(self) -> bool:
        return self.value == "SIMPLE"
    @property
    def is_taxequiv(self) -> bool:
        return self.value == "TAXEQUIV"
    @property
    def is_tender(self) -> bool:
        return self.value == "TENDER"
    @property
    def is_true(self) -> bool:
        return self.value == "TRUE"
    @property
    def is_value1_32(self) -> bool:
        return self.value == "VALUE1/32"
    @property
    def is_worst(self) -> bool:
        return self.value == "WORST"
