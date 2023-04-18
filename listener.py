from antlr4.error.Errors import InputMismatchException, NoViableAltException
from antlr4.error.ErrorListener import *


class SetErrorListener(ErrorListener):
    def __init__(self) -> None:
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, type_error):
        red_error = "\033[1;31;20mSyntax error\033[0m :"

        def replace_eof(replace_str: str):
            return replace_str.replace("<EOF>", "empty")

        msg = replace_eof(msg)
        if isinstance(type_error, InputMismatchException):
            expected_tokens = type_error.getExpectedTokens().toString(recognizer.literalNames, recognizer.symbolicNames)
            expected_tokens = replace_eof(expected_tokens)
            ofend_symbol = replace_eof(offendingSymbol.text)
            print(f"{red_error} mismatched input '{ofend_symbol}' at line {line}, column {column}. "
                  f"Expected one of the following tokens: {expected_tokens}")
        elif isinstance(type_error, NoViableAltException):
            print(f"{red_error} {msg} at line: {line}, column {column}")
        else:
            print(f"{red_error} at line {line}, column {column}: {msg}")
