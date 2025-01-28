from abc import ABC, abstractmethod
from discount_strategy import DiscountStrategy
from user_group import UserGroup


class Coupon(ABC):
    _COUPON_ID = 0

    def __init__(self, coupon_name: str, discount_strategy: DiscountStrategy, user_group: UserGroup):
        self.coupon_id = Coupon._COUPON_ID

        self.coupon_name = coupon_name
        self.discount_strategy = discount_strategy
        self.user_group = user_group

        Coupon._COUPON_ID += 1

    @abstractmethod
    def get_coupon_name(self):
        return self.coupon_name
    


class RideSharingCoupon(Coupon):

    def __init__(self, coupon_name, discount_strategy, user_group):
        super().__init__(coupon_name, discount_strategy, user_group)

