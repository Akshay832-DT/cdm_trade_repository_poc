"""
DAO for Trade entities.
"""
import logging
from typing import Dict, List, Optional, Any, Union
import uuid
import psycopg

from src.models.cdm.generated.event.common.trade import Trade
from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier
from .base_dao import BaseDAO
from .party_dao import PartyDAO

logger = logging.getLogger(__name__)

class TradeDAO(BaseDAO[Trade]):
    """DAO for Trade entities."""
    
    def __init__(self):
        """Initialize TradeDAO."""
        super().__init__(Trade)
        self.party_dao = PartyDAO()
    
    def save(self, trade: Trade) -> int:
        """
        Save a Trade entity to the database.
        
        Args:
            trade: Trade entity to save
            
        Returns:
            Database ID of the trade
        """
        # Execute within a transaction
        return self.execute_transaction(self._save_trade_transaction, trade)
    
    def _save_trade_transaction(self, conn: psycopg.Connection, trade: Trade) -> int:
        """
        Save a trade within a transaction.
        
        Args:
            conn: Database connection
            trade: Trade entity to save
            
        Returns:
            Database ID of the trade
        """
        # Check if trade exists by trade_id
        trade_id = self._get_trade_id(trade)
        existing_trade = self._get_by_trade_id(conn, trade_id)
        
        if existing_trade:
            return existing_trade['id']
        
        # Insert trade record
        trade_date = self._get_trade_date(trade)
        effective_date = self._get_effective_date(trade)
        termination_date = self._get_termination_date(trade)
        product_type = self._get_product_type(trade)
        
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO cdm.trade (
                    trade_id, trade_date, effective_date, termination_date, product_type
                ) VALUES (
                    %(trade_id)s, %(trade_date)s, %(effective_date)s, %(termination_date)s, %(product_type)s
                )
                RETURNING id
                """,
                {
                    'trade_id': trade_id,
                    'trade_date': trade_date,
                    'effective_date': effective_date,
                    'termination_date': termination_date,
                    'product_type': product_type
                }
            )
            trade_db_id = cur.fetchone()['id']
        
        # Save trade identifiers
        if hasattr(trade, 'trade_identifier') and trade.trade_identifier:
            self._save_trade_identifiers(conn, trade_db_id, trade.trade_identifier)
        
        # Save party roles
        if hasattr(trade, 'party') and trade.party:
            self._save_party_roles(conn, trade_db_id, trade.party)
            
        # Return the trade database ID
        return trade_db_id
    
    def get_by_id(self, id_value: int) -> Optional[Dict[str, Any]]:
        """
        Get a trade by database ID.
        
        Args:
            id_value: Database ID
            
        Returns:
            Trade record or None if not found
        """
        return super().get_by_id('trade', id_value)
    
    def get_by_trade_id(self, trade_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a trade by trade_id.
        
        Args:
            trade_id: Trade ID
            
        Returns:
            Trade record or None if not found
        """
        query = "SELECT * FROM cdm.trade WHERE trade_id = %(trade_id)s"
        results = self.execute_query(query, {'trade_id': trade_id})
        return results[0] if results else None
    
    def _get_by_trade_id(self, conn: psycopg.Connection, trade_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a trade by trade_id using a specific connection.
        
        Args:
            conn: Database connection
            trade_id: Trade ID
            
        Returns:
            Trade record or None if not found
        """
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM cdm.trade WHERE trade_id = %(trade_id)s",
                {'trade_id': trade_id}
            )
            result = cur.fetchone()
            return result
    
    def _save_trade_identifiers(self, 
                               conn: psycopg.Connection, 
                               trade_db_id: int, 
                               identifiers: List[TradeIdentifier]) -> None:
        """
        Save trade identifiers.
        
        Args:
            conn: Database connection
            trade_db_id: Trade database ID
            identifiers: List of trade identifiers
        """
        with conn.cursor() as cur:
            for identifier in identifiers:
                issuer = getattr(identifier, 'issuer', {}).get('value') if hasattr(identifier, 'issuer') else 'UNKNOWN'
                
                for assigned_id in getattr(identifier, 'assignedIdentifier', []):
                    id_value = getattr(assigned_id, 'identifier', {}).get('value') if hasattr(assigned_id, 'identifier') else None
                    id_type = getattr(assigned_id, 'identifier', {}).get('type') if hasattr(assigned_id, 'identifier') else None
                    
                    if id_value:
                        cur.execute(
                            """
                            INSERT INTO cdm.trade_identifier (
                                trade_id, issuer, identifier, identifier_type
                            ) VALUES (
                                %(trade_id)s, %(issuer)s, %(identifier)s, %(identifier_type)s
                            )
                            """,
                            {
                                'trade_id': trade_db_id,
                                'issuer': issuer,
                                'identifier': id_value,
                                'identifier_type': id_type
                            }
                        )
    
    def _save_party_roles(self, 
                         conn: psycopg.Connection, 
                         trade_db_id: int, 
                         parties: List[Any]) -> None:
        """
        Save party roles.
        
        Args:
            conn: Database connection
            trade_db_id: Trade database ID
            parties: List of parties
        """
        with conn.cursor() as cur:
            for party in parties:
                # Get or create party
                party_id = self.party_dao._get_party_id(party)
                party_name = self.party_dao._get_party_name(party)
                
                # First, try to find party in database
                cur.execute(
                    "SELECT id FROM cdm.party WHERE party_id = %(party_id)s",
                    {'party_id': party_id}
                )
                party_result = cur.fetchone()
                
                if party_result:
                    party_db_id = party_result['id']
                else:
                    # Create new party
                    cur.execute(
                        """
                        INSERT INTO cdm.party (party_id, name) 
                        VALUES (%(party_id)s, %(name)s)
                        RETURNING id
                        """,
                        {'party_id': party_id, 'name': party_name}
                    )
                    party_db_id = cur.fetchone()['id']
                
                # Determine role - for now just use a generic 'PARTY' role
                role = 'PARTY'
                
                # Insert party role
                cur.execute(
                    """
                    INSERT INTO cdm.trade_party_role (trade_id, party_id, role)
                    VALUES (%(trade_id)s, %(party_id)s, %(role)s)
                    ON CONFLICT (trade_id, party_id, role) DO NOTHING
                    """,
                    {
                        'trade_id': trade_db_id,
                        'party_id': party_db_id,
                        'role': role
                    }
                )
    
    def _get_trade_id(self, trade: Trade) -> str:
        """
        Get a trade ID from a Trade object.
        
        Args:
            trade: Trade object
            
        Returns:
            Trade ID
        """
        # Try to get from trade_identifier
        if hasattr(trade, 'trade_identifier') and trade.trade_identifier:
            for identifier in trade.trade_identifier:
                if hasattr(identifier, 'assignedIdentifier') and identifier.assignedIdentifier:
                    for assigned_id in identifier.assignedIdentifier:
                        if hasattr(assigned_id, 'identifier') and hasattr(assigned_id.identifier, 'value'):
                            return assigned_id.identifier.value
        
        # Generate a random ID as last resort
        return f"trade-{uuid.uuid4()}"
    
    def _get_trade_date(self, trade: Trade) -> Optional[str]:
        """
        Get trade date from a Trade object.
        
        Args:
            trade: Trade object
            
        Returns:
            Trade date or None if not found
        """
        if hasattr(trade, 'trade_date') and trade.trade_date:
            if hasattr(trade.trade_date, 'value'):
                return trade.trade_date.value
        return None
    
    def _get_effective_date(self, trade: Trade) -> Optional[str]:
        """
        Get effective date from a Trade object.
        
        Args:
            trade: Trade object
            
        Returns:
            Effective date or None if not found
        """
        # Different CDM versions might have different paths to effective date
        if hasattr(trade, 'effective_date'):
            if hasattr(trade.effective_date, 'adjustable_date'):
                if hasattr(trade.effective_date.adjustable_date, 'unadjusted_date'):
                    return trade.effective_date.adjustable_date.unadjusted_date
            elif hasattr(trade.effective_date, 'value'):
                return trade.effective_date.value
                
        return None
    
    def _get_termination_date(self, trade: Trade) -> Optional[str]:
        """
        Get termination date from a Trade object.
        
        Args:
            trade: Trade object
            
        Returns:
            Termination date or None if not found
        """
        # Different CDM versions might have different paths to termination date
        if hasattr(trade, 'termination_date'):
            if hasattr(trade.termination_date, 'adjustable_date'):
                if hasattr(trade.termination_date.adjustable_date, 'unadjusted_date'):
                    return trade.termination_date.adjustable_date.unadjusted_date
            elif hasattr(trade.termination_date, 'value'):
                return trade.termination_date.value
                
        return None
    
    def _get_product_type(self, trade: Trade) -> str:
        """
        Get product type from a Trade object.
        
        Args:
            trade: Trade object
            
        Returns:
            Product type or 'UNKNOWN' if not found
        """
        if hasattr(trade, 'product'):
            if hasattr(trade.product, 'contract_terms'):
                # Get the contract type
                if hasattr(trade.product.contract_terms, 'economicTerms'):
                    if hasattr(trade.product.contract_terms.economicTerms, 'payout'):
                        for payout in trade.product.contract_terms.economicTerms.payout:
                            if hasattr(payout, 'creditDefaultPayout'):
                                return 'CREDIT_DEFAULT_SWAP'
                            elif hasattr(payout, 'interestRatePayout'):
                                return 'INTEREST_RATE_SWAP'
                            elif hasattr(payout, 'equityPayout'):
                                return 'EQUITY_SWAP'
        
        return 'UNKNOWN'