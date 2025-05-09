from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CommodityBusinessCalendarEnum(CdmModelBase):
    """"""
    # Enum values
    ADSM: ClassVar[str] = "ADSM"
    AGRUS_FMB: ClassVar[str] = "AGRUS-FMB"
    APPI: ClassVar[str] = "APPI"
    ARGUS_CRUDE: ClassVar[str] = "ARGUS-CRUDE"
    ARGUS_EUROPEAN_GAS: ClassVar[str] = "ARGUS-EUROPEAN-GAS"
    ARGUS_EUROPEAN_PRODUCTS: ClassVar[str] = "ARGUS-EUROPEAN-PRODUCTS"
    ARGUS_INTERNATIONAL_LPG: ClassVar[str] = "ARGUS-INTERNATIONAL-LPG"
    ARGUS_MCCLOSKEYS_COAL_REPORT: ClassVar[str] = "ARGUS-MCCLOSKEYS-COAL-REPORT"
    ARGUS_US_PRODUCTS: ClassVar[str] = "ARGUS-US-PRODUCTS"
    ASX: ClassVar[str] = "ASX"
    AWB: ClassVar[str] = "AWB"
    AWEX: ClassVar[str] = "AWEX"
    BALTIC_EXCHANGE: ClassVar[str] = "BALTIC-EXCHANGE"
    BANK_NEGARA_MALAYSIA_POLICY_COMMITTEE: ClassVar[str] = "BANK-NEGARA-MALAYSIA-POLICY-COMMITTEE"
    BELPEX: ClassVar[str] = "BELPEX"
    BLUENEXT: ClassVar[str] = "BLUENEXT"
    BM_F: ClassVar[str] = "BM&F"
    BURSA_MALAYSIA_SETTLEMENT: ClassVar[str] = "BURSA-MALAYSIA-SETTLEMENT"
    BURSA_MALAYSIA_TRADING: ClassVar[str] = "BURSA-MALAYSIA-TRADING"
    CANADIAN_GAS_PRICE_REPORTER: ClassVar[str] = "CANADIAN-GAS-PRICE-REPORTER"
    CBOT_SOFT: ClassVar[str] = "CBOT-SOFT"
    CMAI_AROMATICS_MARKET_REPORT: ClassVar[str] = "CMAI-AROMATICS-MARKET-REPORT"
    CMAI_GLOBAL_PLASTICS_AND_POLYMERS_MARKET_REPORT: ClassVar[str] = "CMAI-GLOBAL-PLASTICS-AND-POLYMERS-MARKET-REPORT"
    CMAI_METHANOL_MARKET_REPORT: ClassVar[str] = "CMAI-METHANOL-MARKET-REPORT"
    CMAI_MONOMERS_MARKET_REPORT: ClassVar[str] = "CMAI-MONOMERS-MARKET-REPORT"
    CME_DAIRY: ClassVar[str] = "CME-DAIRY"
    CME_NON_DAIRY_SOFT: ClassVar[str] = "CME-NON-DAIRY-SOFT"
    COMEX: ClassVar[str] = "COMEX"
    CRU: ClassVar[str] = "CRU"
    CRU_LONG: ClassVar[str] = "CRU-LONG"
    DEPARTMENT_OF_ENERGY: ClassVar[str] = "DEPARTMENT-OF-ENERGY"
    DEWITT_BENZENE_DERIVATIVES: ClassVar[str] = "DEWITT-BENZENE-DERIVATIVES"
    DME: ClassVar[str] = "DME"
    DOW_JONES: ClassVar[str] = "DOW-JONES"
    DOW_JONES_ENERGY_SERVICE: ClassVar[str] = "DOW-JONES-ENERGY-SERVICE"
    DowJonesPower: ClassVar[str] = "DowJonesPower"
    EEX_COAL: ClassVar[str] = "EEX-COAL"
    EEX_EMISSIONS: ClassVar[str] = "EEX-EMISSIONS"
    EEX_GAS: ClassVar[str] = "EEX-GAS"
    EEX_POWER: ClassVar[str] = "EEX-POWER"
    EURONEX_MATIF: ClassVar[str] = "EURONEX-MATIF"
    FERTECON: ClassVar[str] = "FERTECON"
    FERTILIZER_WEEK: ClassVar[str] = "FERTILIZER-WEEK"
    GAS_DAILY: ClassVar[str] = "GAS-DAILY"
    GAS_DAILY_PRICE_GUIDE: ClassVar[str] = "GAS-DAILY-PRICE-GUIDE"
    GLOBALCOAL: ClassVar[str] = "GLOBALCOAL"
    HEREN_REPORT: ClassVar[str] = "HEREN-REPORT"
    ICE_10X_DAILY: ClassVar[str] = "ICE/10X-DAILY"
    ICE_10X_MONTHLY: ClassVar[str] = "ICE/10X-MONTHLY"
    ICE_CANADA: ClassVar[str] = "ICE-CANADA"
    ICE_ECX: ClassVar[str] = "ICE-ECX"
    ICE_GAS: ClassVar[str] = "ICE-GAS"
    ICE_OIL: ClassVar[str] = "ICE-OIL"
    ICE_US_AGRICULTURAL: ClassVar[str] = "ICE-US-AGRICULTURAL"
    ICIS_PRICING_BENZENE__EUROPE_: ClassVar[str] = "ICIS-PRICING-BENZENE-(EUROPE)"
    ICIS_PRICING_ETHYLENE__EUROPE_: ClassVar[str] = "ICIS-PRICING-ETHYLENE-(EUROPE)"
    ICIS_PRICING_POLYPROPYLENE__EUROPE_: ClassVar[str] = "ICIS-PRICING-POLYPROPYLENE-(EUROPE)"
    INSIDE_FERC: ClassVar[str] = "INSIDE-FERC"
    JAPAN_MOF_TSRR: ClassVar[str] = "JAPAN-MOF-TSRR"
    KCBOT: ClassVar[str] = "KCBOT"
    KUALA_LUMPUR_BANK: ClassVar[str] = "KUALA-LUMPUR-BANK"
    LABUAN_BANK: ClassVar[str] = "LABUAN-BANK"
    LIFFE_LONDON_SOFT: ClassVar[str] = "LIFFE-LONDON-SOFT"
    LME: ClassVar[str] = "LME"
    LONDON_BULLION_MARKET: ClassVar[str] = "LONDON-BULLION-MARKET"
    LONDON_BULLION_MARKET_GOLD_A_M_ONLY: ClassVar[str] = "LONDON-BULLION-MARKET-GOLD-A.M-ONLY"
    LONDON_PLATINUM_PALLADIUM_MARKET: ClassVar[str] = "LONDON-PLATINUM-PALLADIUM-MARKET"
    MGEX: ClassVar[str] = "MGEX"
    N2EX: ClassVar[str] = "N2EX"
    NASDAQ_OMX: ClassVar[str] = "NASDAQ-OMX"
    NATURAL_GAS_WEEK: ClassVar[str] = "NATURAL-GAS-WEEK"
    NERC: ClassVar[str] = "NERC"
    NGI: ClassVar[str] = "NGI"
    NGX: ClassVar[str] = "NGX"
    NUCLEAR_MARKET_REVIEW: ClassVar[str] = "NUCLEAR-MARKET-REVIEW"
    NYMEX_ELECTRICITY: ClassVar[str] = "NYMEX-ELECTRICITY"
    NYMEX_GAS: ClassVar[str] = "NYMEX-GAS"
    NYMEX_NATURAL_GAS: ClassVar[str] = "NYMEX-NATURAL-GAS"
    NYMEX_OIL: ClassVar[str] = "NYMEX-OIL"
    OFFICIAL_BOARD_MARKETS: ClassVar[str] = "OFFICIAL-BOARD-MARKETS"
    OPIS_LP_GAS: ClassVar[str] = "OPIS-LP-GAS"
    OPIS_PROPANE: ClassVar[str] = "OPIS-PROPANE"
    PAPER_PACKAGING_MONITOR: ClassVar[str] = "PAPER-PACKAGING-MONITOR"
    PAPER_TRADER: ClassVar[str] = "PAPER-TRADER"
    PERTAMINA: ClassVar[str] = "PERTAMINA"
    PETROCHEMWIRE: ClassVar[str] = "PETROCHEMWIRE"
    PIX_PULP_BENCHMARK_INDICES: ClassVar[str] = "PIX-PULP-BENCHMARK-INDICES"
    PLATTS_APAG_MARKETSCAN: ClassVar[str] = "PLATTS-APAG-MARKETSCAN"
    PLATTS_BUNKERWIRE: ClassVar[str] = "PLATTS-BUNKERWIRE"
    PLATTS_CLEAN_TANKERWIRE: ClassVar[str] = "PLATTS-CLEAN-TANKERWIRE"
    PLATTS_CRUDE_OIL_MARKETWIRE: ClassVar[str] = "PLATTS-CRUDE-OIL-MARKETWIRE"
    PLATTS_DIRTY_TANKERWIRE: ClassVar[str] = "PLATTS-DIRTY-TANKERWIRE"
    PLATTS_EUROPEAN_GAS: ClassVar[str] = "PLATTS-EUROPEAN-GAS"
    PLATTS_EUROPEAN_MARKETSCAN: ClassVar[str] = "PLATTS-EUROPEAN-MARKETSCAN"
    PLATTS_METALS_ALERT: ClassVar[str] = "PLATTS-METALS-ALERT"
    PLATTS_OILGRAM: ClassVar[str] = "PLATTS-OILGRAM"
    PLATTS_TSI_IRON_ORE: ClassVar[str] = "PLATTS-TSI-IRON-ORE"
    PLATTS_TSI_SCRAP: ClassVar[str] = "PLATTS-TSI-SCRAP"
    PLATTS_TSI_STEEL: ClassVar[str] = "PLATTS-TSI-STEEL"
    PLATTS_US_MARKETSCAN: ClassVar[str] = "PLATTS-US-MARKETSCAN"
    PULP_AND_PAPER_INTERNATIONAL: ClassVar[str] = "PULP-AND-PAPER-INTERNATIONAL"
    PULP_AND_PAPER_WEEK: ClassVar[str] = "PULP-AND-PAPER-WEEK"
    RIM_PRODUCTS_INTELLIGENCE_DAILY: ClassVar[str] = "RIM-PRODUCTS-INTELLIGENCE-DAILY"
    SAFEX_SOFT: ClassVar[str] = "SAFEX-SOFT"
    SFE_SOFT: ClassVar[str] = "SFE-SOFT"
    SGX: ClassVar[str] = "SGX"
    SICOM: ClassVar[str] = "SICOM"
    SP_GSCI: ClassVar[str] = "SP-GSCI"
    STATISTICHES_BUNDESAMT: ClassVar[str] = "STATISTICHES-BUNDESAMT"
    TGE: ClassVar[str] = "TGE"
    TOCOM_OIL: ClassVar[str] = "TOCOM-OIL"
    TOCOM_PRECIOUS: ClassVar[str] = "TOCOM-PRECIOUS"
    TOCOM_SOFT: ClassVar[str] = "TOCOM-SOFT"
    UX_WEEKLY: ClassVar[str] = "UX-WEEKLY"
    WORLD_PULP_MONTHLY: ClassVar[str] = "WORLD-PULP-MONTHLY"


# Import after class definition to avoid circular imports
CommodityBusinessCalendarEnum.model_rebuild()
