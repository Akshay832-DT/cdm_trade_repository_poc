"""
FIX to CDM mappers
"""
from .base import BaseFIXMapper
from .execution_report_mapper import ExecutionReportMapper
from .trade_capture_report_mapper import TradeCaptureReportMapper

# Import all mapper implementations
# This will be populated as mappers are implemented
mappers = {
    'ExecutionReport': ExecutionReportMapper,
    'TradeCaptureReport': TradeCaptureReportMapper,
}

__all__ = ['BaseFIXMapper', 'mappers', 'ExecutionReportMapper', 'TradeCaptureReportMapper'] 