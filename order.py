

class Order:

    def __init__(self, order_value: int):
        self._order_value = order_value

    def get_order_value(self):
        return self._order_value