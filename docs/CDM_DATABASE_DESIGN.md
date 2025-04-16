# CDM Trade Repository Database Design

This document provides an overview of the database design and Data Access Object (DAO) layer implementation for storing Common Domain Model (CDM) trades, with a focus on Credit Default Swaps (CDS).

## Database Design Approach

The CDM model is a complex, deeply nested object model with many circular dependencies and references. When persisting these models to a relational database, we faced several key challenges:

1. **Complex Object Hierarchies**: CDM models have a deep and complex object hierarchy with nested objects that would be inefficient to represent directly in a relational model.

2. **Circular Dependencies**: Many CDM objects reference each other, creating circular dependencies that can be challenging to represent in relational databases.

3. **Flexible Structure**: The CDM structure allows for different ways to represent the same information, requiring a flexible database design.

4. **Performance Requirements**: The system needs to efficiently store and retrieve trade data for regulatory reporting and operational processes.

Our approach uses a database schema design that:

1. **Normalizes the Core Entities**: Parties, reference entities, obligations, and trades are stored in separate tables with proper relationships.

2. **Denormalizes Complex Attributes**: Some complex attributes are denormalized for performance and simplicity.

3. **Uses Junction Tables**: Many-to-many relationships (like credit events, obligations) are handled through junction tables.

4. **Implements a Layered DAO Approach**: The DAO layer handles the complexity of converting between object and relational models.

## Database Schema

The schema includes the following main components:

### Core Tables

- **cdm.party**: Stores information about counterparties and other entities.
- **cdm.legal_entity**: Extends party information with legal entity details.
- **cdm.reference_entity**: Stores information about reference entities for CDS trades.
- **cdm.reference_obligation**: Stores information about reference obligations for CDS trades.
- **cdm.trade**: The main trade table that stores common trade attributes.

### Credit Default Swap Specific Tables

- **cdm.credit_default_swap**: Stores CDS-specific information.
- **cdm.protection_terms**: Stores protection terms for CDS trades.
- **cdm.credit_event**: Stores credit events associated with protection terms.
- **cdm.obligation**: Stores obligation information for protection terms.
- **cdm.fee_leg**: Stores fee leg details for CDS trades.
- **cdm.settlement_terms**: Stores settlement terms information.

### Many-to-Many Relationship Tables

- **cdm.trade_party_role**: Links trades to parties with specific roles.
- **cdm.trade_identifier**: Stores identifiers for trades.
- **cdm.obligation_debt_type**: Links obligations to debt types.

### Specialized Tables for Complex Objects

- **cdm.failure_to_pay**: Stores detailed information about failure to pay credit events.
- **cdm.restructuring**: Stores detailed information about restructuring credit events.
- **cdm.cash_settlement_terms**: Stores cash settlement details.
- **cdm.physical_settlement_terms**: Stores physical settlement details.

## Table to CDM Model Mapping

### Party Tables

- **cdm.party** → `base.staticdata.party.party`
- **cdm.legal_entity** → `base.staticdata.party.legal_entity`

### Reference Information Tables

- **cdm.reference_entity** → `product.asset.reference_information.reference_entity`
- **cdm.reference_obligation** → `product.asset.reference_information.reference_obligation`

### Trade Tables

- **cdm.trade** → `event.common.trade`
- **cdm.trade_identifier** → `event.common.trade_identifier`
- **cdm.trade_party_role** → Links between `event.common.trade.party` and roles

### Credit Default Swap Tables

- **cdm.credit_default_swap** → `product.asset.credit_default_payout`
- **cdm.protection_terms** → `product.asset.protection_terms`
- **cdm.credit_event** → `observable.event.credit_events`
- **cdm.fee_leg** → `product.asset.credit_default_payout.fee_leg`
- **cdm.settlement_terms** → `product.common.settlement.settlement_terms`
- **cdm.cash_settlement_terms** → `product.common.settlement.cash_settlement_terms`
- **cdm.physical_settlement_terms** → `product.common.settlement.physical_settlement_terms`

## DAO Layer Implementation

The DAO (Data Access Object) layer provides an abstraction between the CDM object model and the relational database. It handles:

1. **Object-Relational Mapping**: Converts between CDM objects and database records.
2. **Transaction Management**: Ensures data consistency across related tables.
3. **Circular Dependency Resolution**: Breaks circular dependencies by implementing a specific save order.
4. **Flexible Path Handling**: Handles different object structures that can exist in CDM.

### Key DAO Classes

- **BaseDAO**: Provides common database operations for all DAOs.
- **PartyDAO**: Handles storing and retrieving party information.
- **TradeDAO**: Handles storing and retrieving trade information.
- **CreditDefaultSwapDAO**: Handles CDS-specific operations.

### DAO Implementation Approaches

The DAO layer implements several patterns to handle the CDM complexity:

1. **Hierarchical Save Pattern**: Saves objects in a hierarchical order, starting with the most basic entities.
2. **Flexible Path Extraction**: Extracts data from various possible paths in the object structure.
3. **Transactional Processing**: Ensures all related data is saved or rolled back together.
4. **Default Value Handling**: Provides sensible defaults for missing values.

## Performance Optimizations

Several optimizations have been implemented:

1. **Connection Pooling**: Uses connection pooling for efficient database access.
2. **Batch Operations**: Implements batch operations where possible.
3. **Indexes**: Adds appropriate indexes for common query patterns.
4. **Views**: Creates views for common query patterns to reduce joins.
5. **Denormalization**: Strategically denormalizes certain data for performance.

## Using the DAO Layer

To use the DAO layer:

```python
from src.dao.cdm.cds_dao import CreditDefaultSwapDAO

# Initialize the DAO
cds_dao = CreditDefaultSwapDAO()

# Save a CDM trade
trade_db_id = cds_dao.save(cdm_trade_object)

# Get trade details
trade_details = cds_dao.get_comprehensive_details(trade_db_id)

# Get all CDS trades
all_cds_trades = cds_dao.get_all_with_details()
```

## Coverage Analysis

The current implementation covers all essential CDS trade attributes. The coverage report generated by the `get_coverage_report()` method provides details on implemented fields and coverage percentage.

## Future Enhancements

Planned enhancements include:

1. **Schema Versioning**: Add support for schema versioning and migrations.
2. **Support for More Product Types**: Extend coverage to additional CDM product types.
3. **Performance Tuning**: Further optimize for high-volume trade processing.
4. **Caching Layer**: Add a caching layer for frequently accessed data.

## Conclusion

The implemented database design and DAO layer provide an efficient and flexible solution for storing CDM trade models in a relational database. The design balances normalization for data integrity with strategic denormalization for performance, while the DAO layer handles the complexity of mapping between the object and relational models. 