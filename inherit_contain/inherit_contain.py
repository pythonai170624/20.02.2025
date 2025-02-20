from abc import ABC, abstractmethod
from typing import override

class IPayment(ABC):
    @abstractmethod
    def pay(self):
        pass

class Bit(IPayment):
    @override
    def pay(self):
        print('oper-C')

class Credit(IPayment):
    @override
    def pay(self):
        print('oper-D')

# inheritance
# class MobilePhone(IPayment):
#     def __init__(self, number, model)
#         self ...
#     @override
#     def pay(self):
#         print('oper-D')

# strategy - contain
# class MobilePhone():
#     def __init__(self, pay_impl):
#         self.pay_impl = pay_impl
#     def change_payment(self, pay_impl):
#         self.pay_impl = pay_impl