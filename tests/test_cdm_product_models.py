"""
Test for CDM product models.
"""
import unittest
import json
import pytest
from datetime import date

from src.models.cdm.generated.product.template import Product, TransferableProduct, TradableProduct

class TestCdmProductModels(unittest.TestCase):
    """Test cases for core CDM product models."""
    
    def test_product_model(self):
        """Test Product model."""
        # Create a Product with a TransferableProduct
        data = {
            "transferable_product": {
                "economic_terms": {
                    "payout": []
                }
            }
        }
        
        product = Product(**data)
        self.assertIsNotNone(product)
        self.assertIsNotNone(product.transferable_product)
        self.assertIsNone(product.non_transferable_product)
    
    def test_transferable_product(self):
        """Test TransferableProduct model."""
        # Create a TransferableProduct
        data = {
            "economic_terms": {
                "payout": []
            }
        }
        
        transferable = TransferableProduct(**data)
        self.assertIsNotNone(transferable)
        self.assertIsNotNone(transferable.economic_terms)
        
    def test_model_serialization(self):
        """Test that models can be serialized to dict and JSON."""
        # Create a Product
        data = {
            "transferable_product": {
                "economic_terms": {
                    "payout": []
                }
            }
        }
        
        product = Product(**data)
        
        # Convert to dict
        product_dict = product.model_dump()
        self.assertIsInstance(product_dict, dict)
        self.assertIn("transferable_product", product_dict)
        
        # Convert to JSON
        product_json = product.model_dump_json()
        self.assertIsInstance(product_json, str)
        
        # Parse JSON back
        parsed = json.loads(product_json)
        self.assertIsInstance(parsed, dict)
        self.assertIn("transferable_product", parsed)

if __name__ == "__main__":
    unittest.main() 