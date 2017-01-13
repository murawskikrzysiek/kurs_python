#!/usr/bin/env python
import abc

class AccountManager(object):
    def __init__(self, name):
        self.name = name
        self.service = None

    def make_payment(self, **details):
        assert self.service is not None, "Need to chose a service first"
        self.service.transfer(**details)

    def connect(self, service):
        assert service in available_services.values(), "Unknown service"
        self.service = service()


class Connection(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def transfer(self, **details):
        pass


class ExternalTransferService(Connection):
    def __init__(self):
        self.name = "ExternalTransferService"

    def transfer(self, **details):
        print(">>> {} making a transfer with details {}".format(self.name, details))


class ExternalTransferService2(Connection):
    def __init__(self):
        self.name = "ExternalTransferService2"

    def transfer(self, **details):
        print(">>> {} making a transfer with details {}".format(self.name, details))

if __name__ == '__main__':

    available_services = {"ExternalTransferService": ExternalTransferService,
                          "ExternalTransferService2": ExternalTransferService2}

    manager1 = AccountManager('Bob')
    manager1.connect(ExternalTransferService)
    manager1.make_payment(amount=100, recipient=3949494)

    manager2 = AccountManager('Alice')
    manager2.connect(ExternalTransferService2)
    manager2.make_payment(amount=250, recipient=3934)