from typing import Dict, Any, Optional
import logging
from datetime import datetime

from .base import BaseFIXMapper
from src.models.fix.generated.messages.executionreport import ExecutionReport
from src.models.cdm.generated.event.workflow.workflow_step import WorkflowStep
from src.models.cdm.generated.event.common.business_event import BusinessEvent
from src.models.cdm.generated.event.common.trade.execution_details import ExecutionDetails

class ExecutionReportMapper(BaseFIXMapper):
    """
    Mapper for FIX ExecutionReport to CDM WorkflowStep
    """
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize the ExecutionReport mapper
        
        Args:
            config_file: Optional path to YAML configuration file
            If not provided, will use default config location
        """
        super().__init__(config_file)
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def apply_custom_mappings(self, source_obj: ExecutionReport, target_obj: WorkflowStep) -> None:
        """
        Apply custom mappings that cannot be defined in YAML
        
        Args:
            source_obj: FIX ExecutionReport to map from
            target_obj: CDM WorkflowStep to map to
        """
        # Ensure business_event is initialized
        if not hasattr(target_obj, 'business_event') or target_obj.business_event is None:
            target_obj.business_event = BusinessEvent()
        
        # Add timestamp qualifier
        if hasattr(target_obj, 'timestamp') and target_obj.timestamp and len(target_obj.timestamp) > 0:
            from src.models.cdm.generated.event.workflow.event_timestamp_qualification_enum import EventTimestampQualificationEnum
            target_obj.timestamp[0].qualification = EventTimestampQualificationEnum.EXECUTION_DATETIME
        
        # Set action type based on ExecType
        if hasattr(source_obj, 'ExecType'):
            from src.models.cdm.generated.event.common.action_enum import ActionEnum
            exec_type = source_obj.ExecType
            
            if exec_type == '0':  # New
                target_obj.action = ActionEnum.NEW
            elif exec_type in ('1', '2'):  # Partial Fill, Fill
                target_obj.action = ActionEnum.NEW
            elif exec_type == '4':  # Canceled
                target_obj.action = ActionEnum.CANCEL
            elif exec_type == '5':  # Replaced
                target_obj.action = ActionEnum.CORRECT
            else:
                target_obj.action = ActionEnum.NEW
        
        # Set up execution details if not already present
        if hasattr(target_obj.business_event, 'trade') and target_obj.business_event.trade is not None:
            if not hasattr(target_obj.business_event.trade, 'execution_details') or target_obj.business_event.trade.execution_details is None:
                target_obj.business_event.trade.execution_details = ExecutionDetails()
        
        # Add party information if available
        if hasattr(source_obj, 'SenderCompID') or hasattr(source_obj, 'TargetCompID'):
            from src.models.cdm.generated.base.staticdata.party.party import Party
            from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
            
            if not hasattr(target_obj, 'party'):
                target_obj.party = []
            
            # Add sender as party
            if hasattr(source_obj, 'SenderCompID'):
                sender_party = Party()
                sender_party.name = {"value": source_obj.SenderCompID}
                sender_party.party_id = {"value": source_obj.SenderCompID}
                sender_party.party_role = [PartyRoleEnum.EXECUTING_ENTITY]
                target_obj.party.append(sender_party)
            
            # Add target as party
            if hasattr(source_obj, 'TargetCompID'):
                target_party = Party()
                target_party.name = {"value": source_obj.TargetCompID}
                target_party.party_id = {"value": source_obj.TargetCompID}
                target_party.party_role = [PartyRoleEnum.CLIENT]
                target_obj.party.append(target_party)
        
        # Additional custom mappings as needed
        self._map_complex_trade_information(source_obj, target_obj)
    
    def _map_complex_trade_information(self, source_obj: ExecutionReport, target_obj: WorkflowStep) -> None:
        """
        Map complex trade information that requires special handling
        
        Args:
            source_obj: FIX ExecutionReport to map from
            target_obj: CDM WorkflowStep to map to
        """
        # Map account information if available
        if hasattr(source_obj, 'Account') and source_obj.Account:
            from src.models.cdm.generated.base.staticdata.party.account import Account
            
            account = Account()
            account.account_id = {"value": source_obj.Account}
            
            if not hasattr(target_obj, 'account'):
                target_obj.account = []
            
            target_obj.account.append(account)
        
        # Add execution details like commission if available
        if hasattr(target_obj.business_event, 'trade') and target_obj.business_event.trade is not None:
            if hasattr(source_obj, 'Commission') and source_obj.Commission:
                if not hasattr(target_obj.business_event.trade.execution_details, 'commission'):
                    from src.models.cdm.generated.event.common.trade.execution_commission import ExecutionCommission
                    
                    commission = ExecutionCommission()
                    commission.commission_amount = {"amount": float(source_obj.Commission)}
                    
                    if hasattr(source_obj, 'CommType'):
                        commission.commission_type = source_obj.CommType
                    
                    if hasattr(source_obj, 'Currency'):
                        commission.commission_amount.currency = {"value": source_obj.Currency}
                    
                    target_obj.business_event.trade.execution_details.commission = commission 