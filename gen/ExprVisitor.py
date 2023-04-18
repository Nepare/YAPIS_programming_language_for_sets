# Generated from D:/Projects/3course/yapis/programming_language\Expr.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#func.
    def visitFunc(self, ctx:ExprParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assign_statement.
    def visitAssign_statement(self, ctx:ExprParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#operation.
    def visitOperation(self, ctx:ExprParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#used_func.
    def visitUsed_func(self, ctx:ExprParser.Used_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#set.
    def visitSet(self, ctx:ExprParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#any_statement.
    def visitAny_statement(self, ctx:ExprParser.Any_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#show_statement.
    def visitShow_statement(self, ctx:ExprParser.Show_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if_statement.
    def visitIf_statement(self, ctx:ExprParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if_condition.
    def visitIf_condition(self, ctx:ExprParser.If_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#return_statement.
    def visitReturn_statement(self, ctx:ExprParser.Return_statementContext):
        return self.visitChildren(ctx)



del ExprParser