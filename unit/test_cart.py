import unittest
from models.CartItem import CartItem
from services import CartService
from models.cart import Cart

class TestCart(unittest.TestCase):

    def setUp(self):
        CartService.cart = Cart()

    def test_view_cart(self):
        self.assertEqual("Cart is Empty", CartService.fetch_cart_payload())

    def test_when_item_added_can_see_item_in_cart(self):
        CartService.add_item("tshirt")
        expected = CartItem("tshirt", 7.25, 1)
        self.assertIn(expected, CartService.cart.items)

    def test_when_adding_a_different_item(self):
        CartService.add_item("tshirt")
        expected = CartItem("tshirt",7.25,1)
        self.assertIn(expected, CartService.cart.items)

    def test_adding_two_items_to_cart(self):
        CartService.add_item("tshirt")
        CartService.add_item("shorts")
        expected = CartItem("tshirt", 7.25, 1)
        expected2 = CartItem("shorts", 8.33, 1)
        self.assertIn(expected, CartService.cart.items)
        self.assertIn(expected2, CartService.cart.items)

    def test_adding_single_item_should_have_quantity_of_one(self):
        CartService.add_item("tshirt")
        actual = CartService.cart.items[0]
        self.assertEqual(1, actual.quantity)

    def test_incrementing_quantity_by_one(self):
        CartService.add_item("tshirt")
        CartService.add_item("tshirt")
        actual = CartService.cart.items[0]
        self.assertEqual(2, actual.quantity)

    def test_incrementing_quantity_by_two(self):
        CartService.add_item("tshirt")
        CartService.add_item("tshirt")
        self.assertEqual(1, len(CartService.cart.items))

    def test_remove_an_item(self):
        CartService.add_item("tshirt")
        CartService.remove_item("tshirt")
        self.assertNotIn('tshirt', CartService.cart.items)

    def test_get_total(self):
        CartService.add_item("tshirt")
        CartService.add_item("shorts")
        self.assertEqual(15.58, CartService.get_total())

    def test_get_total_breakdown(self):
        CartService.add_item("tshirt")
        CartService.add_item("shorts")
        CartService.add_item("shorts")
        expected = []
        for item in CartService.cart.items:
            new_item = ({"name": item.name,"price": item.price})
            expected += item.quantity * [new_item]
        self.assertEqual(expected, CartService.breakdown())


