"""
FPML to CDM mappers
"""
from .base import BaseFpMLMapper
from .fpml_trade_mapper import FpMLTradeMapper
from .credit_default_swap_mapper import FpMLCreditDefaultSwapMapper

# Import all mapper implementations
# This will be populated as mappers are implemented
mappers = {
    'FpMLTrade': FpMLTradeMapper,
    'FpMLCreditDefaultSwap': FpMLCreditDefaultSwapMapper,
}

__all__ = ['BaseFpMLMapper', 'mappers', 'FpMLTradeMapper', 'FpMLCreditDefaultSwapMapper'] 