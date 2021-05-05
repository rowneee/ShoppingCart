import unittest
from resources.inventory import Inventory


class TestInventory(unittest.TestCase):
    def test_get_all_items(self):
        inventory = Inventory()
        self.assertEqual(inventory.items, inventory)

