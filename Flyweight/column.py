"""A column that is used in a row"""

from flyweight_factory import FlyweightFactory


class Column:
    """The columns are the contexts. They will share the flyweights via the FlyweightFactory. 'Data',
    'width', and 'justify' are extrinsic values. They are outside of the flyweights."""

    def __init__(self, data="", width=11, justify=0) -> None:
        self.data = data
        self.width = width
        self.justify = justify  # 0:center, 1:left, 2:right

    def get_data(self):
        """Get the flyweight value from the factory, and apply the extrinsic values"""
        ret = ""
        for data in self.data:
            ret = f"{ret.center(self.width)}" if self.justify == 0 else ret
            ret = f"{ret.ljust(self.width)}" if self.justify == 1 else ret
            ret = f"{ret.rjust(self.width)}" if self.justify == 2 else ret
            return ret
