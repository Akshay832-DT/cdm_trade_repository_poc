#!/usr/bin/env python
"""
Initialize the CDM Trade Repository Database.

This script creates the database (if it doesn't exist)
and initializes the schema with tables, indexes, etc.
"""
import os
import sys
import logging
import asyncio
import argparse
import psycopg

from db_manager import db_manager

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def create_database():
    """Create the database if it doesn't exist."""
    # Save original database name
    original_db = db_manager.database
    
    # Connect to postgres database to create our database
    db_manager.database = 'postgres'
    
    # Update connection string
    db_manager.conn_string = (
        f"host={db_manager.host} "
        f"port={db_manager.port} "
        f"dbname={db_manager.database} "
        f"user={db_manager.user} "
        f"password={db_manager.password}"
    )
    
    # Close any existing pool
    if db_manager.pool is not None:
        db_manager.close_pool()
    
    # Initialize a new pool
    db_manager.initialize_pool(min_size=1, max_size=2)
    
    conn = db_manager.get_connection()
    conn.autocommit = True
    
    try:
        # Check if database exists
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (original_db,))
            exists = cur.fetchone()
            
            if not exists:
                logger.info(f"Creating database {original_db}")
                # Close any other connections to the database
                cur.execute(
                    "SELECT pg_terminate_backend(pg_stat_activity.pid) "
                    "FROM pg_stat_activity "
                    "WHERE pg_stat_activity.datname = %s "
                    "AND pid <> pg_backend_pid()", 
                    (original_db,)
                )
                # Create the database
                cur.execute(f"CREATE DATABASE {original_db}")
                logger.info(f"Database {original_db} created successfully")
            else:
                logger.info(f"Database {original_db} already exists")
    finally:
        # Return connection to pool
        db_manager.return_connection(conn)
        
        # Close the pool
        db_manager.close_pool()
    
    # Restore original database name
    db_manager.database = original_db
    
    # Update connection string
    db_manager.conn_string = (
        f"host={db_manager.host} "
        f"port={db_manager.port} "
        f"dbname={db_manager.database} "
        f"user={db_manager.user} "
        f"password={db_manager.password}"
    )

async def initialize_schema():
    """Initialize the database schema."""
    # Get the path to the schema.sql file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(current_dir, 'schema.sql')
    
    logger.info(f"Initializing schema from {schema_path}")
    
    # Execute the schema script
    await db_manager.execute_script(schema_path)
    
    logger.info("Schema initialized successfully")

async def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Initialize CDM Trade Repository Database')
    
    parser.add_argument('--host', default=os.environ.get('DB_HOST', 'localhost'),
                        help='Database host')
    parser.add_argument('--port', type=int, default=int(os.environ.get('DB_PORT', 5432)),
                        help='Database port')
    parser.add_argument('--database', default=os.environ.get('DB_NAME', 'cdm_trade_db'),
                        help='Database name')
    parser.add_argument('--user', default=os.environ.get('DB_USER', 'postgres'),
                        help='Database user')
    parser.add_argument('--password', default=os.environ.get('DB_PASSWORD', 'postgres'),
                        help='Database password')
    
    args = parser.parse_args()
    
    # Configure database manager
    db_manager.host = args.host
    db_manager.port = args.port
    db_manager.database = args.database
    db_manager.user = args.user
    db_manager.password = args.password
    
    # Update connection string
    db_manager.conn_string = (
        f"host={db_manager.host} "
        f"port={db_manager.port} "
        f"dbname={db_manager.database} "
        f"user={db_manager.user} "
        f"password={db_manager.password}"
    )
    
    try:
        # Create database
        await create_database()
        
        # Initialize pool for the target database
        db_manager.initialize_pool(min_size=1, max_size=5)
        
        # Initialize schema
        await initialize_schema()
        
        logger.info(f"Database {args.database} initialized successfully")
        
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        sys.exit(1)
    finally:
        # Close the pool
        db_manager.close_pool()

if __name__ == '__main__':
    asyncio.run(main()) 