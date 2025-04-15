#!/usr/bin/env python3
"""Simple test for Pydantic 2 forward references."""
from typing import List, Optional, ForwardRef
from pydantic import BaseModel, Field, model_validator

# Define the forward reference
InstrumentRef = ForwardRef('Instrument')

class Party(BaseModel):
    """Party class with forward reference to Instrument."""
    id: str
    name: str
    instruments: List[InstrumentRef] = Field(default_factory=list)
    
    @model_validator(mode='after')
    def resolve_forward_refs(cls, model):
        """Resolve forward references."""
        return model

class Instrument(BaseModel):
    """Instrument class."""
    symbol: str
    security_id: str

def main():
    """Main test function."""
    # Create a party and instrument
    party = Party(id="P1", name="Trader")
    instrument = Instrument(symbol="AAPL", security_id="AAPL.US")
    
    # Add the instrument to the party
    party.instruments.append(instrument)
    
    print(f"Created party: {party.id}, {party.name}")
    print(f"Party has {len(party.instruments)} instruments")
    print(f"First instrument: {party.instruments[0].symbol}")
    print("Test successful!")
    
    return 0

if __name__ == "__main__":
    exit(main()) 