#!/user/bin/env python
from abc import ABCMeta, abstractmethod


# the Command interface, that all commands will implement.
class ICommand(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        "the required execute method that all Command objects use."


class Invoker:
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")


class Receiver:
    @staticmethod
    def run_command_1():
        "A set of instructions to run"
        print('Executing Command 1')

    @staticmethod
    def run_command_2():
        "A set of instructions to run"
        print('Executing Command 2')


class Command1(ICommand): # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and runs the Command on the designated receiver."""

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_1()


class Command2(ICommand): # pylint: diable=too-few-public-methods
    """A Command object, that implements the ICommand interface and runs the Command on the designated receiver."""

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_2()


#The Client
#Create a receiver
RECEIVER = Receiver()

#create commands
COMMAND1 = Command1(RECEIVER)
COMMAND2 = Command2(RECEIVER)

#register the commands with the invoker
INVOKER = Invoker()
INVOKER.register('1', COMMAND1)
INVOKER.register('2', COMMAND2)

#execute the commands that are registered on the Invoker
INVOKER.execute('1')
INVOKER.execute('2')
INVOKER.execute('1')
INVOKER.execute('2')


