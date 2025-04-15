"""
FIX SecurityType field (tag 167).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityTypeValues:
    """Enumerated values for SecurityType."""
    EUSUPRA = "EUSUPRA"  # EURO_SUPRANATIONAL_COUPONS
    FAC = "FAC"  # FEDERAL_AGENCY_COUPON
    FADN = "FADN"  # FEDERAL_AGENCY_DISCOUNT_NOTE
    PEF = "PEF"  # PRIVATE_EXPORT_FUNDING
    SUPRA = "SUPRA"  # USD_SUPRANATIONAL_COUPONS
    CORP = "CORP"  # CORPORATE_BOND
    CPP = "CPP"  # CORPORATE_PRIVATE_PLACEMENT
    CB = "CB"  # CONVERTIBLE_BOND
    DUAL = "DUAL"  # DUAL_CURRENCY
    EUCORP = "EUCORP"  # EURO_CORPORATE_BOND
    XLINKD = "XLINKD"  # INDEXED_LINKED
    STRUCT = "STRUCT"  # STRUCTURED_NOTES
    YANK = "YANK"  # YANKEE_CORPORATE_BOND
    FOR = "FOR"  # FOREIGN_EXCHANGE_CONTRACT
    CS = "CS"  # COMMON_STOCK
    PS = "PS"  # PREFERRED_STOCK
    BRADY = "BRADY"  # BRADY_BOND
    EUSOV = "EUSOV"  # EURO_SOVEREIGNS
    TBOND = "TBOND"  # US_TREASURY_BOND
    TINT = "TINT"  # INTEREST_STRIP_FROM_ANY_BOND_OR_NOTE
    TIPS = "TIPS"  # TREASURY_INFLATION_PROTECTED_SECURITIES
    TCAL = "TCAL"  # PRINCIPAL_STRIP_OF_A_CALLABLE_BOND_OR_NOTE
    TPRN = "TPRN"  # PRINCIPAL_STRIP_FROM_A_NON_CALLABLE_BOND_OR_NOTE
    UST = "UST"  # US_TREASURY_NOTE_OLD
    USTB = "USTB"  # US_TREASURY_BILL_OLD
    TNOTE = "TNOTE"  # US_TREASURY_NOTE
    TBILL = "TBILL"  # US_TREASURY_BILL
    REPO = "REPO"  # REPURCHASE
    FORWARD = "FORWARD"  # FORWARD
    BUYSELL = "BUYSELL"  # BUY_SELLBACK
    SECLOAN = "SECLOAN"  # SECURITIES_LOAN
    SECPLEDGE = "SECPLEDGE"  # SECURITIES_PLEDGE
    TERM = "TERM"  # TERM_LOAN
    RVLV = "RVLV"  # REVOLVER_LOAN
    RVLVTRM = "RVLVTRM"  # REVOLVER
    BRIDGE = "BRIDGE"  # BRIDGE_LOAN
    LOFC = "LOFC"  # LETTER_OF_CREDIT
    SWING = "SWING"  # SWING_LINE_FACILITY
    DINP = "DINP"  # DEBTOR_IN_POSSESSION
    DEFLTED = "DEFLTED"  # DEFAULTED
    WITHDRN = "WITHDRN"  # WITHDRAWN
    REPLACD = "REPLACD"  # REPLACED
    MATURED = "MATURED"  # MATURED
    AMENDED = "AMENDED"  # AMENDED
    RETIRED = "RETIRED"  # RETIRED
    BA = "BA"  # BANKERS_ACCEPTANCE
    BN = "BN"  # BANK_NOTES
    BOX = "BOX"  # BILL_OF_EXCHANGES
    CD = "CD"  # CERTIFICATE_OF_DEPOSIT
    CL = "CL"  # CALL_LOANS
    CP = "CP"  # COMMERCIAL_PAPER
    DN = "DN"  # DEPOSIT_NOTES
    EUCD = "EUCD"  # EURO_CERTIFICATE_OF_DEPOSIT
    EUCP = "EUCP"  # EURO_COMMERCIAL_PAPER
    LQN = "LQN"  # LIQUIDITY_NOTE
    MTN = "MTN"  # MEDIUM_TERM_NOTES
    ONITE = "ONITE"  # OVERNIGHT
    PN = "PN"  # PROMISSORY_NOTE
    PZFJ = "PZFJ"  # PLAZOS_FIJOS
    STN = "STN"  # SHORT_TERM_LOAN_NOTE
    TD = "TD"  # TIME_DEPOSIT
    XCN = "XCN"  # EXTENDED_COMM_NOTE
    YCD = "YCD"  # YANKEE_CERTIFICATE_OF_DEPOSIT
    ABS = "ABS"  # ASSET_BACKED_SECURITIES
    CMBS = "CMBS"  # CORP
    CMO = "CMO"  # COLLATERALIZED_MORTGAGE_OBLIGATION
    IET = "IET"  # IOETTE_MORTGAGE
    MBS = "MBS"  # MORTGAGE_BACKED_SECURITIES
    MIO = "MIO"  # MORTGAGE_INTEREST_ONLY
    MPO = "MPO"  # MORTGAGE_PRINCIPAL_ONLY
    MPP = "MPP"  # MORTGAGE_PRIVATE_PLACEMENT
    MPT = "MPT"  # MISCELLANEOUS_PASS_THROUGH
    PFAND = "PFAND"  # PFANDBRIEFE
    TBA = "TBA"  # TO_BE_ANNOUNCED
    AN = "AN"  # OTHER_ANTICIPATION_NOTES
    COFO = "COFO"  # CERTIFICATE_OF_OBLIGATION
    COFP = "COFP"  # CERTIFICATE_OF_PARTICIPATION
    GO = "GO"  # GENERAL_OBLIGATION_BONDS
    MT = "MT"  # MANDATORY_TENDER
    RAN = "RAN"  # REVENUE_ANTICIPATION_NOTE
    REV = "REV"  # REVENUE_BONDS
    SPCLA = "SPCLA"  # SPECIAL_ASSESSMENT
    SPCLO = "SPCLO"  # SPECIAL_OBLIGATION
    SPCLT = "SPCLT"  # SPECIAL_TAX
    TAN = "TAN"  # TAX_ANTICIPATION_NOTE
    TAXA = "TAXA"  # TAX_ALLOCATION
    TECP = "TECP"  # TAX_EXEMPT_COMMERCIAL_PAPER
    TRAN = "TRAN"  # TAX_REVENUE_ANTICIPATION_NOTE
    VRDN = "VRDN"  # VARIABLE_RATE_DEMAND_NOTE
    WAR = "WAR"  # WARRANT
    MF = "MF"  # MUTUAL_FUND
    MLEG = "MLEG"  # MULTILEG_INSTRUMENT
    NONE = "NONE"  # NO_SECURITY_TYPE
    FUT = "FUT"  # FUTURE
    OPT = "OPT"  # OPTION

class SecurityTypeField(FIXFieldBase):
    """"""
    tag: str = "167"
    name: str = "SecurityType"
    type: str = "STRING"
    value: Literal["EUSUPRA", "FAC", "FADN", "PEF", "SUPRA", "CORP", "CPP", "CB", "DUAL", "EUCORP", "XLINKD", "STRUCT", "YANK", "FOR", "CS", "PS", "BRADY", "EUSOV", "TBOND", "TINT", "TIPS", "TCAL", "TPRN", "UST", "USTB", "TNOTE", "TBILL", "REPO", "FORWARD", "BUYSELL", "SECLOAN", "SECPLEDGE", "TERM", "RVLV", "RVLVTRM", "BRIDGE", "LOFC", "SWING", "DINP", "DEFLTED", "WITHDRN", "REPLACD", "MATURED", "AMENDED", "RETIRED", "BA", "BN", "BOX", "CD", "CL", "CP", "DN", "EUCD", "EUCP", "LQN", "MTN", "ONITE", "PN", "PZFJ", "STN", "TD", "XCN", "YCD", "ABS", "CMBS", "CMO", "IET", "MBS", "MIO", "MPO", "MPP", "MPT", "PFAND", "TBA", "AN", "COFO", "COFP", "GO", "MT", "RAN", "REV", "SPCLA", "SPCLO", "SPCLT", "TAN", "TAXA", "TECP", "TRAN", "VRDN", "WAR", "MF", "MLEG", "NONE", "FUT", "OPT"]

    # Helper methods for enum values
    @property
    def is_eusupra(self) -> bool:
        return self.value == "EUSUPRA"
    @property
    def is_fac(self) -> bool:
        return self.value == "FAC"
    @property
    def is_fadn(self) -> bool:
        return self.value == "FADN"
    @property
    def is_pef(self) -> bool:
        return self.value == "PEF"
    @property
    def is_supra(self) -> bool:
        return self.value == "SUPRA"
    @property
    def is_corp(self) -> bool:
        return self.value == "CORP"
    @property
    def is_cpp(self) -> bool:
        return self.value == "CPP"
    @property
    def is_cb(self) -> bool:
        return self.value == "CB"
    @property
    def is_dual(self) -> bool:
        return self.value == "DUAL"
    @property
    def is_eucorp(self) -> bool:
        return self.value == "EUCORP"
    @property
    def is_xlinkd(self) -> bool:
        return self.value == "XLINKD"
    @property
    def is_struct(self) -> bool:
        return self.value == "STRUCT"
    @property
    def is_yank(self) -> bool:
        return self.value == "YANK"
    @property
    def is_for(self) -> bool:
        return self.value == "FOR"
    @property
    def is_cs(self) -> bool:
        return self.value == "CS"
    @property
    def is_ps(self) -> bool:
        return self.value == "PS"
    @property
    def is_brady(self) -> bool:
        return self.value == "BRADY"
    @property
    def is_eusov(self) -> bool:
        return self.value == "EUSOV"
    @property
    def is_tbond(self) -> bool:
        return self.value == "TBOND"
    @property
    def is_tint(self) -> bool:
        return self.value == "TINT"
    @property
    def is_tips(self) -> bool:
        return self.value == "TIPS"
    @property
    def is_tcal(self) -> bool:
        return self.value == "TCAL"
    @property
    def is_tprn(self) -> bool:
        return self.value == "TPRN"
    @property
    def is_ust(self) -> bool:
        return self.value == "UST"
    @property
    def is_ustb(self) -> bool:
        return self.value == "USTB"
    @property
    def is_tnote(self) -> bool:
        return self.value == "TNOTE"
    @property
    def is_tbill(self) -> bool:
        return self.value == "TBILL"
    @property
    def is_repo(self) -> bool:
        return self.value == "REPO"
    @property
    def is_forward(self) -> bool:
        return self.value == "FORWARD"
    @property
    def is_buysell(self) -> bool:
        return self.value == "BUYSELL"
    @property
    def is_secloan(self) -> bool:
        return self.value == "SECLOAN"
    @property
    def is_secpledge(self) -> bool:
        return self.value == "SECPLEDGE"
    @property
    def is_term(self) -> bool:
        return self.value == "TERM"
    @property
    def is_rvlv(self) -> bool:
        return self.value == "RVLV"
    @property
    def is_rvlvtrm(self) -> bool:
        return self.value == "RVLVTRM"
    @property
    def is_bridge(self) -> bool:
        return self.value == "BRIDGE"
    @property
    def is_lofc(self) -> bool:
        return self.value == "LOFC"
    @property
    def is_swing(self) -> bool:
        return self.value == "SWING"
    @property
    def is_dinp(self) -> bool:
        return self.value == "DINP"
    @property
    def is_deflted(self) -> bool:
        return self.value == "DEFLTED"
    @property
    def is_withdrn(self) -> bool:
        return self.value == "WITHDRN"
    @property
    def is_replacd(self) -> bool:
        return self.value == "REPLACD"
    @property
    def is_matured(self) -> bool:
        return self.value == "MATURED"
    @property
    def is_amended(self) -> bool:
        return self.value == "AMENDED"
    @property
    def is_retired(self) -> bool:
        return self.value == "RETIRED"
    @property
    def is_ba(self) -> bool:
        return self.value == "BA"
    @property
    def is_bn(self) -> bool:
        return self.value == "BN"
    @property
    def is_box(self) -> bool:
        return self.value == "BOX"
    @property
    def is_cd(self) -> bool:
        return self.value == "CD"
    @property
    def is_cl(self) -> bool:
        return self.value == "CL"
    @property
    def is_cp(self) -> bool:
        return self.value == "CP"
    @property
    def is_dn(self) -> bool:
        return self.value == "DN"
    @property
    def is_eucd(self) -> bool:
        return self.value == "EUCD"
    @property
    def is_eucp(self) -> bool:
        return self.value == "EUCP"
    @property
    def is_lqn(self) -> bool:
        return self.value == "LQN"
    @property
    def is_mtn(self) -> bool:
        return self.value == "MTN"
    @property
    def is_onite(self) -> bool:
        return self.value == "ONITE"
    @property
    def is_pn(self) -> bool:
        return self.value == "PN"
    @property
    def is_pzfj(self) -> bool:
        return self.value == "PZFJ"
    @property
    def is_stn(self) -> bool:
        return self.value == "STN"
    @property
    def is_td(self) -> bool:
        return self.value == "TD"
    @property
    def is_xcn(self) -> bool:
        return self.value == "XCN"
    @property
    def is_ycd(self) -> bool:
        return self.value == "YCD"
    @property
    def is_abs(self) -> bool:
        return self.value == "ABS"
    @property
    def is_cmbs(self) -> bool:
        return self.value == "CMBS"
    @property
    def is_cmo(self) -> bool:
        return self.value == "CMO"
    @property
    def is_iet(self) -> bool:
        return self.value == "IET"
    @property
    def is_mbs(self) -> bool:
        return self.value == "MBS"
    @property
    def is_mio(self) -> bool:
        return self.value == "MIO"
    @property
    def is_mpo(self) -> bool:
        return self.value == "MPO"
    @property
    def is_mpp(self) -> bool:
        return self.value == "MPP"
    @property
    def is_mpt(self) -> bool:
        return self.value == "MPT"
    @property
    def is_pfand(self) -> bool:
        return self.value == "PFAND"
    @property
    def is_tba(self) -> bool:
        return self.value == "TBA"
    @property
    def is_an(self) -> bool:
        return self.value == "AN"
    @property
    def is_cofo(self) -> bool:
        return self.value == "COFO"
    @property
    def is_cofp(self) -> bool:
        return self.value == "COFP"
    @property
    def is_go(self) -> bool:
        return self.value == "GO"
    @property
    def is_mt(self) -> bool:
        return self.value == "MT"
    @property
    def is_ran(self) -> bool:
        return self.value == "RAN"
    @property
    def is_rev(self) -> bool:
        return self.value == "REV"
    @property
    def is_spcla(self) -> bool:
        return self.value == "SPCLA"
    @property
    def is_spclo(self) -> bool:
        return self.value == "SPCLO"
    @property
    def is_spclt(self) -> bool:
        return self.value == "SPCLT"
    @property
    def is_tan(self) -> bool:
        return self.value == "TAN"
    @property
    def is_taxa(self) -> bool:
        return self.value == "TAXA"
    @property
    def is_tecp(self) -> bool:
        return self.value == "TECP"
    @property
    def is_tran(self) -> bool:
        return self.value == "TRAN"
    @property
    def is_vrdn(self) -> bool:
        return self.value == "VRDN"
    @property
    def is_war(self) -> bool:
        return self.value == "WAR"
    @property
    def is_mf(self) -> bool:
        return self.value == "MF"
    @property
    def is_mleg(self) -> bool:
        return self.value == "MLEG"
    @property
    def is_none(self) -> bool:
        return self.value == "NONE"
    @property
    def is_fut(self) -> bool:
        return self.value == "FUT"
    @property
    def is_opt(self) -> bool:
        return self.value == "OPT"
