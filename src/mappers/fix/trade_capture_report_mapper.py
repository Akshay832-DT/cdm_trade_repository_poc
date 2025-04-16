from typing import Dict, Any, Optional, List
import logging
from datetime import datetime

from .base import BaseFIXMapper
from src.models.fix.generated.messages.tradecapturereport import TradeCaptureReport
from src.models.cdm.generated.event.workflow.workflow_step import WorkflowStep
from src.models.cdm.generated.event.common.business_event import BusinessEvent
from src.models.cdm.generated.event.common.trade.trade import Trade
from src.models.cdm.generated.event.common.trade.execution_details import ExecutionDetails
from src.models.cdm.generated.event.common.action_enum import ActionEnum
from src.models.cdm.generated.event.workflow.event_timestamp import EventTimestamp
from src.models.cdm.generated.event.workflow.event_timestamp_qualification_enum import EventTimestampQualificationEnum
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum

class TradeCaptureReportMapper(BaseFIXMapper):
    """
    Mapper for FIX TradeCaptureReport to CDM WorkflowStep
    """
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize the TradeCaptureReport mapper
        
        Args:
            config_file: Optional path to YAML configuration file
            If not provided, will use default config location
        """
        super().__init__(config_file)
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def apply_custom_mappings(self, source_obj: TradeCaptureReport, target_obj: WorkflowStep) -> None:
        """
        Apply custom mappings that cannot be defined in YAML
        
        Args:
            source_obj: FIX TradeCaptureReport to map from
            target_obj: CDM WorkflowStep to map to
        """
        # Ensure business_event is initialized
        if not hasattr(target_obj, 'business_event') or target_obj.business_event is None:
            target_obj.business_event = BusinessEvent()
        
        # Ensure trade is initialized
        if not hasattr(target_obj.business_event, 'trade') or target_obj.business_event.trade is None:
            target_obj.business_event.trade = Trade()
        
        # Add timestamp qualifier if timestamp exists
        if hasattr(target_obj, 'timestamp') and target_obj.timestamp and len(target_obj.timestamp) > 0:
            target_obj.timestamp[0].qualification = EventTimestampQualificationEnum.TRADE_DATE
        
        # Set action type based on TradeReportType
        if hasattr(source_obj, 'TradeReportType'):
            trade_report_type = source_obj.TradeReportType
            
            if trade_report_type == '0':  # New
                target_obj.action = ActionEnum.NEW
            elif trade_report_type == '1':  # Cancel
                target_obj.action = ActionEnum.CANCEL
            elif trade_report_type == '2':  # Replace
                target_obj.action = ActionEnum.CORRECT
            elif trade_report_type == '3':  # Release
                target_obj.action = ActionEnum.NEW
            elif trade_report_type == '4':  # Reverse
                target_obj.action = ActionEnum.CANCEL
            elif trade_report_type == '5':  # Cancel Due To Back Out Agreement
                target_obj.action = ActionEnum.CANCEL
            else:
                target_obj.action = ActionEnum.NEW
        
        # Ensure execution details are initialized
        if not hasattr(target_obj.business_event.trade, 'execution_details') or target_obj.business_event.trade.execution_details is None:
            target_obj.business_event.trade.execution_details = ExecutionDetails()
        
        # Map trade reference information
        self._map_trade_references(source_obj, target_obj)
        
        # Map parties more comprehensively (handling repeating groups)
        self._map_parties(source_obj, target_obj)
        
        # Map instrument identifiers more comprehensively
        self._map_instrument_identifiers(source_obj, target_obj)
        
        # Map underlying instruments if present
        self._map_underlying_instruments(source_obj, target_obj)
    
    def _map_trade_references(self, source_obj: TradeCaptureReport, target_obj: WorkflowStep) -> None:
        """
        Map trade reference identifiers
        
        Args:
            source_obj: FIX TradeCaptureReport to map from
            target_obj: CDM WorkflowStep to map to
        """
        from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
        
        # Add execution ID to identifiers if not already mapped
        if hasattr(source_obj, 'ExecID') and source_obj.ExecID:
            if not hasattr(target_obj, 'event_identifier'):
                target_obj.event_identifier = []
            
            # Only add if no identifier with same value exists
            exists = False
            for event_id in target_obj.event_identifier:
                if event_id.identifier.value == source_obj.ExecID:
                    exists = True
                    break
            
            if not exists:
                exec_id = Identifier()
                exec_id.identifier = {"value": source_obj.ExecID}
                exec_id.issuer = {"reference": {"value": "EXECUTION_SYSTEM"}}
                target_obj.event_identifier.append(exec_id)
        
        # Map regulatory trade identifiers
        if hasattr(source_obj, 'TrdRegTimestamps'):
            # Map regulatory timestamps as regular timestamps
            # This would normally be a repeating group in FIX
            # As a placeholder, we'd handle each timestamp in the group
            if not hasattr(target_obj, 'timestamp'):
                target_obj.timestamp = []
            
            # In a real implementation, would handle the TrdRegTimestamps repeating group
            # For demonstration, adding a placeholder timestamp when TrdRegTimestamps exists
            if hasattr(source_obj, 'TransactTime') and len(target_obj.timestamp) == 0:
                timestamp = EventTimestamp()
                timestamp.value = source_obj.TransactTime
                timestamp.qualification = EventTimestampQualificationEnum.EXECUTION_DATETIME
                target_obj.timestamp.append(timestamp)
    
    def _map_parties(self, source_obj: TradeCaptureReport, target_obj: WorkflowStep) -> None:
        """
        Map party information comprehensively
        
        Args:
            source_obj: FIX TradeCaptureReport to map from
            target_obj: CDM WorkflowStep to map to
        """
        # Ensure party list is initialized
        if not hasattr(target_obj, 'party'):
            target_obj.party = []
        
        # Map reporting party if present
        if hasattr(source_obj, 'ReportingPartyID') and source_obj.ReportingPartyID:
            reporting_party = Party()
            reporting_party.party_id = {"value": source_obj.ReportingPartyID}
            reporting_party.name = {"value": source_obj.ReportingPartyID}
            
            # Set role based on ReportingPartyRole if present
            if hasattr(source_obj, 'ReportingPartyRole'):
                role = self._map_party_role(source_obj.ReportingPartyRole)
                reporting_party.party_role = [role]
            else:
                reporting_party.party_role = [PartyRoleEnum.REPORTING_PARTY]
            
            target_obj.party.append(reporting_party)
        
        # Map contra party if present
        if hasattr(source_obj, 'ContraPartyID') and source_obj.ContraPartyID:
            contra_party = Party()
            contra_party.party_id = {"value": source_obj.ContraPartyID}
            contra_party.name = {"value": source_obj.ContraPartyID}
            
            # Set role based on ContraPartyRole if present
            if hasattr(source_obj, 'ContraPartyRole'):
                role = self._map_party_role(source_obj.ContraPartyRole, is_contra=True)
                contra_party.party_role = [role]
            else:
                contra_party.party_role = [PartyRoleEnum.COUNTERPARTY]
            
            target_obj.party.append(contra_party)
        
        # In a real implementation, would handle the NoPartyIDs repeating group
        # This would involve looping through party IDs, roles, and sources
    
    def _map_party_role(self, role_code: str, is_contra: bool = False) -> PartyRoleEnum:
        """
        Map FIX party role code to CDM PartyRoleEnum
        
        Args:
            role_code: FIX role code
            is_contra: Whether this is a contra party
            
        Returns:
            CDM PartyRoleEnum
        """
        # Default roles
        default_role = PartyRoleEnum.COUNTERPARTY if is_contra else PartyRoleEnum.EXECUTING_ENTITY
        
        # Common role mapping
        role_map = {
            "1": PartyRoleEnum.EXECUTING_ENTITY,
            "2": PartyRoleEnum.BROKER_OF_CREDIT,
            "3": PartyRoleEnum.CLIENT,
            "4": PartyRoleEnum.CLEARING_FIRM,
            "7": PartyRoleEnum.ENTERING_FIRM,
            "11": PartyRoleEnum.ORDER_ORIGINATION_TRADER,
            "12": PartyRoleEnum.EXECUTING_TRADER,
            "13": PartyRoleEnum.ORDER_ORIGINATION_FIRM,
            "14": PartyRoleEnum.GIVEUP_CLEARING_FIRM,
            "15": PartyRoleEnum.CORRESPONDENT_CLEARING_FIRM,
            "16": PartyRoleEnum.EXECUTING_SYSTEM,
            "17": PartyRoleEnum.CONTRA_FIRM,
            "18": PartyRoleEnum.CONTRA_CLEARING_FIRM,
            "19": PartyRoleEnum.SPONSORING_FIRM,
            "21": PartyRoleEnum.CLEARING_ORGANIZATION,
            "22": PartyRoleEnum.EXCHANGE,
            "24": PartyRoleEnum.CUSTOMER_ACCOUNT,
            "25": PartyRoleEnum.CORRESPONDENT_CLEARING_ORGANIZATION,
            "26": PartyRoleEnum.CORRESPONDENT_BROKER,
            "27": PartyRoleEnum.BUYER_SELLER,
            "28": PartyRoleEnum.CUSTODIAN,
            "29": PartyRoleEnum.INTERMEDIARY,
            "30": PartyRoleEnum.AGENT,
            "31": PartyRoleEnum.SUB_CUSTODIAN,
            "32": PartyRoleEnum.BENEFICIARY,
            "33": PartyRoleEnum.INTERESTED_PARTY,
            "34": PartyRoleEnum.REGULATORY_BODY,
            "35": PartyRoleEnum.LIQUIDITY_PROVIDER,
            "36": PartyRoleEnum.ENTERING_TRADER,
            "37": PartyRoleEnum.CONTRA_TRADER,
            "38": PartyRoleEnum.POSITION_ACCOUNT,
            "39": PartyRoleEnum.CONTRA_INVESTOR_ID,
            "40": PartyRoleEnum.TRANSFER_TO_FIRM,
            "41": PartyRoleEnum.CONTRA_POSITION_ACCOUNT,
            "42": PartyRoleEnum.CONTRA_EXCHANGE,
            "43": PartyRoleEnum.INTERNAL_CARRYING_FIRM,
            "44": PartyRoleEnum.CONTRA_INTERNAL_CARRYING_FIRM,
            "45": PartyRoleEnum.CLEARING_ACCOUNT,
            "46": PartyRoleEnum.ACCEPTABLE_SETTLING_COUNTERPARTY,
            "47": PartyRoleEnum.UNACCEPTABLE_SETTLING_COUNTERPARTY
        }
        
        return role_map.get(role_code, default_role)
    
    def _map_instrument_identifiers(self, source_obj: TradeCaptureReport, target_obj: WorkflowStep) -> None:
        """
        Map instrument identifiers
        
        Args:
            source_obj: FIX TradeCaptureReport to map from
            target_obj: CDM WorkflowStep to map to
        """
        # Ensure security product is initialized
        if not hasattr(target_obj.business_event.trade, 'product'):
            from src.models.cdm.generated.product.product import Product
            target_obj.business_event.trade.product = Product()
        
        if not hasattr(target_obj.business_event.trade.product, 'security'):
            from src.models.cdm.generated.product.security.security import Security
            target_obj.business_event.trade.product.security = Security()
        
        if not hasattr(target_obj.business_event.trade.product.security, 'security_details'):
            from src.models.cdm.generated.product.security.security_details import SecurityDetails
            target_obj.business_event.trade.product.security.security_details = SecurityDetails()
        
        # Now map additional security identifiers if not already mapped via YAML
        sec_details = target_obj.business_event.trade.product.security.security_details
        
        # Add instrument type if present
        if hasattr(source_obj, 'SecurityType') and source_obj.SecurityType:
            from src.models.cdm.generated.product.security.security_type_enum import SecurityTypeEnum
            
            # Map security type codes - this would be expanded in a real implementation
            sec_type_map = {
                "EQTY": SecurityTypeEnum.EQUITY,
                "CS": SecurityTypeEnum.COMMON_STOCK,
                "OPT": SecurityTypeEnum.OPTION,
                "FUT": SecurityTypeEnum.FUTURE,
                "BOND": SecurityTypeEnum.BOND,
                "FX": SecurityTypeEnum.FX,
                "FXSPOT": SecurityTypeEnum.FX_SPOT,
                "FXFWD": SecurityTypeEnum.FX_FORWARD
            }
            
            if not hasattr(sec_details, 'security_type'):
                sec_details.security_type = sec_type_map.get(source_obj.SecurityType, SecurityTypeEnum.OTHER)
    
    def _map_underlying_instruments(self, source_obj: TradeCaptureReport, target_obj: WorkflowStep) -> None:
        """
        Map underlying instrument information
        
        Args:
            source_obj: FIX TradeCaptureReport to map from
            target_obj: CDM WorkflowStep to map to
        """
        # In a real implementation, would handle the NoUnderlyings repeating group
        # For demonstration, check if basic underlying information is present
        if (hasattr(source_obj, 'UnderlyingSymbol') and source_obj.UnderlyingSymbol or
            hasattr(source_obj, 'UnderlyingSecurityID') and source_obj.UnderlyingSecurityID):
            
            # Ensure option product structure is initialized for underlying
            if not hasattr(target_obj.business_event.trade.product, 'option'):
                from src.models.cdm.generated.product.option.option import Option
                target_obj.business_event.trade.product.option = Option()
            
            # Set up underlying
            if not hasattr(target_obj.business_event.trade.product.option, 'underlier'):
                from src.models.cdm.generated.product.option.underlier import Underlier
                target_obj.business_event.trade.product.option.underlier = Underlier()
            
            # Map underlier product
            if not hasattr(target_obj.business_event.trade.product.option.underlier, 'security'):
                from src.models.cdm.generated.product.security.security import Security
                target_obj.business_event.trade.product.option.underlier.security = Security()
                
            # Add security details to underlying
            if not hasattr(target_obj.business_event.trade.product.option.underlier.security, 'security_details'):
                from src.models.cdm.generated.product.security.security_details import SecurityDetails
                target_obj.business_event.trade.product.option.underlier.security.security_details = SecurityDetails()
            
            # Map underlying symbol
            if hasattr(source_obj, 'UnderlyingSymbol') and source_obj.UnderlyingSymbol:
                target_obj.business_event.trade.product.option.underlier.security.security_details.instrument_details = {
                    "description": source_obj.UnderlyingSymbol
                }
            
            # Map underlying security ID
            if hasattr(source_obj, 'UnderlyingSecurityID') and source_obj.UnderlyingSecurityID:
                from src.models.cdm.generated.product.security.instrument_identification import InstrumentIdentification
                
                target_obj.business_event.trade.product.option.underlier.security.security_details.instrument_identification = InstrumentIdentification()
                target_obj.business_event.trade.product.option.underlier.security.security_details.instrument_identification.identifier = {
                    "value": source_obj.UnderlyingSecurityID
                }
                
                # Add ID source if available
                if hasattr(source_obj, 'UnderlyingSecurityIDSource') and source_obj.UnderlyingSecurityIDSource:
                    target_obj.business_event.trade.product.option.underlier.security.security_details.instrument_identification.identifier.issuer = {
                        "value": source_obj.UnderlyingSecurityIDSource
                    } 