from user import User
from order import Order

class CouponService:
    _INSTANCE = None

    def __init__(self):
        if CouponService._INSTANCE is not None:
            raise Exception("This class is a singleton!")

    @staticmethod
    def get_instance(self):
        if CouponService._INSTANCE is None:
            CouponService._INSTANCE = CouponService()
            return CouponService._INSTANCE
        return CouponService._INSTANCE
    
    def get_valid_coupon(self, user: User, order: Order) -> int:
        pass

    def create_coupon(self):
        pass





        