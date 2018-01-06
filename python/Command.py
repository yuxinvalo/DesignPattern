import abc

class HouseworkRecevier(object):
    def start(self):
        print("Start to clean the floor")

    def stop(self):
        print("Stop to clean the flood")

class Command(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass

class StartHouseWorkCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver
    def execute(self):
        self.receiver.start()

class StopHouseWorkCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.stop()

class CommandInvoker(object):
    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()

receiver = HouseworkRecevier()
start_cmd = StartHouseWorkCommand(receiver)
client = CommandInvoker(start_cmd)
client.do()
stop_cmd = StopHouseWorkCommand(receiver)
client.command = stop_cmd
client.do()
