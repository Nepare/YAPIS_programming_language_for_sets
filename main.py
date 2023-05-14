from antlr4 import *
from gen.ExprLexer import ExprLexer
from gen.ExprParser import ExprParser
from antlr4.CommonTokenStream import CommonTokenStream
from listener import SetErrorListener
from error_strategy import SetLangVisitor, SemanticError


def start_parse(input_string):
    input_stream = InputStream(input_string)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    parser.removeErrorListeners()
    syntax_error_listener = SetErrorListener()
    parser.addErrorListener(syntax_error_listener)

    tree = parser.program()
    if syntax_error_listener.has_errors:
        print("The program has syntax errors!")
        exit()
    else:
        print("The program has no syntax errors!")
        visitor = SetLangVisitor()
        visitor.visit(tree)


with open('example1_syntax_error.txt', 'r') as file:
    program_string = file.read()

start_parse(program_string)
