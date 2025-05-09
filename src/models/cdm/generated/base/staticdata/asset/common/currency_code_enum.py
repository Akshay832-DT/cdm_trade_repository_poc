from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CurrencyCodeEnum(CdmModelBase):
    """Union of the enumerated values defined by the International Standards Organization (ISO) and the FpML nonISOCurrencyScheme which consists of offshore and historical currencies (https://www.fpml.org/coding-scheme/non-iso-currency), as of 28-Oct-2016."""
    # Enum values
    AED: ClassVar[str] = "AED"
    AFN: ClassVar[str] = "AFN"
    ALL: ClassVar[str] = "ALL"
    AMD: ClassVar[str] = "AMD"
    ANG: ClassVar[str] = "ANG"
    AOA: ClassVar[str] = "AOA"
    ARS: ClassVar[str] = "ARS"
    AUD: ClassVar[str] = "AUD"
    AWG: ClassVar[str] = "AWG"
    AZN: ClassVar[str] = "AZN"
    BAM: ClassVar[str] = "BAM"
    BBD: ClassVar[str] = "BBD"
    BDT: ClassVar[str] = "BDT"
    BGN: ClassVar[str] = "BGN"
    BHD: ClassVar[str] = "BHD"
    BIF: ClassVar[str] = "BIF"
    BMD: ClassVar[str] = "BMD"
    BND: ClassVar[str] = "BND"
    BOB: ClassVar[str] = "BOB"
    BOV: ClassVar[str] = "BOV"
    BRL: ClassVar[str] = "BRL"
    BSD: ClassVar[str] = "BSD"
    BTN: ClassVar[str] = "BTN"
    BWP: ClassVar[str] = "BWP"
    BYN: ClassVar[str] = "BYN"
    BZD: ClassVar[str] = "BZD"
    CAD: ClassVar[str] = "CAD"
    CDF: ClassVar[str] = "CDF"
    CHE: ClassVar[str] = "CHE"
    CHF: ClassVar[str] = "CHF"
    CHW: ClassVar[str] = "CHW"
    CLF: ClassVar[str] = "CLF"
    CLP: ClassVar[str] = "CLP"
    CNH: ClassVar[str] = "CNH"
    CNT: ClassVar[str] = "CNT"
    CNY: ClassVar[str] = "CNY"
    COP: ClassVar[str] = "COP"
    COU: ClassVar[str] = "COU"
    CRC: ClassVar[str] = "CRC"
    CUC: ClassVar[str] = "CUC"
    CUP: ClassVar[str] = "CUP"
    CVE: ClassVar[str] = "CVE"
    CZK: ClassVar[str] = "CZK"
    DJF: ClassVar[str] = "DJF"
    DKK: ClassVar[str] = "DKK"
    DOP: ClassVar[str] = "DOP"
    DZD: ClassVar[str] = "DZD"
    EGP: ClassVar[str] = "EGP"
    ERN: ClassVar[str] = "ERN"
    ETB: ClassVar[str] = "ETB"
    EUR: ClassVar[str] = "EUR"
    FJD: ClassVar[str] = "FJD"
    FKP: ClassVar[str] = "FKP"
    GBP: ClassVar[str] = "GBP"
    GEL: ClassVar[str] = "GEL"
    GGP: ClassVar[str] = "GGP"
    GHS: ClassVar[str] = "GHS"
    GIP: ClassVar[str] = "GIP"
    GMD: ClassVar[str] = "GMD"
    GNF: ClassVar[str] = "GNF"
    GTQ: ClassVar[str] = "GTQ"
    GYD: ClassVar[str] = "GYD"
    HKD: ClassVar[str] = "HKD"
    HNL: ClassVar[str] = "HNL"
    HTG: ClassVar[str] = "HTG"
    HUF: ClassVar[str] = "HUF"
    IDR: ClassVar[str] = "IDR"
    ILS: ClassVar[str] = "ILS"
    IMP: ClassVar[str] = "IMP"
    INR: ClassVar[str] = "INR"
    IQD: ClassVar[str] = "IQD"
    IRR: ClassVar[str] = "IRR"
    ISK: ClassVar[str] = "ISK"
    JEP: ClassVar[str] = "JEP"
    JMD: ClassVar[str] = "JMD"
    JOD: ClassVar[str] = "JOD"
    JPY: ClassVar[str] = "JPY"
    KES: ClassVar[str] = "KES"
    KGS: ClassVar[str] = "KGS"
    KHR: ClassVar[str] = "KHR"
    KID: ClassVar[str] = "KID"
    KMF: ClassVar[str] = "KMF"
    KPW: ClassVar[str] = "KPW"
    KRW: ClassVar[str] = "KRW"
    KWD: ClassVar[str] = "KWD"
    KYD: ClassVar[str] = "KYD"
    KZT: ClassVar[str] = "KZT"
    LAK: ClassVar[str] = "LAK"
    LBP: ClassVar[str] = "LBP"
    LKR: ClassVar[str] = "LKR"
    LRD: ClassVar[str] = "LRD"
    LSL: ClassVar[str] = "LSL"
    LYD: ClassVar[str] = "LYD"
    MAD: ClassVar[str] = "MAD"
    MCF: ClassVar[str] = "MCF"
    MDL: ClassVar[str] = "MDL"
    MGA: ClassVar[str] = "MGA"
    MKD: ClassVar[str] = "MKD"
    MMK: ClassVar[str] = "MMK"
    MNT: ClassVar[str] = "MNT"
    MOP: ClassVar[str] = "MOP"
    MRU: ClassVar[str] = "MRU"
    MUR: ClassVar[str] = "MUR"
    MVR: ClassVar[str] = "MVR"
    MWK: ClassVar[str] = "MWK"
    MXN: ClassVar[str] = "MXN"
    MXV: ClassVar[str] = "MXV"
    MYR: ClassVar[str] = "MYR"
    MZN: ClassVar[str] = "MZN"
    NAD: ClassVar[str] = "NAD"
    NGN: ClassVar[str] = "NGN"
    NIO: ClassVar[str] = "NIO"
    NOK: ClassVar[str] = "NOK"
    NPR: ClassVar[str] = "NPR"
    NZD: ClassVar[str] = "NZD"
    OMR: ClassVar[str] = "OMR"
    PAB: ClassVar[str] = "PAB"
    PEN: ClassVar[str] = "PEN"
    PGK: ClassVar[str] = "PGK"
    PHP: ClassVar[str] = "PHP"
    PKR: ClassVar[str] = "PKR"
    PLN: ClassVar[str] = "PLN"
    PYG: ClassVar[str] = "PYG"
    QAR: ClassVar[str] = "QAR"
    RON: ClassVar[str] = "RON"
    RSD: ClassVar[str] = "RSD"
    RUB: ClassVar[str] = "RUB"
    RWF: ClassVar[str] = "RWF"
    SAR: ClassVar[str] = "SAR"
    SBD: ClassVar[str] = "SBD"
    SCR: ClassVar[str] = "SCR"
    SDG: ClassVar[str] = "SDG"
    SEK: ClassVar[str] = "SEK"
    SGD: ClassVar[str] = "SGD"
    SHP: ClassVar[str] = "SHP"
    SLE: ClassVar[str] = "SLE"
    SML: ClassVar[str] = "SML"
    SOS: ClassVar[str] = "SOS"
    SRD: ClassVar[str] = "SRD"
    SSP: ClassVar[str] = "SSP"
    STN: ClassVar[str] = "STN"
    SVC: ClassVar[str] = "SVC"
    SYP: ClassVar[str] = "SYP"
    SZL: ClassVar[str] = "SZL"
    THB: ClassVar[str] = "THB"
    TJS: ClassVar[str] = "TJS"
    TMT: ClassVar[str] = "TMT"
    TND: ClassVar[str] = "TND"
    TOP: ClassVar[str] = "TOP"
    TRY: ClassVar[str] = "TRY"
    TTD: ClassVar[str] = "TTD"
    TWD: ClassVar[str] = "TWD"
    TZS: ClassVar[str] = "TZS"
    UAH: ClassVar[str] = "UAH"
    UGX: ClassVar[str] = "UGX"
    USD: ClassVar[str] = "USD"
    USN: ClassVar[str] = "USN"
    UYI: ClassVar[str] = "UYI"
    UYU: ClassVar[str] = "UYU"
    UYW: ClassVar[str] = "UYW"
    UZS: ClassVar[str] = "UZS"
    VAL: ClassVar[str] = "VAL"
    VED: ClassVar[str] = "VED"
    VES: ClassVar[str] = "VES"
    VND: ClassVar[str] = "VND"
    VUV: ClassVar[str] = "VUV"
    WST: ClassVar[str] = "WST"
    XAF: ClassVar[str] = "XAF"
    XAG: ClassVar[str] = "XAG"
    XAU: ClassVar[str] = "XAU"
    XBA: ClassVar[str] = "XBA"
    XBB: ClassVar[str] = "XBB"
    XBC: ClassVar[str] = "XBC"
    XBD: ClassVar[str] = "XBD"
    XCD: ClassVar[str] = "XCD"
    XCG: ClassVar[str] = "XCG"
    XDR: ClassVar[str] = "XDR"
    XOF: ClassVar[str] = "XOF"
    XPD: ClassVar[str] = "XPD"
    XPF: ClassVar[str] = "XPF"
    XPT: ClassVar[str] = "XPT"
    XSU: ClassVar[str] = "XSU"
    XTS: ClassVar[str] = "XTS"
    XUA: ClassVar[str] = "XUA"
    XXX: ClassVar[str] = "XXX"
    YER: ClassVar[str] = "YER"
    ZAR: ClassVar[str] = "ZAR"
    ZMW: ClassVar[str] = "ZMW"
    ZWG: ClassVar[str] = "ZWG"


# Import after class definition to avoid circular imports
CurrencyCodeEnum.model_rebuild()
