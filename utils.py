# cart details for price and quantity
class Cart:
    def __init__(self):
        self.items = {}
        self.total = 0

    def add_item(self, item, price, qty=1):
        self.items[item] = self.items.get(item, 0) + qty
        self.total += price * qty

    def remove_item(self, item, price, qty=1):
        if item in self.items:
            remove_qty = min(qty, self.items[item])
            self.items[item] -= remove_qty
            self.total -= price * remove_qty
            if self.items[item] == 0:
                del self.items[item]

    def show_cart(self):
        return self.items, self.total
