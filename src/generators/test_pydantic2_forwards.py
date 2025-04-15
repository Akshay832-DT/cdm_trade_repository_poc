#!/usr/bin/env python3
"""
Test script to validate forward reference handling in Pydantic 2.
This demonstrates how to properly handle forward references to avoid circular imports.
"""
from typing import Optional, List, Annotated
from pydantic import BaseModel, Field, ConfigDict

# Define the classes with forward references using string literals
class Component(BaseModel):
    """Test component with a circular reference."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True
    )
    
    name: str
    other: Optional['OtherComponent'] = None
    
    def __str__(self):
        return f"Component({self.name})"

class OtherComponent(BaseModel):
    """Test component that will be referenced by Component."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True
    )
    
    id: str
    components: List[Component] = Field(default_factory=list)
    
    def __str__(self):
        return f"OtherComponent({self.id})"

def test_forward_references():
    """Test that forward references work correctly."""
    # Create components
    comp1 = Component(name="Component 1")
    comp2 = Component(name="Component 2")
    other = OtherComponent(id="Other 1", components=[comp1])
    
    # Create circular reference
    comp2.other = other
    
    print(f"Created {comp1}")
    print(f"Created {comp2} with other={comp2.other}")
    print(f"Created {other} with components={other.components}")
    
    # Test serialization
    comp_dict = comp2.model_dump()
    print(f"\nSerialized Component 2: {comp_dict}")
    
    # Test that we can access the circular reference
    if comp2.other and comp2.other.components:
        print(f"\nAccessing circular reference:")
        for component in comp2.other.components:
            print(f"- {component}")
    
    return True

if __name__ == "__main__":
    result = test_forward_references()
    print(f"\nTest {'passed' if result else 'failed'}")
