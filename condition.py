from slither.slithir.operations.operation import Operation
#from /Users/akansha/Downloads/slither-master/slither/slithir/operations import Operation
from slither.slithir.utils.utils import is_valid_rvalue


class Condition(Operation):
    """
    Condition
    Only present as last operation in conditional node
    """

    def __init__(self, value):
        assert is_valid_rvalue(value)
        super().__init__()
        self._value = value

    @property
    def read(self):
        return [self.value]

    @property
    def value(self):
        return self._value

    def __str__(self):
        print("Hello")
        return f"CONDITION {self.value}"
