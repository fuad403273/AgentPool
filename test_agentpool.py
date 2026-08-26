# test_agentpool.py
"""
Tests for AgentPool module.
"""

import unittest
from agentpool import AgentPool

class TestAgentPool(unittest.TestCase):
    """Test cases for AgentPool class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgentPool()
        self.assertIsInstance(instance, AgentPool)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgentPool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
