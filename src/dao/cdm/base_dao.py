"""
Base DAO class that provides common functionality for all DAOs.
"""
import logging
from typing import Any, Dict, List, Optional, Type, TypeVar, Generic, Union
import psycopg
from pydantic import BaseModel

from .db_manager import db_manager

logger = logging.getLogger(__name__)

T = TypeVar('T', bound=BaseModel)

class BaseDAO(Generic[T]):
    """Base DAO class with common database operations."""
    
    def __init__(self, model_class: Type[T] = None):
        """Initialize base DAO with model class."""
        self.model_class = model_class
    
    def _get_connection(self) -> psycopg.Connection:
        """Get a database connection."""
        return db_manager.get_connection()
    
    def _return_connection(self, conn: psycopg.Connection) -> None:
        """Return a database connection to the pool."""
        db_manager.return_connection(conn)
    
    def execute_query(self, 
                     query: str, 
                     params: Optional[Dict[str, Any]] = None,
                     fetch: bool = True,
                     commit: bool = False) -> Union[List[Dict[str, Any]], None]:
        """
        Execute a SQL query and optionally fetch results.
        
        Args:
            query: SQL query to execute
            params: Query parameters
            fetch: Whether to fetch results
            commit: Whether to commit the transaction
            
        Returns:
            Query results as a list of dictionaries if fetch=True, else None
        """
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(query, params or {})
                if fetch:
                    results = cur.fetchall()
                else:
                    results = None
                
                if commit:
                    conn.commit()
                    
                return results
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            conn.rollback()
            raise
        finally:
            self._return_connection(conn)
    
    def execute_transaction(self, callback: callable, *args, **kwargs) -> Any:
        """
        Execute a callback function within a transaction.
        
        Args:
            callback: Function to execute within transaction
            args: Arguments to pass to callback
            kwargs: Keyword arguments to pass to callback
            
        Returns:
            Result of callback function
        """
        conn = self._get_connection()
        try:
            with conn.transaction():
                result = callback(conn, *args, **kwargs)
                return result
        except Exception as e:
            logger.error(f"Transaction error: {e}")
            raise
        finally:
            self._return_connection(conn)
    
    def get_by_id(self, table: str, id_value: int, schema: str = 'cdm') -> Optional[Dict[str, Any]]:
        """
        Get a record by ID.
        
        Args:
            table: Table name
            id_value: ID value
            schema: Database schema
            
        Returns:
            Record as dictionary or None if not found
        """
        query = f"SELECT * FROM {schema}.{table} WHERE id = %s"
        results = self.execute_query(query, {'id': id_value})
        return results[0] if results else None
    
    def insert(self, 
              table: str, 
              data: Dict[str, Any], 
              schema: str = 'cdm',
              return_id: bool = True) -> Union[int, None]:
        """
        Insert a record into a table.
        
        Args:
            table: Table name
            data: Data to insert
            schema: Database schema
            return_id: Whether to return the inserted ID
            
        Returns:
            Inserted ID if return_id=True, else None
        """
        # Filter out None values
        filtered_data = {k: v for k, v in data.items() if v is not None}
        
        columns = ', '.join(filtered_data.keys())
        placeholders = ', '.join([f"%({k})s" for k in filtered_data.keys()])
        
        query = f"INSERT INTO {schema}.{table} ({columns}) VALUES ({placeholders})"
        
        if return_id:
            query += " RETURNING id"
            
        results = self.execute_query(query, filtered_data, commit=True)
        if return_id and results:
            return results[0]['id']
        return None
    
    def update(self, 
              table: str, 
              id_value: int, 
              data: Dict[str, Any], 
              schema: str = 'cdm') -> bool:
        """
        Update a record in a table.
        
        Args:
            table: Table name
            id_value: ID of record to update
            data: Data to update
            schema: Database schema
            
        Returns:
            True if successful, False otherwise
        """
        # Filter out None values
        filtered_data = {k: v for k, v in data.items() if v is not None}
        
        # Add ID to data
        filtered_data['id'] = id_value
        
        set_clause = ', '.join([f"{k} = %({k})s" for k in filtered_data.keys() if k != 'id'])
        
        query = f"UPDATE {schema}.{table} SET {set_clause} WHERE id = %(id)s"
        
        self.execute_query(query, filtered_data, fetch=False, commit=True)
        return True
    
    def delete(self, table: str, id_value: int, schema: str = 'cdm') -> bool:
        """
        Delete a record from a table.
        
        Args:
            table: Table name
            id_value: ID of record to delete
            schema: Database schema
            
        Returns:
            True if successful, False otherwise
        """
        query = f"DELETE FROM {schema}.{table} WHERE id = %(id)s"
        self.execute_query(query, {'id': id_value}, fetch=False, commit=True)
        return True 