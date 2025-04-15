from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CommodityReferencePriceEnum(CdmModelBase):
    """The enumeration values to specify the Commodity Reference Prices specified in the Annex to the 2005 ISDA Commodity Definitions."""
    # Enum values
    ALUMINIUM_ALLOY_LME_15_MONTH: ClassVar[str] = "ALUMINIUM ALLOY-LME 15 MONTH"
    COAL_CENTRAL_APPALACHIAN_NYMEX: ClassVar[str] = "COAL-CENTRAL APPALACHIAN-NYMEX"
    COCOA_ICE: ClassVar[str] = "COCOA-ICE"
    COFFEE_ARABICA_ICE: ClassVar[str] = "COFFEE ARABICA-ICE"
    COFFEE_ROBUSTA_ICE: ClassVar[str] = "COFFEE ROBUSTA-ICE"
    COPPER_COMEX: ClassVar[str] = "COPPER-COMEX"
    CORN_CBOT: ClassVar[str] = "CORN-CBOT"
    COTTON_NO__2_ICE: ClassVar[str] = "COTTON NO. 2-ICE"
    ETHANOL_CBOT: ClassVar[str] = "ETHANOL-CBOT"
    FEEDER_CATTLE_CME: ClassVar[str] = "FEEDER CATTLE-CME"
    FROZEN_CONCENTRATED_ORANGE_JUICE_NO__1_ICE: ClassVar[str] = "FROZEN CONCENTRATED ORANGE JUICE NO. 1-ICE"
    GASOLINE_RBOB_NEW_YORK_ICE: ClassVar[str] = "GASOLINE-RBOB-NEW YORK-ICE"
    GASOLINE_RBOB_NEW_YORK_NYMEX: ClassVar[str] = "GASOLINE-RBOB-NEW YORK-NYMEX"
    GOLD_COMEX: ClassVar[str] = "GOLD-COMEX"
    HEATING_OIL_NEW_YORK_NYMEX: ClassVar[str] = "HEATING OIL-NEW YORK-NYMEX"
    LEAN_HOGS_CME: ClassVar[str] = "LEAN HOGS-CME"
    LIVE_CATTLE_CME: ClassVar[str] = "LIVE CATTLE-CME"
    LUMBER_CME: ClassVar[str] = "LUMBER-CME"
    MILK_CLASS_III_CME: ClassVar[str] = "MILK-CLASS III-CME"
    MILK_NONFAT_DRY_CME: ClassVar[str] = "MILK-NONFAT-DRY-CME"
    NATURAL_GAS_NYMEX: ClassVar[str] = "NATURAL GAS-NYMEX"
    NATURAL_GAS_PEPL__TEXOK_MAINLINE__INSIDE_FERC: ClassVar[str] = "NATURAL GAS-PEPL (TEXOK MAINLINE)-INSIDE FERC"
    NATURAL_GAS_W__TEXAS__WAHA__INSIDE_FERC: ClassVar[str] = "NATURAL GAS-W. TEXAS (WAHA)-INSIDE FERC"
    OATS_CBOT: ClassVar[str] = "OATS-CBOT"
    OIL_WTI_NYMEX: ClassVar[str] = "OIL-WTI-NYMEX"
    PALLADIUM_NYMEX: ClassVar[str] = "PALLADIUM-NYMEX"
    PLATINUM_NYMEX: ClassVar[str] = "PLATINUM-NYMEX"
    RICE_CBOT: ClassVar[str] = "RICE-CBOT"
    SILVER_COMEX: ClassVar[str] = "SILVER-COMEX"
    SOYBEANS_CBOT: ClassVar[str] = "SOYBEANS-CBOT"
    SOYBEAN_MEAL_CBOT: ClassVar[str] = "SOYBEAN MEAL-CBOT"
    SOYBEAN_OIL_CBOT: ClassVar[str] = "SOYBEAN OIL-CBOT"
    SUGAR___11__WORLD__ICE: ClassVar[str] = "SUGAR # 11 (WORLD)-ICE"
    SUGAR___16__US__ICE: ClassVar[str] = "SUGAR # 16 (US)-ICE"
    WHEAT_CBOT: ClassVar[str] = "WHEAT-CBOT"
    WHEAT_HRW_KCBOT: ClassVar[str] = "WHEAT HRW-KCBOT"
    WHEAT_RED_SPRING_MGE: ClassVar[str] = "WHEAT RED SPRING-MGE"


# Import after class definition to avoid circular imports
CommodityReferencePriceEnum.model_rebuild()
