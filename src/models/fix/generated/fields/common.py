"""
FIX 4.4 Common Field Definitions

This module contains Pydantic models for FIX 4.4 fields.
"""
from enum import Enum
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict
from pydantic import BaseModel, Field

class AdvSideEnum(Enum):
    B = 'B'
    S = 'S'
    X = 'X'
    T = 'T'

class AdvTransTypeEnum(Enum):
    N = 'N'
    C = 'C'
    R = 'R'

class CommTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class ExecInstEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_0 = 0
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    O = 'O'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    U = 'U'
    V = 'V'
    W = 'W'
    X = 'X'
    Y = 'Y'
    Z = 'Z'
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'

class HandlInstEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class SecurityIDSourceEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'

class IOIQltyIndEnum(Enum):
    L = 'L'
    M = 'M'
    H = 'H'

class IOIQtyEnum(Enum):
    S = 'S'
    M = 'M'
    L = 'L'

class IOITransTypeEnum(Enum):
    N = 'N'
    C = 'C'
    R = 'R'

class LastCapacityEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class MsgTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    T = 'T'
    V = 'V'
    W = 'W'
    X = 'X'
    Y = 'Y'
    Z = 'Z'
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    f = 'f'
    g = 'g'
    h = 'h'
    i = 'i'
    j = 'j'
    k = 'k'
    l = 'l'
    m = 'm'
    n = 'n'
    o = 'o'
    p = 'p'
    q = 'q'
    r = 'r'
    s = 's'
    t = 't'
    u = 'u'
    v = 'v'
    w = 'w'
    x = 'x'
    y = 'y'
    z = 'z'
    AA = 'AA'
    AB = 'AB'
    AC = 'AC'
    AD = 'AD'
    AE = 'AE'
    AF = 'AF'
    AG = 'AG'
    AH = 'AH'
    AI = 'AI'
    AJ = 'AJ'
    AK = 'AK'
    AL = 'AL'
    AM = 'AM'
    AN = 'AN'
    AO = 'AO'
    AP = 'AP'
    AQ = 'AQ'
    AR = 'AR'
    AS = 'AS'
    AT = 'AT'
    AU = 'AU'
    AV = 'AV'
    AW = 'AW'
    AX = 'AX'
    AY = 'AY'
    AZ = 'AZ'
    BA = 'BA'
    BB = 'BB'
    BC = 'BC'
    BD = 'BD'
    BE = 'BE'
    BF = 'BF'
    BG = 'BG'
    BH = 'BH'

class OrdStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'

class OrdTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    D = 'D'
    E = 'E'
    G = 'G'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    P = 'P'

class PossDupFlagEnum(Enum):
    Y = 'Y'
    N = 'N'

class SideEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'

class TimeInForceEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

class UrgencyEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class SettlTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9

class AllocTransTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class PositionEffectEnum(Enum):
    O = 'O'
    C = 'C'
    R = 'R'
    F = 'F'

class ProcessCodeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class AllocStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class AllocRejCodeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13

class EmailTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class PossResendEnum(Enum):
    Y = 'Y'
    N = 'N'

class EncryptMethodEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class CxlRejReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_99 = 99

class OrdRejReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_99 = 99

class IOIQualifierEnum(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    I = 'I'
    L = 'L'
    M = 'M'
    O = 'O'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    T = 'T'
    V = 'V'
    W = 'W'
    X = 'X'
    Y = 'Y'
    Z = 'Z'

class ReportToExchEnum(Enum):
    Y = 'Y'
    N = 'N'

class LocateReqdEnum(Enum):
    Y = 'Y'
    N = 'N'

class ForexReqEnum(Enum):
    Y = 'Y'
    N = 'N'

class GapFillFlagEnum(Enum):
    Y = 'Y'
    N = 'N'

class DKReasonEnum(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    Z = 'Z'

class IOINaturalFlagEnum(Enum):
    Y = 'Y'
    N = 'N'

class MiscFeeTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12

class ResetSeqNumFlagEnum(Enum):
    Y = 'Y'
    N = 'N'

class ExecTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'

class SettlCurrFxRateCalcEnum(Enum):
    M = 'M'
    D = 'D'

class SettlInstModeEnum(Enum):
    VALUE_1 = 1
    VALUE_4 = 4
    VALUE_5 = 5

class SettlInstTransTypeEnum(Enum):
    N = 'N'
    C = 'C'
    R = 'R'
    T = 'T'

class SettlInstSourceEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class SecurityTypeEnum(Enum):
    EUSUPRA = 'EUSUPRA'
    FAC = 'FAC'
    FADN = 'FADN'
    PEF = 'PEF'
    SUPRA = 'SUPRA'
    CORP = 'CORP'
    CPP = 'CPP'
    CB = 'CB'
    DUAL = 'DUAL'
    EUCORP = 'EUCORP'
    XLINKD = 'XLINKD'
    STRUCT = 'STRUCT'
    YANK = 'YANK'
    FOR = 'FOR'
    CS = 'CS'
    PS = 'PS'
    BRADY = 'BRADY'
    EUSOV = 'EUSOV'
    TBOND = 'TBOND'
    TINT = 'TINT'
    TIPS = 'TIPS'
    TCAL = 'TCAL'
    TPRN = 'TPRN'
    UST = 'UST'
    USTB = 'USTB'
    TNOTE = 'TNOTE'
    TBILL = 'TBILL'
    REPO = 'REPO'
    FORWARD = 'FORWARD'
    BUYSELL = 'BUYSELL'
    SECLOAN = 'SECLOAN'
    SECPLEDGE = 'SECPLEDGE'
    TERM = 'TERM'
    RVLV = 'RVLV'
    RVLVTRM = 'RVLVTRM'
    BRIDGE = 'BRIDGE'
    LOFC = 'LOFC'
    SWING = 'SWING'
    DINP = 'DINP'
    DEFLTED = 'DEFLTED'
    WITHDRN = 'WITHDRN'
    REPLACD = 'REPLACD'
    MATURED = 'MATURED'
    AMENDED = 'AMENDED'
    RETIRED = 'RETIRED'
    BA = 'BA'
    BN = 'BN'
    BOX = 'BOX'
    CD = 'CD'
    CL = 'CL'
    CP = 'CP'
    DN = 'DN'
    EUCD = 'EUCD'
    EUCP = 'EUCP'
    LQN = 'LQN'
    MTN = 'MTN'
    ONITE = 'ONITE'
    PN = 'PN'
    PZFJ = 'PZFJ'
    STN = 'STN'
    TD = 'TD'
    XCN = 'XCN'
    YCD = 'YCD'
    ABS = 'ABS'
    CMBS = 'CMBS'
    CMO = 'CMO'
    IET = 'IET'
    MBS = 'MBS'
    MIO = 'MIO'
    MPO = 'MPO'
    MPP = 'MPP'
    MPT = 'MPT'
    PFAND = 'PFAND'
    TBA = 'TBA'
    AN = 'AN'
    COFO = 'COFO'
    COFP = 'COFP'
    GO = 'GO'
    MT = 'MT'
    RAN = 'RAN'
    REV = 'REV'
    SPCLA = 'SPCLA'
    SPCLO = 'SPCLO'
    SPCLT = 'SPCLT'
    TAN = 'TAN'
    TAXA = 'TAXA'
    TECP = 'TECP'
    TRAN = 'TRAN'
    VRDN = 'VRDN'
    WAR = 'WAR'
    MF = 'MF'
    MLEG = 'MLEG'
    NONE = 'NONE'
    FUT = 'FUT'
    OPT = 'OPT'

class StandInstDbTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class SettlDeliveryTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class AllocLinkTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class PutOrCallEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class CoveredOrUncoveredEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class NotifyBrokerOfCreditEnum(Enum):
    Y = 'Y'
    N = 'N'

class AllocHandlInstEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class RoutingTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class StipulationTypeEnum(Enum):
    AMT = 'AMT'
    AUTOREINV = 'AUTOREINV'
    BANKQUAL = 'BANKQUAL'
    BGNCON = 'BGNCON'
    COUPON = 'COUPON'
    CURRENCY = 'CURRENCY'
    CUSTOMDATE = 'CUSTOMDATE'
    GEOG = 'GEOG'
    HAIRCUT = 'HAIRCUT'
    INSURED = 'INSURED'
    ISSUE = 'ISSUE'
    ISSUER = 'ISSUER'
    ISSUESIZE = 'ISSUESIZE'
    LOOKBACK = 'LOOKBACK'
    LOT = 'LOT'
    LOTVAR = 'LOTVAR'
    MAT = 'MAT'
    MATURITY = 'MATURITY'
    MAXSUBS = 'MAXSUBS'
    MINQTY = 'MINQTY'
    MININCR = 'MININCR'
    MINDNOM = 'MINDNOM'
    PAYFREQ = 'PAYFREQ'
    PIECES = 'PIECES'
    PMAX = 'PMAX'
    PPM = 'PPM'
    PPL = 'PPL'
    PPT = 'PPT'
    PRICE = 'PRICE'
    PRICEFREQ = 'PRICEFREQ'
    PROD = 'PROD'
    PROTECT = 'PROTECT'
    PURPOSE = 'PURPOSE'
    PXSOURCE = 'PXSOURCE'
    RATING = 'RATING'
    REDEMPTION = 'REDEMPTION'
    RESTRICTED = 'RESTRICTED'
    SECTOR = 'SECTOR'
    SECTYPE = 'SECTYPE'
    STRUCT = 'STRUCT'
    SUBSFREQ = 'SUBSFREQ'
    SUBSLEFT = 'SUBSLEFT'
    TEXT = 'TEXT'
    TRDVAR = 'TRDVAR'
    WAC = 'WAC'
    WAL = 'WAL'
    WALA = 'WALA'
    WAM = 'WAM'
    WHOLE = 'WHOLE'
    YIELD = 'YIELD'

class YieldTypeEnum(Enum):
    AFTERTAX = 'AFTERTAX'
    ANNUAL = 'ANNUAL'
    ATISSUE = 'ATISSUE'
    AVGMATURITY = 'AVGMATURITY'
    BOOK = 'BOOK'
    CALL = 'CALL'
    CHANGE = 'CHANGE'
    CLOSE = 'CLOSE'
    COMPOUND = 'COMPOUND'
    CURRENT = 'CURRENT'
    GROSS = 'GROSS'
    GOVTEQUIV = 'GOVTEQUIV'
    INFLATION = 'INFLATION'
    INVERSEFLOATER = 'INVERSEFLOATER'
    LASTCLOSE = 'LASTCLOSE'
    LASTMONTH = 'LASTMONTH'
    LASTQUARTER = 'LASTQUARTER'
    LASTYEAR = 'LASTYEAR'
    LONGAVGLIFE = 'LONGAVGLIFE'
    MARK = 'MARK'
    MATURITY = 'MATURITY'
    NEXTREFUND = 'NEXTREFUND'
    OPENAVG = 'OPENAVG'
    PUT = 'PUT'
    PREVCLOSE = 'PREVCLOSE'
    PROCEEDS = 'PROCEEDS'
    SEMIANNUAL = 'SEMIANNUAL'
    SHORTAVGLIFE = 'SHORTAVGLIFE'
    SIMPLE = 'SIMPLE'
    TAXEQUIV = 'TAXEQUIV'
    TENDER = 'TENDER'
    TRUE = 'TRUE'
    VALUE1/32 = 'VALUE1/32'
    WORST = 'WORST'

class TradedFlatSwitchEnum(Enum):
    Y = 'Y'
    N = 'N'

class SubscriptionRequestTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class MDUpdateTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class AggregatedBookEnum(Enum):
    Y = 'Y'
    N = 'N'

class MDEntryTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    A = 'A'
    B = 'B'
    C = 'C'

class TickDirectionEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class QuoteConditionEnum(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'

class TradeConditionEnum(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    P = 'P'
    Q = 'Q'
    R = 'R'

class MDUpdateActionEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class MDReqRejReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    A = 'A'
    B = 'B'
    C = 'C'

class DeleteReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class OpenCloseSettlFlagEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class FinancialStatusEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class CorporateActionEnum(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'

class QuoteStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15

class QuoteCancelTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class QuoteRejectReasonEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_99 = 99

class QuoteResponseLevelEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class QuoteRequestTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class SecurityRequestTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class SecurityResponseTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_5 = 5
    VALUE_6 = 6

class UnsolicitedIndicatorEnum(Enum):
    Y = 'Y'
    N = 'N'

class SecurityTradingStatusEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23

class HaltReasonCharEnum(Enum):
    I = 'I'
    X = 'X'
    P = 'P'
    D = 'D'
    E = 'E'
    M = 'M'

class InViewOfCommonEnum(Enum):
    Y = 'Y'
    N = 'N'

class DueToRelatedEnum(Enum):
    Y = 'Y'
    N = 'N'

class AdjustmentEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class TradSesMethodEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class TradSesModeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class TradSesStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class MessageEncodingEnum(Enum):
    ISO-2022-JP = 'ISO-2022-JP'
    EUC-JP = 'EUC-JP'
    Shift_JIS = 'Shift_JIS'
    UTF-8 = 'UTF-8'

class SessionRejectReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_99 = 99

class BidRequestTransTypeEnum(Enum):
    N = 'N'
    C = 'C'

class SolicitedFlagEnum(Enum):
    Y = 'Y'
    N = 'N'

class ExecRestatementReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_99 = 99

class BusinessRejectReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

class MsgDirectionEnum(Enum):
    S = 'S'
    R = 'R'

class DiscretionInstEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class BidTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class BidDescriptorTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class SideValueIndEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class LiquidityIndTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class ExchangeForPhysicalEnum(Enum):
    Y = 'Y'
    N = 'N'

class ProgRptReqsEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class IncTaxIndEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class BidTradeTypeEnum(Enum):
    R = 'R'
    G = 'G'
    A = 'A'
    J = 'J'

class BasisPxTypeEnum(Enum):
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    Z = 'Z'

class PriceTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11

class GTBookingInstEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class ListStatusTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class NetGrossIndEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class ListOrderStatusEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

class ListExecInstTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class CxlRejResponseToEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class MultiLegReportingTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class PartyIDSourceEnum(Enum):
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    A = 'A'
    I = 'I'

class PartyRoleEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_34 = 34
    VALUE_35 = 35
    VALUE_36 = 36
    VALUE_37 = 37
    VALUE_38 = 38

class ProductEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13

class TestMessageIndicatorEnum(Enum):
    Y = 'Y'
    N = 'N'

class RoundingDirectionEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class DistribPaymentMethodEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12

class CancellationRightsEnum(Enum):
    Y = 'Y'
    N = 'N'
    M = 'M'
    O = 'O'

class MoneyLaunderingStatusEnum(Enum):
    Y = 'Y'
    N = 'N'
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class ExecPriceTypeEnum(Enum):
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    O = 'O'
    P = 'P'
    Q = 'Q'
    S = 'S'

class PaymentMethodEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15

class TaxAdvantageTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_29 = 29

class FundRenewWaivEnum(Enum):
    Y = 'Y'
    N = 'N'

class RegistStatusEnum(Enum):
    A = 'A'
    R = 'R'
    H = 'H'
    N = 'N'

class RegistRejReasonCodeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_99 = 99

class RegistTransTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class OwnershipTypeEnum(Enum):
    J = 'J'
    T = 'T'
    VALUE_2 = 2

class ContAmtTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15

class OwnerTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13

class OrderCapacityEnum(Enum):
    A = 'A'
    G = 'G'
    I = 'I'
    P = 'P'
    R = 'R'
    W = 'W'

class OrderRestrictionsEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    A = 'A'

class MassCancelRequestTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

class MassCancelResponseEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

class MassCancelRejectReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_99 = 99

class QuoteTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class CashMarginEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class ScopeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class MDImplicitDeleteEnum(Enum):
    Y = 'Y'
    N = 'N'

class CrossTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class CrossPrioritizationEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class NoSidesEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class SecurityListRequestTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class SecurityRequestResultEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class MultiLegRptTypeReqEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class TradSesStatusRejReasonEnum(Enum):
    VALUE_1 = 1
    VALUE_99 = 99

class TradeRequestTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class PreviouslyReportedEnum(Enum):
    Y = 'Y'
    N = 'N'

class MatchStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class MatchTypeEnum(Enum):
    A1 = 'A1'
    A2 = 'A2'
    A3 = 'A3'
    A4 = 'A4'
    A5 = 'A5'
    AQ = 'AQ'
    S1 = 'S1'
    S2 = 'S2'
    S3 = 'S3'
    S4 = 'S4'
    S5 = 'S5'
    M1 = 'M1'
    M2 = 'M2'
    MT = 'MT'
    M3 = 'M3'
    M4 = 'M4'
    M5 = 'M5'
    M6 = 'M6'

class OddLotEnum(Enum):
    Y = 'Y'
    N = 'N'

class ClearingInstructionEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13

class AccountTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8

class CustOrderCapacityEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class MassStatusReqTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8

class DayBookingInstEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class BookingUnitEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class PreallocMethodEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class AllocTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_5 = 5
    VALUE_7 = 7
    VALUE_8 = 8

class ClearingFeeIndicatorEnum(Enum):
    B = 'B'
    C = 'C'
    E = 'E'
    F = 'F'
    H = 'H'
    I = 'I'
    L = 'L'
    M = 'M'
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_9 = 9

class WorkingIndicatorEnum(Enum):
    Y = 'Y'
    N = 'N'

class PriorityIndicatorEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class LegalConfirmEnum(Enum):
    Y = 'Y'
    N = 'N'

class QuoteRequestRejectReasonEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_99 = 99

class AcctIDSourceEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_99 = 99

class ConfirmStatusEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class ConfirmTransTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class DeliveryFormEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class LegSwapTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_5 = 5

class QuotePriceTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10

class QuoteRespTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class PosTypeEnum(Enum):
    TQ = 'TQ'
    IAS = 'IAS'
    IES = 'IES'
    FIN = 'FIN'
    SOD = 'SOD'
    EX = 'EX'
    AS = 'AS'
    TX = 'TX'
    TA = 'TA'
    PIT = 'PIT'
    TRF = 'TRF'
    ETR = 'ETR'
    ALC = 'ALC'
    PA = 'PA'
    ASF = 'ASF'
    DLV = 'DLV'
    TOT = 'TOT'
    XM = 'XM'
    SPL = 'SPL'

class PosQtyStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class PosAmtTypeEnum(Enum):
    FMTM = 'FMTM'
    IMTM = 'IMTM'
    TVAR = 'TVAR'
    SMTM = 'SMTM'
    PREM = 'PREM'
    CRES = 'CRES'
    CASH = 'CASH'
    VADJ = 'VADJ'

class PosTransTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class PosMaintActionEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class SettlSessIDEnum(Enum):
    ITD = 'ITD'
    RTH = 'RTH'
    ETH = 'ETH'

class AdjustmentTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class PosMaintStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class PosMaintResultEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_99 = 99

class PosReqTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class ResponseTransportTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class PosReqResultEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_99 = 99

class PosReqStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class SettlPriceTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class AssignmentMethodEnum(Enum):
    R = 'R'
    P = 'P'

class ExerciseMethodEnum(Enum):
    A = 'A'
    M = 'M'

class TradeRequestResultEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_99 = 99

class TradeRequestStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class TradeReportRejectReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_99 = 99

class SideMultiLegReportingTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class TrdRegTimestampTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class ConfirmTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class ConfirmRejReasonEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_99 = 99

class BookingTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class AllocSettlInstTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class DlvyInstTypeEnum(Enum):
    S = 'S'
    C = 'C'

class TerminationTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class SettlInstReqRejCodeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_99 = 99

class AllocReportTypeEnum(Enum):
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_8 = 8

class AllocCancReplaceReasonEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_99 = 99

class AllocAccountTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8

class PartySubIDTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26

class AllocIntermedReqTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class ApplQueueResolutionEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class ApplQueueActionEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class AvgPxIndicatorEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class TradeAllocIndicatorEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class ExpirationCycleEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class TrdTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10

class PegMoveTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class PegOffsetTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class PegLimitTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class PegRoundDirectionEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class PegScopeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class DiscretionMoveTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class DiscretionOffsetTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class DiscretionLimitTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class DiscretionRoundDirectionEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class DiscretionScopeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class TargetStrategyEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class LastLiquidityIndEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class PublishTrdIndicatorEnum(Enum):
    Y = 'Y'
    N = 'N'

class ShortSaleReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class QtyTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class TradeReportTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

class AllocNoOrdersTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class EventTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_99 = 99

class InstrAttribTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_99 = 99

class CPProgramEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_99 = 99

class MiscFeeBasisEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class LastFragmentEnum(Enum):
    Y = 'Y'
    N = 'N'

class CollAsgnReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

class CollInquiryQualifierEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

class CollAsgnTransTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class CollAsgnRespTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class CollAsgnRejectReasonEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_99 = 99

class CollStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class DeliveryTypeEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class UserRequestTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class UserStatusEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class StatusValueEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class NetworkRequestTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_8 = 8

class NetworkStatusResponseTypeEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2

class TrdRptStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1

class AffirmStatusEnum(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class CollActionEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class CollInquiryStatusEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class CollInquiryResultEnum(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_99 = 99

