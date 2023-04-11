"""
    Module printing summary of the contract
"""

from slither.printers.abstract_printer import AbstractPrinter

from slither.slithir.operations.condition import Condition


def calls_as_expressions(self) -> List["Expression"]:
        return self._expression_calls


def expressions(self) -> List["Expression"]:
        """
        list(Expression): List of the expressions
        """
        if self._expressions is None:
            expressionss = [n.expression for n in self.nodes]
            expressions = [e for e in expressionss if e]
            self._expressions = expressions
        return self._expressions

def return_values(self) -> List["SlithIRVariable"]:
        """
        list(Return Values): List of the return values
        """
        from slither.core.cfg.node import NodeType
        from slither.slithir.operations import Return
        from slither.slithir.variables import Constant

        if self._return_values is None:
            return_values = []
            returns = [n for n in self.nodes if n.type == NodeType.RETURN]
            [  # pylint: disable=expression-not-assigned
                return_values.extend(ir.values)
                for node in returns
                for ir in node.irs
                if isinstance(ir, Return)
            ]
            self._return_values = list({x for x in return_values if not isinstance(x, Constant)})
        return self._return_values
def _print_function(function: Function) -> str:
        txt = ""
        print("Hello")
        for node in function.nodes:
            if node.expression:
                txt += f"\t\tExpression: {node.expression}\n"
                txt += "\t\tIRs:\n"
                for ir in node.irs:
                    txt += f"\t\t\t{ir}\n"
                    if ir:
                        txt += "\t\tIRs:\n"
                        for ir in node.irs:
                            txt += f"\t\t\t{ir}\n"
            elif node.irs:
                txt += "\t\tIRs:\n"
                for ir in node.irs:
                    txt += f"\t\t\t{ir}\n"
        return txt


class PrinterSlithIR(AbstractPrinter):
    ARGUMENT = "slithir"
    HELP = "Print the slithIR representation of the functions"

    WIKI = "https://github.com/trailofbits/slither/wiki/Printer-documentation#slithir"

    def output(self, _filename):
        """
        _filename is not used
        Args:
            _filename(string)
        """

        txt = ""
        for compilation_unit in self.slither.compilation_units:
            for contract in compilation_unit.contracts:
                if contract.is_top_level:
                    continue
                txt += f"Contract {contract.name}\n"
                for function in contract.functions:
                    txt += f'\tFunction {function.canonical_name} {"" if function.is_shadowed else "(*)"}\n'
                    txt += _print_function(function)
                for modifier in contract.modifiers:
                    txt += f"\tModifier {modifier.canonical_name}\n"
                    txt += _print_function(modifier)
            if compilation_unit.functions_top_level:
                txt += "Top level functions\n"
            for function in compilation_unit.functions_top_level:
                txt += f"\tFunction {function.canonical_name}\n"
                txt += _print_function(function)
        self.info(txt)
        res = self.generate_output(txt)
        return res
