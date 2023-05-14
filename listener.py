from antlr4.error.Errors import InputMismatchException, NoViableAltException
from antlr4.error.ErrorListener import *


class SetErrorListener(ErrorListener):
    has_errors = False

    def __init__(self) -> None:
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, type_error):
        red_error = "\033[31;1mSyntax error\033[0m :"

        def replace_eof(replace_str: str):
            return replace_str.replace("<EOF>", "empty")

        msg = replace_eof(msg)
        self.has_errors = True
        print(f"{red_error} at line {line}, column {column}: {msg}")


