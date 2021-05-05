from models.cart import Cart
from models.CartItem import CartItem
from db.db import inventory

cart = Cart()

def fetch_cart_payload():
    cart_result = list(map(lambda x: x.json(), cart.items))
    if cart_result:
        return {'Items': cart_result}
    return "Cart is Empty"

def add_item(item_name):
    inv_items = [item for item in inventory if item.name == item_name]
    cart_items = [item for item in cart.items if item.name == item_name]
    if len(cart_items) < 1:
        cart.items.append(CartItem(item_name, inv_items[0].price, 1))
    else:
        cart_items[0].quantity += 1

def remove_item(item_name):
    cart_items = [item for item in cart.items if item.name == item_name][0]

    if cart_items.quantity > 1:
        cart_items.quantity -= 1
    else:
        index = cart.items.index(cart_items)
        del cart.items[index]

def get_total():
    total = 0
    for item in cart.items:
        inv_item = [i for i in inventory if i.name == item.name][0]
        total += (inv_item.price * item.quantity)
    return total

def breakdown():
    breakdown_list = []
    if cart.items:
        for item in cart.items:
            item1 = ({
                "name": item.name,
                "price": item.price
            })
            breakdown_list += item.quantity * [item1]
        return breakdown_list
    return "Empty"
















