from antlr4 import *
from gen.ExprVisitor import ExprVisitor
from gen.ExprParser import ExprParser


class SemanticError:
    def __init__(self, msg):
        self.msg = msg

    def print_msg(self):
        red_error = "\033[31;1mSemantic error\033[0m : "
        print(red_error + self.msg)


class SetLangVisitor(ExprVisitor):
    main_dict = {}
    hasSemanticErrors = False

    @staticmethod
    def get_path(ctx):
        path_to_ctx: list = [ctx]
        cur_ctx = ctx
        while type(cur_ctx) != ExprParser.ProgramContext:
            cur_ctx = cur_ctx.parentCtx
            path_to_ctx.append(cur_ctx)
        return path_to_ctx[1:]

    @staticmethod
    def check_if_var_is_in_namespace(path_of_var_used, path_of_var_declared):
        path_of_var_declared = path_of_var_declared[1:]
        print(path_of_var_used, path_of_var_declared)

        for i in range(len(path_of_var_declared)):
            if path_of_var_used[-(i+1)] != path_of_var_declared[-(i+1)]:
                return False
        return True

    def visitStatement(self, ctx:ExprParser.StatementContext):
        if ctx.TYPE() is None:
            if type(ctx.ID()) is list:
                for i in range(len(ctx.ID())):
                    if ctx.ID(i).getText() not in self.main_dict.keys():
                        SemanticError("Variable '" + ctx.ID(i).getText() + "' is not defined!").print_msg()
                        return None
            else:
                if ctx.ID().getText() not in self.main_dict.keys():
                    SemanticError("Variable '" + ctx.ID().getText() + "' is not defined!").print_msg()
                    return None
        else:
            local_type = ctx.TYPE().getText()
            if type(ctx.ID()) is list:
                for i in range(len(ctx.ID())):
                    cur_var_name = ctx.ID(i).getText()
                    cur_var_path = self.get_path(ctx.ID(i))
                    self.main_dict[cur_var_name] = {'type': local_type, 'path': cur_var_path[1:]}
            else:
                cur_var_name = ctx.ID().getText()
                cur_var_path = self.get_path(ctx.ID())
                self.main_dict[cur_var_name] = {'type': local_type, 'path': cur_var_path}

    def visitAssign_statement(self, ctx: ExprParser.Assign_statementContext):
        local_type = ctx.TYPE().getText()
        if type(ctx.ID()) is list:
            for i in range(len(ctx.ID())):
                cur_var_name = ctx.ID(i).getText()
                cur_var_path = self.get_path(ctx.ID(i))
                self.main_dict[cur_var_name] = {'type': local_type, 'path': cur_var_path}
        else:
            cur_var_name = ctx.ID().getText()
            cur_var_path = self.get_path(ctx.ID())
            self.main_dict[cur_var_name] = {'type': local_type, 'path': cur_var_path}

    def visitExpr(self, ctx: ExprParser.ExprContext):
        if ctx.ID():
            if ctx.ID().getText() not in self.main_dict.keys():
                SemanticError("Variable '" + ctx.ID().getText() + "' is not defined!").print_msg()
                return None

    def visitOperation(self, ctx:ExprParser.OperationContext):
        if ctx.ID(0):
            if ctx.ID(0).getText() not in self.main_dict.keys():
                SemanticError("Variable '" + ctx.ID(0).getText() + "' is not defined!").print_msg()
                return None
            return self.main_dict[ctx.ID(0).getText()]['path']

    def visitIf_condition(self, ctx:ExprParser.If_conditionContext):
        for i in range(1):
            if ctx.ID(i):
                if ctx.ID(0).getText() not in self.main_dict.keys():
                    SemanticError("Variable '" + ctx.ID(i).getText() + "' is not defined!").print_msg()
                    return None
                return self.main_dict[ctx.ID(i).getText()]['path']

    def visitShow_statement(self, ctx:ExprParser.Show_statementContext):
        if ctx.ID():
            if ctx.ID().getText() not in self.main_dict.keys():
                SemanticError("Variable '" + ctx.ID().getText() + "' is not defined!").print_msg()
                return None
            return self.main_dict[ctx.ID().getText()]['path']

    def visitUsed_func(self, ctx:ExprParser.Used_funcContext):
        print("hello")

    def visitReturn_statement(self, ctx:ExprParser.Return_statementContext):
        if ctx.ID():
            if ctx.ID().getText() not in self.main_dict.keys():
                SemanticError("Variable '" + ctx.ID().getText() + "' is not defined!").print_msg()
                return None
            return self.main_dict[ctx.ID().getText()]['path']

