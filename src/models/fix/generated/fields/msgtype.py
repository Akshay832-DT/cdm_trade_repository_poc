"""
FIX MsgType field (tag 35).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MsgTypeValues:
    """Enumerated values for MsgType."""
    VALUE_0 = "0"  # HEARTBEAT
    VALUE_1 = "1"  # TEST_REQUEST
    VALUE_2 = "2"  # RESEND_REQUEST
    VALUE_3 = "3"  # REJECT
    VALUE_4 = "4"  # SEQUENCE_RESET
    VALUE_5 = "5"  # LOGOUT
    VALUE_6 = "6"  # IOI
    VALUE_7 = "7"  # ADVERTISEMENT
    VALUE_8 = "8"  # EXECUTION_REPORT
    VALUE_9 = "9"  # ORDER_CANCEL_REJECT
    A = "A"  # LOGON
    B = "B"  # NEWS
    C = "C"  # EMAIL
    D = "D"  # NEW_ORDER_SINGLE
    E = "E"  # NEW_ORDER_LIST
    F = "F"  # ORDER_CANCEL_REQUEST
    G = "G"  # ORDER_CANCEL_REPLACE_REQUEST
    H = "H"  # ORDER_STATUS_REQUEST
    J = "J"  # ALLOCATION_INSTRUCTION
    K = "K"  # LIST_CANCEL_REQUEST
    L = "L"  # LIST_EXECUTE
    M = "M"  # LIST_STATUS_REQUEST
    N = "N"  # LIST_STATUS
    P = "P"  # ALLOCATION_INSTRUCTION_ACK
    Q = "Q"  # DONT_KNOW_TRADE
    R = "R"  # QUOTE_REQUEST
    S = "S"  # QUOTE
    T = "T"  # SETTLEMENT_INSTRUCTIONS
    V = "V"  # MARKET_DATA_REQUEST
    W = "W"  # MARKET_DATA_SNAPSHOT_FULL_REFRESH
    X = "X"  # MARKET_DATA_INCREMENTAL_REFRESH
    Y = "Y"  # MARKET_DATA_REQUEST_REJECT
    Z = "Z"  # QUOTE_CANCEL
    a = "a"  # QUOTE_STATUS_REQUEST
    b = "b"  # MASS_QUOTE_ACKNOWLEDGEMENT
    c = "c"  # SECURITY_DEFINITION_REQUEST
    d = "d"  # SECURITY_DEFINITION
    e = "e"  # SECURITY_STATUS_REQUEST
    f = "f"  # SECURITY_STATUS
    g = "g"  # TRADING_SESSION_STATUS_REQUEST
    h = "h"  # TRADING_SESSION_STATUS
    i = "i"  # MASS_QUOTE
    j = "j"  # BUSINESS_MESSAGE_REJECT
    k = "k"  # BID_REQUEST
    l = "l"  # BID_RESPONSE
    m = "m"  # LIST_STRIKE_PRICE
    n = "n"  # XML_NON_FIX
    o = "o"  # REGISTRATION_INSTRUCTIONS
    p = "p"  # REGISTRATION_INSTRUCTIONS_RESPONSE
    q = "q"  # ORDER_MASS_CANCEL_REQUEST
    r = "r"  # ORDER_MASS_CANCEL_REPORT
    s = "s"  # NEW_ORDER_CROSS
    t = "t"  # CROSS_ORDER_CANCEL_REPLACE_REQUEST
    u = "u"  # CROSS_ORDER_CANCEL_REQUEST
    v = "v"  # SECURITY_TYPE_REQUEST
    w = "w"  # SECURITY_TYPES
    x = "x"  # SECURITY_LIST_REQUEST
    y = "y"  # SECURITY_LIST
    z = "z"  # DERIVATIVE_SECURITY_LIST_REQUEST
    AA = "AA"  # DERIVATIVE_SECURITY_LIST
    AB = "AB"  # NEW_ORDER_MULTILEG
    AC = "AC"  # MULTILEG_ORDER_CANCEL_REPLACE
    AD = "AD"  # TRADE_CAPTURE_REPORT_REQUEST
    AE = "AE"  # TRADE_CAPTURE_REPORT
    AF = "AF"  # ORDER_MASS_STATUS_REQUEST
    AG = "AG"  # QUOTE_REQUEST_REJECT
    AH = "AH"  # RFQ_REQUEST
    AI = "AI"  # QUOTE_STATUS_REPORT
    AJ = "AJ"  # QUOTE_RESPONSE
    AK = "AK"  # CONFIRMATION
    AL = "AL"  # POSITION_MAINTENANCE_REQUEST
    AM = "AM"  # POSITION_MAINTENANCE_REPORT
    AN = "AN"  # REQUEST_FOR_POSITIONS
    AO = "AO"  # REQUEST_FOR_POSITIONS_ACK
    AP = "AP"  # POSITION_REPORT
    AQ = "AQ"  # TRADE_CAPTURE_REPORT_REQUEST_ACK
    AR = "AR"  # TRADE_CAPTURE_REPORT_ACK
    AS = "AS"  # ALLOCATION_REPORT
    AT = "AT"  # ALLOCATION_REPORT_ACK
    AU = "AU"  # CONFIRMATION_ACK
    AV = "AV"  # SETTLEMENT_INSTRUCTION_REQUEST
    AW = "AW"  # ASSIGNMENT_REPORT
    AX = "AX"  # COLLATERAL_REQUEST
    AY = "AY"  # COLLATERAL_ASSIGNMENT
    AZ = "AZ"  # COLLATERAL_RESPONSE
    BA = "BA"  # COLLATERAL_REPORT
    BB = "BB"  # COLLATERAL_INQUIRY
    BC = "BC"  # NETWORK_COUNTERPARTY_SYSTEM_STATUS_REQUEST
    BD = "BD"  # NETWORK_COUNTERPARTY_SYSTEM_STATUS_RESPONSE
    BE = "BE"  # USER_REQUEST
    BF = "BF"  # USER_RESPONSE
    BG = "BG"  # COLLATERAL_INQUIRY_ACK
    BH = "BH"  # CONFIRMATION_REQUEST

class MsgTypeField(FIXFieldBase):
    """"""
    tag: str = "35"
    name: str = "MsgType"
    type: str = "STRING"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ", "AR", "AS", "AT", "AU", "AV", "AW", "AX", "AY", "AZ", "BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_3(self) -> bool:
        return self.value == "3"
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
    @property
    def is_value_6(self) -> bool:
        return self.value == "6"
    @property
    def is_value_7(self) -> bool:
        return self.value == "7"
    @property
    def is_value_8(self) -> bool:
        return self.value == "8"
    @property
    def is_value_9(self) -> bool:
        return self.value == "9"
    @property
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_b(self) -> bool:
        return self.value == "B"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
    @property
    def is_d(self) -> bool:
        return self.value == "D"
    @property
    def is_e(self) -> bool:
        return self.value == "E"
    @property
    def is_f(self) -> bool:
        return self.value == "F"
    @property
    def is_g(self) -> bool:
        return self.value == "G"
    @property
    def is_h(self) -> bool:
        return self.value == "H"
    @property
    def is_j(self) -> bool:
        return self.value == "J"
    @property
    def is_k(self) -> bool:
        return self.value == "K"
    @property
    def is_l(self) -> bool:
        return self.value == "L"
    @property
    def is_m(self) -> bool:
        return self.value == "M"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
    @property
    def is_p(self) -> bool:
        return self.value == "P"
    @property
    def is_q(self) -> bool:
        return self.value == "Q"
    @property
    def is_r(self) -> bool:
        return self.value == "R"
    @property
    def is_s(self) -> bool:
        return self.value == "S"
    @property
    def is_t(self) -> bool:
        return self.value == "T"
    @property
    def is_v(self) -> bool:
        return self.value == "V"
    @property
    def is_w(self) -> bool:
        return self.value == "W"
    @property
    def is_x(self) -> bool:
        return self.value == "X"
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_z(self) -> bool:
        return self.value == "Z"
    @property
    def is_a(self) -> bool:
        return self.value == "a"
    @property
    def is_b(self) -> bool:
        return self.value == "b"
    @property
    def is_c(self) -> bool:
        return self.value == "c"
    @property
    def is_d(self) -> bool:
        return self.value == "d"
    @property
    def is_e(self) -> bool:
        return self.value == "e"
    @property
    def is_f(self) -> bool:
        return self.value == "f"
    @property
    def is_g(self) -> bool:
        return self.value == "g"
    @property
    def is_h(self) -> bool:
        return self.value == "h"
    @property
    def is_i(self) -> bool:
        return self.value == "i"
    @property
    def is_j(self) -> bool:
        return self.value == "j"
    @property
    def is_k(self) -> bool:
        return self.value == "k"
    @property
    def is_l(self) -> bool:
        return self.value == "l"
    @property
    def is_m(self) -> bool:
        return self.value == "m"
    @property
    def is_n(self) -> bool:
        return self.value == "n"
    @property
    def is_o(self) -> bool:
        return self.value == "o"
    @property
    def is_p(self) -> bool:
        return self.value == "p"
    @property
    def is_q(self) -> bool:
        return self.value == "q"
    @property
    def is_r(self) -> bool:
        return self.value == "r"
    @property
    def is_s(self) -> bool:
        return self.value == "s"
    @property
    def is_t(self) -> bool:
        return self.value == "t"
    @property
    def is_u(self) -> bool:
        return self.value == "u"
    @property
    def is_v(self) -> bool:
        return self.value == "v"
    @property
    def is_w(self) -> bool:
        return self.value == "w"
    @property
    def is_x(self) -> bool:
        return self.value == "x"
    @property
    def is_y(self) -> bool:
        return self.value == "y"
    @property
    def is_z(self) -> bool:
        return self.value == "z"
    @property
    def is_aa(self) -> bool:
        return self.value == "AA"
    @property
    def is_ab(self) -> bool:
        return self.value == "AB"
    @property
    def is_ac(self) -> bool:
        return self.value == "AC"
    @property
    def is_ad(self) -> bool:
        return self.value == "AD"
    @property
    def is_ae(self) -> bool:
        return self.value == "AE"
    @property
    def is_af(self) -> bool:
        return self.value == "AF"
    @property
    def is_ag(self) -> bool:
        return self.value == "AG"
    @property
    def is_ah(self) -> bool:
        return self.value == "AH"
    @property
    def is_ai(self) -> bool:
        return self.value == "AI"
    @property
    def is_aj(self) -> bool:
        return self.value == "AJ"
    @property
    def is_ak(self) -> bool:
        return self.value == "AK"
    @property
    def is_al(self) -> bool:
        return self.value == "AL"
    @property
    def is_am(self) -> bool:
        return self.value == "AM"
    @property
    def is_an(self) -> bool:
        return self.value == "AN"
    @property
    def is_ao(self) -> bool:
        return self.value == "AO"
    @property
    def is_ap(self) -> bool:
        return self.value == "AP"
    @property
    def is_aq(self) -> bool:
        return self.value == "AQ"
    @property
    def is_ar(self) -> bool:
        return self.value == "AR"
    @property
    def is_as(self) -> bool:
        return self.value == "AS"
    @property
    def is_at(self) -> bool:
        return self.value == "AT"
    @property
    def is_au(self) -> bool:
        return self.value == "AU"
    @property
    def is_av(self) -> bool:
        return self.value == "AV"
    @property
    def is_aw(self) -> bool:
        return self.value == "AW"
    @property
    def is_ax(self) -> bool:
        return self.value == "AX"
    @property
    def is_ay(self) -> bool:
        return self.value == "AY"
    @property
    def is_az(self) -> bool:
        return self.value == "AZ"
    @property
    def is_ba(self) -> bool:
        return self.value == "BA"
    @property
    def is_bb(self) -> bool:
        return self.value == "BB"
    @property
    def is_bc(self) -> bool:
        return self.value == "BC"
    @property
    def is_bd(self) -> bool:
        return self.value == "BD"
    @property
    def is_be(self) -> bool:
        return self.value == "BE"
    @property
    def is_bf(self) -> bool:
        return self.value == "BF"
    @property
    def is_bg(self) -> bool:
        return self.value == "BG"
    @property
    def is_bh(self) -> bool:
        return self.value == "BH"
