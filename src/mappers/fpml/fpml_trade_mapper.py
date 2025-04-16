from typing import Dict, Any, Optional
import logging
from datetime import datetime

from .base import BaseFpMLMapper
from src.models.fpml.generated.trade.trade import FpMLTrade
from src.models.cdm.generated.event.workflow.workflow_step import WorkflowStep
from src.models.cdm.generated.event.common.business_event import BusinessEvent
from src.models.cdm.generated.event.common.trade import Trade

class FpMLTradeMapper(BaseFpMLMapper):
    """
    Mapper for FpML Trade to CDM WorkflowStep
    """
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize the FpML Trade mapper
        
        Args:
            config_file: Optional path to YAML configuration file
            If not provided, will use default config location
        """
        super().__init__(config_file)
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def apply_custom_mappings(self, source_obj: FpMLTrade, target_obj: WorkflowStep) -> None:
        """
        Apply custom mappings that cannot be defined in YAML
        
        Args:
            source_obj: FpML Trade to map from
            target_obj: CDM WorkflowStep to map to
        """
        # Ensure business_event is initialized
        if not hasattr(target_obj, 'business_event') or target_obj.business_event is None:
            target_obj.business_event = BusinessEvent()
        
        # Ensure trade is initialized
        if not hasattr(target_obj.business_event, 'trade') or target_obj.business_event.trade is None:
            target_obj.business_event.trade = Trade()
        
        # Set action type
        from src.models.cdm.generated.event.common.action_enum import ActionEnum
        target_obj.action = ActionEnum.NEW
        
        # Add timestamp with trade date
        if hasattr(source_obj, 'tradeHeader') and hasattr(source_obj.tradeHeader, 'tradeDate'):
            from src.models.cdm.generated.event.workflow.event_timestamp import EventTimestamp
            from src.models.cdm.generated.event.workflow.event_timestamp_qualification_enum import EventTimestampQualificationEnum
            
            if not hasattr(target_obj, 'timestamp'):
                target_obj.timestamp = []
            
            timestamp = EventTimestamp()
            timestamp.value = source_obj.tradeHeader.tradeDate
            timestamp.qualification = EventTimestampQualificationEnum.TRADE_DATE
            
            target_obj.timestamp.append(timestamp)
        
        # Add event identifier
        if hasattr(source_obj, 'tradeHeader') and hasattr(source_obj.tradeHeader, 'partyTradeIdentifier'):
            from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
            
            if not hasattr(target_obj, 'event_identifier'):
                target_obj.event_identifier = []
            
            for party_trade_id in source_obj.tradeHeader.partyTradeIdentifier:
                event_id = Identifier()
                event_id.identifier = {"value": party_trade_id.tradeId}
                event_id.issuer = {"reference": {"value": party_trade_id.partyReference.href}}
                
                target_obj.event_identifier.append(event_id)
        
        # Map parties
        self._map_parties(source_obj, target_obj)
        
        # Map product details based on product type
        self._map_product_details(source_obj, target_obj)
    
    def _map_parties(self, source_obj: FpMLTrade, target_obj: WorkflowStep) -> None:
        """
        Map party information from FpML to CDM
        
        Args:
            source_obj: FpML Trade to map from
            target_obj: CDM WorkflowStep to map to
        """
        if not hasattr(source_obj, 'tradeHeader') or not hasattr(source_obj.tradeHeader, 'partyTradeIdentifier'):
            return
        
        from src.models.cdm.generated.base.staticdata.party.party import Party
        from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
        
        if not hasattr(target_obj, 'party'):
            target_obj.party = []
        
        # Map parties from partyTradeIdentifier
        party_refs = set()
        for party_trade_id in source_obj.tradeHeader.partyTradeIdentifier:
            party_ref = party_trade_id.partyReference.href
            
            if party_ref not in party_refs:
                party = Party()
                party.party_id = {"value": party_ref}
                party.name = {"value": f"Party {party_ref}"}  # Use actual party name if available
                
                # Set party role - this would require more context in a real implementation
                party.party_role = [PartyRoleEnum.TRADE_PARTY]
                
                target_obj.party.append(party)
                party_refs.add(party_ref)
        
        # Map party roles from product structure if available
        if hasattr(source_obj, 'product'):
            # Interest rate product
            if hasattr(source_obj.product, 'interestRate') and source_obj.product.interestRate:
                if hasattr(source_obj.product.interestRate, 'swapStream'):
                    for i, swap_stream in enumerate(source_obj.product.interestRate.swapStream):
                        if hasattr(swap_stream, 'payerReceiver'):
                            payer_ref = swap_stream.payerReceiver.payerPartyReference.href
                            receiver_ref = swap_stream.payerReceiver.receiverPartyReference.href
                            
                            # Update payer party
                            for party in target_obj.party:
                                if party.party_id.value == payer_ref:
                                    if PartyRoleEnum.PAYER not in party.party_role:
                                        party.party_role.append(PartyRoleEnum.PAYER)
                                
                                if party.party_id.value == receiver_ref:
                                    if PartyRoleEnum.RECEIVER not in party.party_role:
                                        party.party_role.append(PartyRoleEnum.RECEIVER)
    
    def _map_product_details(self, source_obj: FpMLTrade, target_obj: WorkflowStep) -> None:
        """
        Map product details based on product type
        
        Args:
            source_obj: FpML Trade to map from
            target_obj: CDM WorkflowStep to map to
        """
        if not hasattr(source_obj, 'product'):
            return
        
        # Map interest rate product (swap)
        if hasattr(source_obj.product, 'interestRate') and source_obj.product.interestRate:
            self._map_interest_rate_product(source_obj, target_obj)
        
        # Map credit product (CDS)
        elif hasattr(source_obj.product, 'credit') and source_obj.product.credit:
            self._map_credit_product(source_obj, target_obj)
    
    def _map_interest_rate_product(self, source_obj: FpMLTrade, target_obj: WorkflowStep) -> None:
        """
        Map interest rate product details
        
        Args:
            source_obj: FpML Trade to map from
            target_obj: CDM WorkflowStep to map to
        """
        from src.models.cdm.generated.product.product import Product
        from src.models.cdm.generated.product.interest_rate.swap.swap import Swap
        
        # Initialize product structure if needed
        if not hasattr(target_obj.business_event.trade, 'product'):
            target_obj.business_event.trade.product = Product()
        
        # Set product type to swap
        if not hasattr(target_obj.business_event.trade.product, 'contract_terms'):
            from src.models.cdm.generated.product.contract_terms import ContractTerms
            target_obj.business_event.trade.product.contract_terms = ContractTerms()
        
        # Initialize swap structure
        if not hasattr(target_obj.business_event.trade.product.contract_terms, 'swap'):
            target_obj.business_event.trade.product.contract_terms.swap = Swap()
        
        # Map swap streams
        if hasattr(source_obj.product.interestRate, 'swapStream'):
            from src.models.cdm.generated.product.interest_rate.swap.swap_stream import SwapStream
            
            if not hasattr(target_obj.business_event.trade.product.contract_terms.swap, 'swap_stream'):
                target_obj.business_event.trade.product.contract_terms.swap.swap_stream = []
            
            for i, source_stream in enumerate(source_obj.product.interestRate.swapStream):
                cdm_stream = SwapStream()
                
                # Map payer/receiver
                if hasattr(source_stream, 'payerReceiver'):
                    from src.models.cdm.generated.product.common.payer_receiver import PayerReceiver
                    
                    cdm_stream.payer_receiver = PayerReceiver()
                    
                    # Map payer
                    if hasattr(source_stream.payerReceiver, 'payerPartyReference'):
                        from src.models.cdm.generated.base.staticdata.reference.party_reference import PartyReference
                        
                        cdm_stream.payer_receiver.payer = PartyReference()
                        cdm_stream.payer_receiver.payer.reference = {
                            "value": source_stream.payerReceiver.payerPartyReference.href
                        }
                    
                    # Map receiver
                    if hasattr(source_stream.payerReceiver, 'receiverPartyReference'):
                        from src.models.cdm.generated.base.staticdata.reference.party_reference import PartyReference
                        
                        cdm_stream.payer_receiver.receiver = PartyReference()
                        cdm_stream.payer_receiver.receiver.reference = {
                            "value": source_stream.payerReceiver.receiverPartyReference.href
                        }
                
                # Map notional amount
                if hasattr(source_stream, 'notionalAmount'):
                    from src.models.cdm.generated.product.interest_rate.swap.calculation_period_amount import CalculationPeriodAmount
                    from src.models.cdm.generated.product.interest_rate.swap.calculation import Calculation
                    from src.models.cdm.generated.product.common.notional_amount import NotionalAmount
                    from src.models.cdm.generated.product.common.money import Money
                    
                    cdm_stream.calculation_period_amount = CalculationPeriodAmount()
                    cdm_stream.calculation_period_amount.calculation = Calculation()
                    cdm_stream.calculation_period_amount.calculation.notional_amount = NotionalAmount()
                    cdm_stream.calculation_period_amount.calculation.notional_amount.amount = Money()
                    
                    cdm_stream.calculation_period_amount.calculation.notional_amount.amount.amount = source_stream.notionalAmount.amount
                    
                    if hasattr(source_stream.notionalAmount, 'currency'):
                        cdm_stream.calculation_period_amount.calculation.notional_amount.amount.currency = {
                            "value": source_stream.notionalAmount.currency
                        }
                
                # Add to swap streams
                target_obj.business_event.trade.product.contract_terms.swap.swap_stream.append(cdm_stream)
    
    def _map_credit_product(self, source_obj: FpMLTrade, target_obj: WorkflowStep) -> None:
        """
        Map credit product details
        
        Args:
            source_obj: FpML Trade to map from
            target_obj: CDM WorkflowStep to map to
        """
        from src.models.cdm.generated.product.product import Product
        from src.models.cdm.generated.product.credit.credit_default_swap.credit_default_swap import CreditDefaultSwap
        
        # Initialize product structure if needed
        if not hasattr(target_obj.business_event.trade, 'product'):
            target_obj.business_event.trade.product = Product()
        
        # Set product type to CDS
        if not hasattr(target_obj.business_event.trade.product, 'contract_terms'):
            from src.models.cdm.generated.product.contract_terms import ContractTerms
            target_obj.business_event.trade.product.contract_terms = ContractTerms()
        
        # Initialize CDS structure
        if not hasattr(target_obj.business_event.trade.product.contract_terms, 'credit_default_swap'):
            target_obj.business_event.trade.product.contract_terms.credit_default_swap = CreditDefaultSwap()
        
        # Map general terms
        if hasattr(source_obj.product.credit, 'protectionTerms') or hasattr(source_obj.product.credit, 'referenceInformation'):
            from src.models.cdm.generated.product.credit.credit_default_swap.general_terms import GeneralTerms
            from src.models.cdm.generated.product.credit.credit_default_swap.reference_information import ReferenceInformation
            from src.models.cdm.generated.product.credit.credit_default_swap.reference_entity import ReferenceEntity
            from src.models.cdm.generated.product.credit.credit_default_swap.legal_entity import LegalEntity
            
            # Initialize general terms
            if not hasattr(target_obj.business_event.trade.product.contract_terms.credit_default_swap, 'general_terms'):
                target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms = GeneralTerms()
            
            # Initialize reference information
            if not hasattr(target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms, 'reference_information'):
                target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms.reference_information = ReferenceInformation()
            
            # Map reference entity
            ref_entity = None
            if hasattr(source_obj.product.credit, 'protectionTerms') and hasattr(source_obj.product.credit.protectionTerms, 'referenceEntity'):
                ref_entity = source_obj.product.credit.protectionTerms.referenceEntity
            elif hasattr(source_obj.product.credit, 'referenceInformation') and hasattr(source_obj.product.credit.referenceInformation, 'referenceEntity'):
                ref_entity = source_obj.product.credit.referenceInformation.referenceEntity
            
            if ref_entity:
                # Initialize reference entity
                if not hasattr(target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms.reference_information, 'reference_entity'):
                    target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms.reference_information.reference_entity = ReferenceEntity()
                
                # Set reference entity name
                if not hasattr(target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms.reference_information.reference_entity, 'reference_entity_name'):
                    target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms.reference_information.reference_entity.reference_entity_name = LegalEntity()
                
                target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms.reference_information.reference_entity.reference_entity_name.name = {"value": ref_entity}
            
            # Map reference obligation
            if hasattr(source_obj.product.credit, 'referenceInformation') and hasattr(source_obj.product.credit.referenceInformation, 'referenceObligation'):
                from src.models.cdm.generated.product.credit.credit_default_swap.reference_obligation import ReferenceObligation
                
                if not hasattr(target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms.reference_information, 'reference_obligation'):
                    target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms.reference_information.reference_obligation = ReferenceObligation()
                
                target_obj.business_event.trade.product.contract_terms.credit_default_swap.general_terms.reference_information.reference_obligation.reference_obligation_description = source_obj.product.credit.referenceInformation.referenceObligation 