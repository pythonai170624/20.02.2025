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

# inheritance (implement)
# class MobilePhone(IPayment):
#     def __init__(self, number, model)

#     @override
#     def pay(self):
#         print('oper-D')

# strategy - contain
# class MobilePhone():
#     def __init__(self, payer: IPayment):
#         self.payer = payer
#     def change_payment(self, payer: IPayment):
#         self.payer = payer


class IFly:
    @abstractmethod
    def fly(self):
        pass

class Superman(IFly):
    @override
    def fly(self):
        print('fly')

# class Bycycle(IFly):
#     @override
#     def fly(self):
#         raise NotImplemented

class Bycycle(IFly):
    def __init__(self, flyer: IFly):
        self.flyer = flyer

    @override
    def fly(self):
        self.flyer.fly()

class CannotFly(IFly):
    @override
    def fly(self):
        raise NotImplementedError

class NewFlyingBycler(IFly):
    @override
    def fly(self):
        print('flying bycycle....')

b = Bycycle(CannotFly())
b.fly()  # Error
b.flyer = NewFlyingBycler()
b.fly()
b.flyer = CannotFly()
b.fly()  # Error


class IGo_0_100_3_seconds:
    @abstractmethod
    def go_fast(self):
        pass










