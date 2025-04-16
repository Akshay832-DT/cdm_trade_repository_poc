"""
DAO for Party entities.
"""
import logging
from typing import Dict, List, Optional, Any, Union
import uuid

from src.models.cdm.generated.base.staticdata.party.party import Party
from .base_dao import BaseDAO

logger = logging.getLogger(__name__)

class PartyDAO(BaseDAO[Party]):
    """DAO for Party entities."""
    
    def __init__(self):
        """Initialize PartyDAO."""
        super().__init__(Party)
    
    def save(self, party: Party) -> int:
        """
        Save a Party entity to the database.
        
        Args:
            party: Party entity to save
            
        Returns:
            Database ID of the party
        """
        # Check if party exists by party_id
        party_id = self._get_party_id(party)
        existing_party = self.get_by_party_id(party_id)
        
        if existing_party:
            return existing_party['id']
        
        # Insert new party
        data = {
            'party_id': party_id,
            'name': self._get_party_name(party)
        }
        
        return self.insert('party', data)
    
    def get_by_party_id(self, party_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a party by party_id.
        
        Args:
            party_id: Party ID
            
        Returns:
            Party record or None if not found
        """
        query = "SELECT * FROM cdm.party WHERE party_id = %(party_id)s"
        results = self.execute_query(query, {'party_id': party_id})
        return results[0] if results else None
    
    def find_or_create(self, party_id: str, name: str) -> int:
        """
        Find or create a party.
        
        Args:
            party_id: Party ID
            name: Party name
            
        Returns:
            Database ID of the party
        """
        existing = self.get_by_party_id(party_id)
        if existing:
            return existing['id']
        
        data = {
            'party_id': party_id,
            'name': name
        }
        
        return self.insert('party', data)
    
    def _get_party_id(self, party: Party) -> str:
        """
        Get a party ID from a Party object.
        
        Args:
            party: Party object
            
        Returns:
            Party ID
        """
        # Try to get ID from various party fields
        if hasattr(party, 'id') and party.id:
            return party.id
        
        if hasattr(party, 'party_id') and party.party_id:
            return party.party_id
        
        if hasattr(party, 'name') and party.name:
            # Create a deterministic ID based on name
            return f"party-{party.name.lower().replace(' ', '-')}"
        
        # Generate a random ID as last resort
        return f"party-{uuid.uuid4()}"
    
    def _get_party_name(self, party: Party) -> str:
        """
        Get a party name from a Party object.
        
        Args:
            party: Party object
            
        Returns:
            Party name
        """
        if hasattr(party, 'name') and party.name:
            return party.name
        
        # Try to get name from party_id
        party_id = self._get_party_id(party)
        if party_id.startswith('party-'):
            return party_id[6:].replace('-', ' ').title()
        
        return party_id 