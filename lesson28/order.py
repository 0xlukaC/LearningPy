class Order:
    def __init__(self, order_id, items, total):
        self.order_id = order_id
        self.items = items
        self.total = total

    def add_item(self, item, price):
        self.items.append(item)
        self.total += price

    def get_summary(self):
        return f"Order {self.order_id}: {len(self.items)} items, total ${self.total}"
