-- CDM Trade Repository Database Schema
-- This schema defines the tables needed to store CDM Trade models
-- with a focus on handling complex relationships and circular dependencies.

-- Schema creation
CREATE SCHEMA IF NOT EXISTS cdm;

------------------------------------------
-- ENUMERATIONS 
------------------------------------------

-- Credit Event Enum: Maps to values in observable.event.credit_events
CREATE TYPE cdm.credit_event_enum AS ENUM (
    'Bankruptcy', 
    'FailureToPay', 
    'FailureToPayPrincipal',
    'FailureToPayInterest',
    'ObligationDefault',
    'ObligationAcceleration',
    'RepudiationMoratorium',
    'Restructuring',
    'GovernmentalIntervention',
    'DistressedRatingsDowngrade',
    'MaturityExtension',
    'Writedown',
    'ImpliedWritedown',
    'Other'
);

-- Debt Type/Obligation Category Enum: Maps to base.staticdata.asset.credit.obligation_category_enum
CREATE TYPE cdm.obligation_category_enum AS ENUM (
    'Bond', 
    'Loan', 
    'BondOrLoan',
    'SUBI',
    'Borrowed_Money',
    'Reference_Obligations_Only',
    'Other'
);

-- Day Count Fraction Enum
CREATE TYPE cdm.day_count_fraction_enum AS ENUM (
    'ACT/360', 
    'ACT/365', 
    '30/360', 
    'ACT/ACT.ISDA', 
    'ACT/ACT.ICMA', 
    '30E/360', 
    '30E/360.ISDA', 
    'Other'
);

-- Period Enum: Maps to payment frequencies
CREATE TYPE cdm.period_enum AS ENUM (
    '1D', '1W', '2W', '1M', '2M', '3M', '4M', '6M', '9M', '1Y', '2Y', '5Y', 'Other'
);

-- Settlement Type Enum: Maps to product.common.settlement.settlement_type_enum
CREATE TYPE cdm.settlement_type_enum AS ENUM (
    'Cash', 
    'Physical', 
    'Election', 
    'CashOrPhysical', 
    'CashWithoutDisruption', 
    'Other'
);

-- Business Day Convention Enum
CREATE TYPE cdm.business_day_convention_enum AS ENUM (
    'FOLLOWING',
    'MODFOLLOWING',
    'PRECEDING',
    'MODPRECEDING',
    'NONE'
);

-- Role Type Enum: Maps to party roles
CREATE TYPE cdm.role_type_enum AS ENUM (
    'BUYER',
    'SELLER',
    'PAYER',
    'RECEIVER',
    'PARTY',
    'COUNTERPARTY',
    'AGENT',
    'CLEARING_ORGANIZATION',
    'CUSTODIAN',
    'OTHER'
);

------------------------------------------
-- CORE ENTITY TABLES
------------------------------------------

-- Party table: Maps to base.staticdata.party.party
CREATE TABLE cdm.party (
    id SERIAL PRIMARY KEY,
    party_id VARCHAR(255) NOT NULL UNIQUE,  -- External identifier for the party
    name VARCHAR(255) NOT NULL,             -- Name of the party
    entity_type VARCHAR(50),                -- Type of entity (Corporation, Sovereign, etc.)
    lei VARCHAR(20),                        -- Legal Entity Identifier
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Legal Entity table: Maps to base.staticdata.party.legal_entity
-- This extends the Party table with additional fields specific to legal entities
CREATE TABLE cdm.legal_entity (
    id SERIAL PRIMARY KEY,
    party_id INTEGER NOT NULL REFERENCES cdm.party(id) ON DELETE CASCADE,
    entity_id VARCHAR(255),                 -- Entity identifier (e.g., RED code)
    entity_id_scheme VARCHAR(50),           -- Scheme for the entity identifier
    credit_rating_agency VARCHAR(50),       -- Agency providing the credit rating
    credit_rating VARCHAR(20),              -- Credit rating value
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Reference Entity table: Maps to reference_entity in ReferenceInformation
CREATE TABLE cdm.reference_entity (
    id SERIAL PRIMARY KEY,
    entity_id VARCHAR(255) NOT NULL UNIQUE, -- Deterministic ID derived from name
    name VARCHAR(255) NOT NULL,             -- Name of the reference entity
    entity_type VARCHAR(50),                -- Type of entity (e.g., Corporate, Sovereign)
    legal_entity_id INTEGER REFERENCES cdm.legal_entity(id), -- Link to legal entity if exists
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Reference Obligation table: Maps to reference_obligation in ReferenceInformation
CREATE TABLE cdm.reference_obligation (
    id SERIAL PRIMARY KEY,
    obligation_id VARCHAR(255) NOT NULL UNIQUE, -- Deterministic ID derived from description
    security_type VARCHAR(50) NOT NULL,         -- Type of security (Bond, Loan, etc.)
    description TEXT,                           -- Description of the obligation
    reference_entity_id INTEGER REFERENCES cdm.reference_entity(id), -- Reference entity issuing obligation
    isin VARCHAR(12),                           -- ISIN code if available
    cusip VARCHAR(9),                           -- CUSIP code if available
    issuer VARCHAR(255),                        -- Issuer of the obligation
    maturity_date DATE,                         -- Maturity date of the obligation
    coupon NUMERIC(10,6),                       -- Coupon rate
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Trade table - top level object: Maps to event.common.trade
CREATE TABLE cdm.trade (
    id SERIAL PRIMARY KEY,
    trade_id VARCHAR(255) NOT NULL UNIQUE,    -- External trade identifier
    trade_date DATE NOT NULL,                 -- Date the trade was executed
    effective_date DATE,                      -- Date the trade becomes effective
    termination_date DATE,                    -- Scheduled termination date
    product_type VARCHAR(50) NOT NULL,        -- Type of product (CREDIT_DEFAULT_SWAP, etc.)
    notional_amount NUMERIC(19, 2),           -- Notional amount of the trade
    notional_currency VARCHAR(3),             -- Currency of the notional
    cleared BOOLEAN DEFAULT FALSE,            -- Whether the trade is cleared
    clearing_organization VARCHAR(100),       -- Name of the clearing organization if cleared
    cleared_date DATE,                        -- Date the trade was cleared
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Trade identifiers: Maps to trade_identifier in event.common.trade
CREATE TABLE cdm.trade_identifier (
    id SERIAL PRIMARY KEY,
    trade_id INTEGER NOT NULL REFERENCES cdm.trade(id) ON DELETE CASCADE,
    issuer VARCHAR(255) NOT NULL,             -- Party that issued the identifier
    identifier VARCHAR(255) NOT NULL,         -- The actual identifier value
    identifier_type VARCHAR(50),              -- Type of identifier (USI, UTI, etc.)
    UNIQUE(trade_id, issuer, identifier)
);

-- Trade party roles: Maps to party_role in event.common.trade
CREATE TABLE cdm.trade_party_role (
    id SERIAL PRIMARY KEY,
    trade_id INTEGER NOT NULL REFERENCES cdm.trade(id) ON DELETE CASCADE,
    party_id INTEGER NOT NULL REFERENCES cdm.party(id),
    role cdm.role_type_enum NOT NULL,         -- Role the party plays in the trade
    UNIQUE(trade_id, party_id, role)
);

------------------------------------------
-- CREDIT DEFAULT SWAP SPECIFIC TABLES
------------------------------------------

-- Credit Default Swap table: Maps to product.asset.credit_default_payout
CREATE TABLE cdm.credit_default_swap (
    id SERIAL PRIMARY KEY,
    trade_id INTEGER NOT NULL UNIQUE REFERENCES cdm.trade(id) ON DELETE CASCADE,
    reference_entity_id INTEGER REFERENCES cdm.reference_entity(id),
    reference_obligation_id INTEGER REFERENCES cdm.reference_obligation(id),
    buy_sell VARCHAR(10) NOT NULL,           -- 'BUY' or 'SELL' from buyer/seller perspective
    fixed_rate NUMERIC(10, 6) NOT NULL,      -- Spread in percentage
    day_count_fraction cdm.day_count_fraction_enum NOT NULL,
    payment_frequency cdm.period_enum NOT NULL,
    first_payment_date DATE,                 -- First scheduled payment date
    last_payment_date DATE,                  -- Last scheduled payment date
    settlement_type cdm.settlement_type_enum, -- Type of settlement
    settlement_currency VARCHAR(3),          -- Settlement currency if cash settlement
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Protection Terms table: Maps to protection_terms in CreditDefaultPayout
CREATE TABLE cdm.protection_terms (
    id SERIAL PRIMARY KEY,
    cds_id INTEGER NOT NULL REFERENCES cdm.credit_default_swap(id) ON DELETE CASCADE,
    all_guarantees BOOLEAN,                  -- Whether all guarantees are covered
    protection_start_date DATE,              -- Start date of protection
    protection_end_date DATE,                -- End date of protection
    default_requirement_amount NUMERIC(19, 2), -- Default requirement amount
    default_requirement_currency VARCHAR(3),  -- Currency for default requirement
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Credit Events for a CDS: Maps to credit_events in protection_terms
CREATE TABLE cdm.credit_event (
    id SERIAL PRIMARY KEY,
    protection_terms_id INTEGER NOT NULL REFERENCES cdm.protection_terms(id) ON DELETE CASCADE,
    event_type cdm.credit_event_enum NOT NULL,
    applicable BOOLEAN DEFAULT TRUE,         -- Whether the event type is applicable
    UNIQUE(protection_terms_id, event_type)
);

-- Failure to Pay details: Maps to failure_to_pay in credit_events
CREATE TABLE cdm.failure_to_pay (
    id SERIAL PRIMARY KEY,
    credit_event_id INTEGER NOT NULL REFERENCES cdm.credit_event(id) ON DELETE CASCADE,
    payment_requirement_amount NUMERIC(19, 2), -- Minimum amount that triggers failure to pay
    payment_requirement_currency VARCHAR(3),   -- Currency for payment requirement
    grace_period_extension BOOLEAN,            -- Whether grace period extension applies
    grace_period_days INTEGER,                 -- Number of days in grace period
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Restructuring details: Maps to restructuring in credit_events
CREATE TABLE cdm.restructuring (
    id SERIAL PRIMARY KEY,
    credit_event_id INTEGER NOT NULL REFERENCES cdm.credit_event(id) ON DELETE CASCADE,
    restructuring_type VARCHAR(50),          -- Type of restructuring (Mod, ModMod, ModModR)
    multiple_holder_obligation BOOLEAN,      -- Whether multiple holder obligation applies
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Obligations table: Maps to obligations in protection_terms
CREATE TABLE cdm.obligation (
    id SERIAL PRIMARY KEY,
    protection_terms_id INTEGER NOT NULL REFERENCES cdm.protection_terms(id) ON DELETE CASCADE,
    category cdm.obligation_category_enum NOT NULL,
    not_subordinated BOOLEAN,                -- Whether obligation must not be subordinated
    specified_currency VARCHAR(3),           -- Specified currency for obligation
    not_sovereign_lender BOOLEAN,            -- Whether not sovereign lender applies
    not_domestic_currency BOOLEAN,           -- Whether not domestic currency applies
    not_domestic_law BOOLEAN,                -- Whether not domestic law applies
    listed BOOLEAN,                          -- Whether obligation must be listed
    not_domestic_issuance BOOLEAN,           -- Whether not domestic issuance applies
    not_contingent BOOLEAN,                  -- Whether not contingent applies
    excluded_obligations TEXT,               -- Description of excluded obligations
    designated_priority VARCHAR(50),         -- Priority of the obligation (senior, etc.)
    cash_settlement_only BOOLEAN,            -- Whether cash settlement only applies
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Debt Types for Obligations: Maps to debt_type in obligations
CREATE TABLE cdm.obligation_debt_type (
    id SERIAL PRIMARY KEY,
    obligation_id INTEGER NOT NULL REFERENCES cdm.obligation(id) ON DELETE CASCADE,
    debt_type cdm.obligation_category_enum NOT NULL,
    UNIQUE(obligation_id, debt_type)
);

-- Fee Leg table: Maps to fee_leg in CreditDefaultPayout
CREATE TABLE cdm.fee_leg (
    id SERIAL PRIMARY KEY,
    cds_id INTEGER NOT NULL UNIQUE REFERENCES cdm.credit_default_swap(id) ON DELETE CASCADE,
    initial_payment_amount NUMERIC(19, 2),    -- Initial payment amount if any
    initial_payment_currency VARCHAR(3),      -- Currency for initial payment
    initial_payment_payer_id INTEGER REFERENCES cdm.party(id), -- Party making initial payment
    initial_payment_receiver_id INTEGER REFERENCES cdm.party(id), -- Party receiving initial payment
    initial_payment_date DATE,                -- Date of initial payment
    fee_rate NUMERIC(10, 6),                  -- Fee rate if different from fixed rate
    fee_day_count_fraction cdm.day_count_fraction_enum, -- Day count for fees
    fee_payment_frequency cdm.period_enum,    -- Payment frequency for fees
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Settlement Terms table: Maps to settlement_terms in CreditDefaultPayout
CREATE TABLE cdm.settlement_terms (
    id SERIAL PRIMARY KEY,
    cds_id INTEGER NOT NULL UNIQUE REFERENCES cdm.credit_default_swap(id) ON DELETE CASCADE,
    settlement_type cdm.settlement_type_enum NOT NULL,
    settlement_currency VARCHAR(3),            -- Currency for settlement
    settlement_date DATE,                     -- Date of settlement
    business_day_convention cdm.business_day_convention_enum, -- Business day convention
    business_centers VARCHAR(255),            -- Business centers for date adjustments
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Cash Settlement Terms: Maps to cash_settlement_terms in settlement_terms
CREATE TABLE cdm.cash_settlement_terms (
    id SERIAL PRIMARY KEY,
    settlement_terms_id INTEGER NOT NULL REFERENCES cdm.settlement_terms(id) ON DELETE CASCADE,
    cash_settlement_method VARCHAR(50),       -- Method of cash settlement
    cash_settlement_amount NUMERIC(19, 2),    -- Fixed cash settlement amount if known
    valuation_method VARCHAR(50),             -- Method for valuation
    valuation_date DATE,                      -- Date of valuation
    valuation_time TIME,                      -- Time of valuation
    quotation_rate_type VARCHAR(50),          -- Type of quotation rate
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Physical Settlement Terms: Maps to physical_settlement_terms in settlement_terms
CREATE TABLE cdm.physical_settlement_terms (
    id SERIAL PRIMARY KEY,
    settlement_terms_id INTEGER NOT NULL REFERENCES cdm.settlement_terms(id) ON DELETE CASCADE,
    delivery_date DATE,                       -- Date for delivery
    deliverable_obligation_type VARCHAR(50),  -- Type of deliverable obligation
    deliverable_obligation_currency VARCHAR(3), -- Currency of deliverable obligation
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

------------------------------------------
-- INDICES FOR PERFORMANCE
------------------------------------------

-- Trade indices
CREATE INDEX idx_trade_trade_date ON cdm.trade(trade_date);
CREATE INDEX idx_trade_product_type ON cdm.trade(product_type);
CREATE INDEX idx_trade_effective_date ON cdm.trade(effective_date);
CREATE INDEX idx_trade_termination_date ON cdm.trade(termination_date);

-- Trade identifier indices
CREATE INDEX idx_trade_identifier_identifier ON cdm.trade_identifier(identifier);
CREATE INDEX idx_trade_identifier_issuer ON cdm.trade_identifier(issuer);

-- Party indices
CREATE INDEX idx_party_name ON cdm.party(name);
CREATE INDEX idx_party_lei ON cdm.party(lei);

-- CDS indices
CREATE INDEX idx_cds_reference_entity ON cdm.credit_default_swap(reference_entity_id);
CREATE INDEX idx_cds_fixed_rate ON cdm.credit_default_swap(fixed_rate);
CREATE INDEX idx_cds_buy_sell ON cdm.credit_default_swap(buy_sell);

-- Reference entity and obligation
CREATE INDEX idx_reference_entity_name ON cdm.reference_entity(name);
CREATE INDEX idx_reference_obligation_isin ON cdm.reference_obligation(isin);
CREATE INDEX idx_reference_obligation_cusip ON cdm.reference_obligation(cusip);

------------------------------------------
-- VIEWS FOR EASIER QUERYING
------------------------------------------

-- CDS trade view for easier querying
CREATE OR REPLACE VIEW cdm.v_credit_default_swap AS
SELECT 
    t.id AS trade_id,
    t.trade_id AS trade_external_id,
    t.trade_date,
    t.effective_date,
    t.termination_date,
    t.notional_amount,
    t.notional_currency,
    cds.fixed_rate,
    cds.day_count_fraction,
    cds.payment_frequency,
    cds.buy_sell,
    b.party_id AS buyer_id,
    b.name AS buyer_name,
    s.party_id AS seller_id,
    s.name AS seller_name,
    re.name AS reference_entity_name,
    ro.description AS reference_obligation_desc,
    ro.isin AS reference_obligation_isin,
    st.settlement_type
FROM 
    cdm.trade t
JOIN 
    cdm.credit_default_swap cds ON t.id = cds.trade_id
LEFT JOIN 
    cdm.settlement_terms st ON cds.id = st.cds_id
LEFT JOIN 
    cdm.trade_party_role tpr_buyer ON t.id = tpr_buyer.trade_id AND tpr_buyer.role = 'BUYER'
LEFT JOIN 
    cdm.party b ON tpr_buyer.party_id = b.id
LEFT JOIN 
    cdm.trade_party_role tpr_seller ON t.id = tpr_seller.trade_id AND tpr_seller.role = 'SELLER'
LEFT JOIN 
    cdm.party s ON tpr_seller.party_id = s.id
LEFT JOIN 
    cdm.reference_entity re ON cds.reference_entity_id = re.id
LEFT JOIN 
    cdm.reference_obligation ro ON cds.reference_obligation_id = ro.id;

-- Comprehensive CDS details view
CREATE OR REPLACE VIEW cdm.v_cds_details AS
SELECT
    t.id AS trade_id,
    t.trade_id AS trade_external_id,
    t.trade_date,
    t.effective_date,
    t.termination_date,
    t.notional_amount,
    t.notional_currency,
    cds.fixed_rate,
    cds.day_count_fraction,
    cds.payment_frequency,
    cds.buy_sell,
    re.name AS reference_entity_name,
    ro.description AS reference_obligation_desc,
    pt.id AS protection_terms_id,
    st.settlement_type,
    json_agg(DISTINCT ce.event_type) AS credit_events,
    json_agg(DISTINCT odt.debt_type) AS obligation_debt_types
FROM 
    cdm.trade t
JOIN 
    cdm.credit_default_swap cds ON t.id = cds.trade_id
LEFT JOIN 
    cdm.reference_entity re ON cds.reference_entity_id = re.id
LEFT JOIN 
    cdm.reference_obligation ro ON cds.reference_obligation_id = ro.id
LEFT JOIN 
    cdm.protection_terms pt ON cds.id = pt.cds_id
LEFT JOIN 
    cdm.credit_event ce ON pt.id = ce.protection_terms_id
LEFT JOIN 
    cdm.settlement_terms st ON cds.id = st.cds_id
LEFT JOIN 
    cdm.obligation o ON pt.id = o.protection_terms_id
LEFT JOIN 
    cdm.obligation_debt_type odt ON o.id = odt.obligation_id
GROUP BY
    t.id, t.trade_id, t.trade_date, t.effective_date, t.termination_date,
    t.notional_amount, t.notional_currency, cds.fixed_rate, cds.day_count_fraction,
    cds.payment_frequency, cds.buy_sell, re.name, ro.description, pt.id, st.settlement_type; 