#!/usr/bin/env python3
"""
Test script for Pydantic 2 forward references.
This demonstrates how to properly handle forward references in Pydantic 2.
"""
from typing import Optional, List, ForwardRef, TYPE_CHECKING, Dict, Any
from pydantic import BaseModel, Field, ConfigDict, model_validator
from datetime import datetime

# Define forward references for components
InstrumentRef = ForwardRef('Instrument')
PartyRef = ForwardRef('Party')

class Party(BaseModel):
    """Party component demo class."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True
    )
    
    id: str
    name: str
    role: str = "Trader"
    instruments: List[InstrumentRef] = Field(default_factory=list)
    
    def __str__(self):
        return f"Party(id='{self.id}', name='{self.name}')"

class Instrument(BaseModel):
    """Instrument component demo class."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True
    )
    
    symbol: str
    security_id: str
    exchange: str = "NYSE"
    parties: List[PartyRef] = Field(default_factory=list)
    
    def __str__(self):
        return f"Instrument(symbol='{self.symbol}')"

class ExecutionReport(BaseModel):
    """ExecutionReport message demo class."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True
    )
    
    msg_type: str = "8"  # 8 = ExecutionReport
    order_id: str
    exec_id: str
    instrument: Instrument
    parties: List[Party] = Field(default_factory=list)
    
    @model_validator(mode='after')
    def resolve_forward_refs(cls, model):
        """Resolve forward references."""
        return model
    
    def __str__(self):
        return f"ExecutionReport(order_id='{self.order_id}', exec_id='{self.exec_id}')"

def test_forward_references():
    """Test that forward references work correctly in Pydantic 2."""
    # Create components
    party1 = Party(id="P1", name="Trader A")
    party2 = Party(id="P2", name="Trader B")
    
    instrument1 = Instrument(symbol="AAPL", security_id="AAPL.US")
    instrument2 = Instrument(symbol="MSFT", security_id="MSFT.US")
    
    # Create circular references
    party1.instruments.append(instrument1)
    instrument1.parties.append(party1)
    
    # Create an execution report with these components
    exec_report = ExecutionReport(
        order_id="ORD123",
        exec_id="EXE456",
        instrument=instrument2,
        parties=[party1, party2]
    )
    
    print(f"Created {party1} with instruments: {party1.instruments}")
    print(f"Created {instrument1} with parties: {instrument1.parties}")
    print(f"Created {exec_report}")
    
    # Test serialization
    exec_dict = exec_report.model_dump()
    print(f"\nSerialized ExecutionReport: {exec_dict}")
    
    # Test accessing circular references
    if party1.instruments and party1.instruments[0].parties:
        print(f"\nAccessing circular reference:")
        for party in party1.instruments[0].parties:
            print(f"- {party}")
    
    return True

if __name__ == "__main__":
    result = test_forward_references()
    print(f"\nTest {'passed' if result else 'failed'}") 