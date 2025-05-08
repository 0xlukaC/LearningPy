from order import Order


class Delivery:
    def __init__(self, delivery_id, order, address):
        self.delivery_id = delivery_id
        self.order = order  # Order object
        self.address = address
        self.status = "Preparing"

    def update_status(self, new_status):
        self.status = new_status

    def delivery_summary(self):
        return f"Delivery {self.delivery_id} to {self.address} — {self.status}"
