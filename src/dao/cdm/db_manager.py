"""
Database manager for CDM trade repository.
Handles connection pooling and transaction management.
"""
import os
import logging
from typing import Optional, Any
import psycopg
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool

logger = logging.getLogger(__name__)

class DatabaseManager:
    """Database manager for CDM trade repository."""
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        """Implement singleton pattern."""
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, 
                 host: str = None, 
                 port: int = None, 
                 database: str = None, 
                 user: str = None, 
                 password: str = None):
        """Initialize database manager with connection parameters."""
        if self._initialized:
            return
        
        # Use parameters or environment variables
        self.host = host or os.environ.get('DB_HOST', 'localhost')
        self.port = port or int(os.environ.get('DB_PORT', 5432))
        self.database = database or os.environ.get('DB_NAME', 'cdm_trade_db')
        self.user = user or os.environ.get('DB_USER', 'postgres')
        self.password = password or os.environ.get('DB_PASSWORD', 'postgres')
        
        self.conn_string = (
            f"host={self.host} "
            f"port={self.port} "
            f"dbname={self.database} "
            f"user={self.user} "
            f"password={self.password}"
        )
        
        self.pool = None
        self._initialized = True
    
    def initialize_pool(self, min_size: int = 5, max_size: int = 20) -> None:
        """Initialize the connection pool."""
        if self.pool is None:
            logger.info(f"Initializing database connection pool to {self.host}:{self.port}/{self.database}")
            self.pool = ConnectionPool(
                conninfo=self.conn_string,
                min_size=min_size,
                max_size=max_size,
                kwargs={"row_factory": dict_row}
            )
    
    def get_connection(self) -> psycopg.Connection:
        """Get a connection from the pool."""
        if self.pool is None:
            self.initialize_pool()
        return self.pool.getconn()
    
    def return_connection(self, conn: psycopg.Connection) -> None:
        """Return a connection to the pool."""
        if self.pool is not None:
            self.pool.putconn(conn)
    
    def close_pool(self) -> None:
        """Close the connection pool."""
        if self.pool is not None:
            logger.info("Closing database connection pool")
            self.pool.close()
            self.pool = None
    
    async def execute_script(self, script_path: str) -> None:
        """Execute a SQL script file."""
        try:
            with open(script_path, 'r') as f:
                sql = f.read()
            
            conn = self.get_connection()
            try:
                with conn.cursor() as cur:
                    cur.execute(sql)
                conn.commit()
                logger.info(f"Successfully executed SQL script: {script_path}")
            finally:
                self.return_connection(conn)
        except Exception as e:
            logger.error(f"Error executing SQL script {script_path}: {e}")
            raise

# Global database manager instance
db_manager = DatabaseManager() 