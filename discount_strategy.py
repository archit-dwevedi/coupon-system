from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    
    def __init__(self, discount_value, upper_limit=None):
        self.discount_value = discount_value

        self.upper_limit = upper_limit

    @abstractmethod
    def get_discount(self, order_value):
        pass


class PercentageDiscount(DiscountStrategy):
    
    def get_discount(self, order_value):

        if self.upper_limit:
            discount = min(order_value * self.discount_value / 100, self.upper_limit)
            return order_value - discount
            
        return order_value * self.discount_value / 100
    

    
class FixedDiscount(DiscountStrategy):

    def get_discount(self, order_value):
        return order_value - self.discount_value
    