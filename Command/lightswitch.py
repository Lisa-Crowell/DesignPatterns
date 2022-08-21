#!/user/bin/env python
from abc import ABCMeta, abstractmethod
import time


class Light:
    def Switch_ON(self):
        print('The light is ON')

    def Switch_OFF(self):
        print('The light is OFF')


class ICommand(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        """A static interface method"""


class Switch_on_Command(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.Switch_ON()


class Switch_off_Command(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.Switch_OFF()


class Switch:
    def __init__(self):
        self._commands = {}
        self._history = []

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
            self._history.append({time.time(): command_name})
        else:
            print(f"Command [{command_name}] not recognised")


    @property
    def history(self):
        return self._history


if __name__ == '__main__':
    LIGHT = Light()

    SWITCH_ON = Switch_on_Command(LIGHT)
    SWITCH_OFF = Switch_off_Command(LIGHT)

    SWITCH = Switch()

    SWITCH.register('ON', SWITCH_ON)
    SWITCH.register('OFF', SWITCH_OFF)

    SWITCH.execute('ON')
    SWITCH.execute('OFF')
    SWITCH.execute('ON')
    SWITCH.execute('OFF')
    SWITCH.execute('ON')
    SWITCH.execute('OFF')
    SWITCH.execute('ON')
    SWITCH.execute('OFF')

    print(SWITCH.history)
