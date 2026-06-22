# test_dappblock.py
"""
Tests for DappBlock module.
"""

import unittest
from dappblock import DappBlock

class TestDappBlock(unittest.TestCase):
    """Test cases for DappBlock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DappBlock()
        self.assertIsInstance(instance, DappBlock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DappBlock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
