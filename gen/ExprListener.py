# Generated from D:/Projects/3course/yapis/programming_language\Expr.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#func.
    def enterFunc(self, ctx:ExprParser.FuncContext):
        pass

    # Exit a parse tree produced by ExprParser#func.
    def exitFunc(self, ctx:ExprParser.FuncContext):
        pass


    # Enter a parse tree produced by ExprParser#assign_statement.
    def enterAssign_statement(self, ctx:ExprParser.Assign_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#assign_statement.
    def exitAssign_statement(self, ctx:ExprParser.Assign_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#operation.
    def enterOperation(self, ctx:ExprParser.OperationContext):
        pass

    # Exit a parse tree produced by ExprParser#operation.
    def exitOperation(self, ctx:ExprParser.OperationContext):
        pass


    # Enter a parse tree produced by ExprParser#used_func.
    def enterUsed_func(self, ctx:ExprParser.Used_funcContext):
        pass

    # Exit a parse tree produced by ExprParser#used_func.
    def exitUsed_func(self, ctx:ExprParser.Used_funcContext):
        pass


    # Enter a parse tree produced by ExprParser#set.
    def enterSet(self, ctx:ExprParser.SetContext):
        pass

    # Exit a parse tree produced by ExprParser#set.
    def exitSet(self, ctx:ExprParser.SetContext):
        pass


    # Enter a parse tree produced by ExprParser#any_statement.
    def enterAny_statement(self, ctx:ExprParser.Any_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#any_statement.
    def exitAny_statement(self, ctx:ExprParser.Any_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#show_statement.
    def enterShow_statement(self, ctx:ExprParser.Show_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#show_statement.
    def exitShow_statement(self, ctx:ExprParser.Show_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#if_statement.
    def enterIf_statement(self, ctx:ExprParser.If_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#if_statement.
    def exitIf_statement(self, ctx:ExprParser.If_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#if_condition.
    def enterIf_condition(self, ctx:ExprParser.If_conditionContext):
        pass

    # Exit a parse tree produced by ExprParser#if_condition.
    def exitIf_condition(self, ctx:ExprParser.If_conditionContext):
        pass


    # Enter a parse tree produced by ExprParser#return_statement.
    def enterReturn_statement(self, ctx:ExprParser.Return_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#return_statement.
    def exitReturn_statement(self, ctx:ExprParser.Return_statementContext):
        pass



del ExprParser