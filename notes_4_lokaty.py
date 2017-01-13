import time


def trigger(f):
    def g(self, *args, **kwargs):
        while self.do_trigger:
            time.sleep(0.1)
            f(self, *args, **kwargs)
    return g


class DepositAccount:
    def __init__(self, name, investment):
        self.name = name
        self.amount_of_money = 1000
        self.investment_strategy = investment

    def charge_interest(self):
        interest = self.investment_strategy.calculate_interest(self.amount_of_money)
        self.amount_of_money += interest


class InterestCalculator:
    def __init__(self, DepositAccount):
        self.do_trigger = True
        self.day_counter = 0
        self.deposit_account = DepositAccount

    @trigger
    def charge_interest(self):

        self.day_counter += 1
        if self.day_counter >= 100:
            self.do_trigger = False

        self.deposit_account.charge_interest()


class Investment:

    def calculate_interest(self, amount_of_money):
        if 0 < amount_of_money <= 1200:
            algorithm = algorithm_1
        elif 1200 < amount_of_money <= 1600:
            algorithm = algorithm_2
        else:
            algorithm = algorithm_3

        interest = algorithm(amount_of_money)

        return interest


def algorithm_1(amount_of_money):
    percentage = 0.005
    print("For amount: {} and percentage: {} the interest is: {}".format(
        amount_of_money, percentage, percentage * amount_of_money
    ))
    return percentage * amount_of_money


def algorithm_2(amount_of_money):
    percentage = 0.007
    print("For amount: {} and percentage: {} the interest is: {}".format(
        amount_of_money, percentage, percentage * amount_of_money
    ))
    return percentage * amount_of_money


def algorithm_3(amount_of_money):
    percentage = 0.01
    print("For amount: {} and percentage: {} the interest is: {}".format(
        amount_of_money, percentage, percentage * amount_of_money
    ))
    return percentage * amount_of_money



if __name__ == '__main__':
    inv = Investment()
    d = DepositAccount("Andrzej", inv)
    a = InterestCalculator(d)
    a.charge_interest()