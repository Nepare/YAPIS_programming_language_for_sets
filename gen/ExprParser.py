# Generated from D:/Projects/3course/yapis/programming_language\Expr.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,232,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,0,5,0,36,8,0,10,0,12,0,39,9,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,12,1,
        55,9,1,3,1,57,8,1,1,1,1,1,1,1,5,1,62,8,1,10,1,12,1,65,9,1,1,1,1,
        1,1,2,1,2,1,2,1,2,3,2,73,8,2,1,2,5,2,76,8,2,10,2,12,2,79,9,2,1,3,
        3,3,82,8,3,1,3,1,3,1,3,3,3,87,8,3,1,3,5,3,90,8,3,10,3,12,3,93,9,
        3,1,3,1,3,1,3,1,3,5,3,99,8,3,10,3,12,3,102,9,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,114,8,4,1,5,1,5,1,5,3,5,119,8,5,1,5,1,
        5,1,5,1,5,3,5,125,8,5,1,5,1,5,3,5,129,8,5,1,5,1,5,1,5,1,5,3,5,135,
        8,5,1,5,1,5,1,5,1,5,3,5,141,8,5,1,5,1,5,3,5,145,8,5,5,5,147,8,5,
        10,5,12,5,150,9,5,1,6,1,6,1,6,1,6,1,6,5,6,157,8,6,10,6,12,6,160,
        9,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,168,8,7,10,7,12,7,171,9,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,188,8,
        8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,201,8,10,
        10,10,12,10,204,9,10,1,10,1,10,1,10,1,10,5,10,210,8,10,10,10,12,
        10,213,9,10,1,10,3,10,216,8,10,1,11,1,11,1,11,3,11,221,8,11,1,11,
        1,11,1,11,1,11,3,11,227,8,11,1,12,1,12,1,12,1,12,0,0,13,0,2,4,6,
        8,10,12,14,16,18,20,22,24,0,1,2,0,20,20,24,24,257,0,29,1,0,0,0,2,
        43,1,0,0,0,4,68,1,0,0,0,6,81,1,0,0,0,8,113,1,0,0,0,10,128,1,0,0,
        0,12,151,1,0,0,0,14,163,1,0,0,0,16,187,1,0,0,0,18,189,1,0,0,0,20,
        194,1,0,0,0,22,220,1,0,0,0,24,228,1,0,0,0,26,28,3,2,1,0,27,26,1,
        0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,
        29,1,0,0,0,32,33,5,14,0,0,33,37,5,9,0,0,34,36,3,16,8,0,35,34,1,0,
        0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,
        1,0,0,0,40,41,5,10,0,0,41,42,5,0,0,1,42,1,1,0,0,0,43,44,5,18,0,0,
        44,45,5,20,0,0,45,56,5,7,0,0,46,47,5,18,0,0,47,53,5,20,0,0,48,49,
        5,5,0,0,49,50,5,18,0,0,50,52,5,20,0,0,51,48,1,0,0,0,52,55,1,0,0,
        0,53,51,1,0,0,0,53,54,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,56,46,
        1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,5,8,0,0,59,63,5,9,0,0,
        60,62,3,16,8,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,
        0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,10,0,0,67,3,1,0,0,0,68,
        69,5,18,0,0,69,77,5,20,0,0,70,72,5,5,0,0,71,73,5,18,0,0,72,71,1,
        0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,76,5,20,0,0,75,70,1,0,0,0,76,
        79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,5,1,0,0,0,79,77,1,0,0,
        0,80,82,5,18,0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,91,
        5,20,0,0,84,86,5,5,0,0,85,87,5,18,0,0,86,85,1,0,0,0,86,87,1,0,0,
        0,87,88,1,0,0,0,88,90,5,20,0,0,89,84,1,0,0,0,90,93,1,0,0,0,91,89,
        1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,1,0,0,0,94,95,5,4,0,0,
        95,100,3,8,4,0,96,97,5,5,0,0,97,99,3,8,4,0,98,96,1,0,0,0,99,102,
        1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,7,1,0,0,0,102,100,1,0,
        0,0,103,114,5,20,0,0,104,105,5,7,0,0,105,106,5,18,0,0,106,107,5,
        8,0,0,107,114,5,20,0,0,108,114,5,19,0,0,109,114,3,14,7,0,110,114,
        3,10,5,0,111,114,3,12,6,0,112,114,5,17,0,0,113,103,1,0,0,0,113,104,
        1,0,0,0,113,108,1,0,0,0,113,109,1,0,0,0,113,110,1,0,0,0,113,111,
        1,0,0,0,113,112,1,0,0,0,114,9,1,0,0,0,115,116,5,7,0,0,116,117,5,
        18,0,0,117,119,5,8,0,0,118,115,1,0,0,0,118,119,1,0,0,0,119,120,1,
        0,0,0,120,129,5,20,0,0,121,122,5,7,0,0,122,123,5,18,0,0,123,125,
        5,8,0,0,124,121,1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,129,
        5,19,0,0,127,129,3,12,6,0,128,118,1,0,0,0,128,124,1,0,0,0,128,127,
        1,0,0,0,129,148,1,0,0,0,130,144,5,21,0,0,131,132,5,7,0,0,132,133,
        5,18,0,0,133,135,5,8,0,0,134,131,1,0,0,0,134,135,1,0,0,0,135,136,
        1,0,0,0,136,145,5,20,0,0,137,138,5,7,0,0,138,139,5,18,0,0,139,141,
        5,8,0,0,140,137,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,145,
        5,19,0,0,143,145,3,12,6,0,144,134,1,0,0,0,144,140,1,0,0,0,144,143,
        1,0,0,0,145,147,1,0,0,0,146,130,1,0,0,0,147,150,1,0,0,0,148,146,
        1,0,0,0,148,149,1,0,0,0,149,11,1,0,0,0,150,148,1,0,0,0,151,152,5,
        20,0,0,152,153,5,7,0,0,153,158,5,20,0,0,154,155,5,5,0,0,155,157,
        5,20,0,0,156,154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,
        1,0,0,0,159,161,1,0,0,0,160,158,1,0,0,0,161,162,5,8,0,0,162,13,1,
        0,0,0,163,164,5,9,0,0,164,169,5,19,0,0,165,166,5,5,0,0,166,168,5,
        19,0,0,167,165,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,
        0,0,0,170,172,1,0,0,0,171,169,1,0,0,0,172,173,5,10,0,0,173,15,1,
        0,0,0,174,175,3,6,3,0,175,176,5,6,0,0,176,188,1,0,0,0,177,178,3,
        4,2,0,178,179,5,6,0,0,179,188,1,0,0,0,180,188,3,20,10,0,181,182,
        3,18,9,0,182,183,5,6,0,0,183,188,1,0,0,0,184,185,3,24,12,0,185,186,
        5,6,0,0,186,188,1,0,0,0,187,174,1,0,0,0,187,177,1,0,0,0,187,180,
        1,0,0,0,187,181,1,0,0,0,187,184,1,0,0,0,188,17,1,0,0,0,189,190,5,
        15,0,0,190,191,5,7,0,0,191,192,7,0,0,0,192,193,5,8,0,0,193,19,1,
        0,0,0,194,195,5,11,0,0,195,196,5,7,0,0,196,197,3,22,11,0,197,198,
        5,8,0,0,198,202,5,9,0,0,199,201,3,16,8,0,200,199,1,0,0,0,201,204,
        1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,205,1,0,0,0,204,202,
        1,0,0,0,205,215,5,10,0,0,206,207,5,12,0,0,207,211,5,9,0,0,208,210,
        3,16,8,0,209,208,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,
        1,0,0,0,212,214,1,0,0,0,213,211,1,0,0,0,214,216,5,10,0,0,215,206,
        1,0,0,0,215,216,1,0,0,0,216,21,1,0,0,0,217,221,5,20,0,0,218,221,
        5,19,0,0,219,221,3,12,6,0,220,217,1,0,0,0,220,218,1,0,0,0,220,219,
        1,0,0,0,221,222,1,0,0,0,222,226,5,22,0,0,223,227,5,20,0,0,224,227,
        5,19,0,0,225,227,3,12,6,0,226,223,1,0,0,0,226,224,1,0,0,0,226,225,
        1,0,0,0,227,23,1,0,0,0,228,229,5,16,0,0,229,230,5,20,0,0,230,25,
        1,0,0,0,27,29,37,53,56,63,72,77,81,86,91,100,113,118,124,128,134,
        140,144,148,158,169,187,202,211,215,220,226
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'='", "','", 
                     "';'", "'('", "')'", "'{'", "'}'", "'if'", "'else'", 
                     "'\\n'", "'main'", "'print'", "'return'", "'input()'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'=='" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "EQ", "COMMA", "SEMI", 
                      "LPAREN", "RPAREN", "LCURLY", "RCURLY", "IF", "ELSE", 
                      "NLINE", "MAIN", "PRINT", "RETURN", "INPUT", "TYPE", 
                      "NUM", "ID", "DEF_OP", "EQ_OP", "WS", "STR" ]

    RULE_program = 0
    RULE_func = 1
    RULE_assign_statement = 2
    RULE_statement = 3
    RULE_expr = 4
    RULE_operation = 5
    RULE_used_func = 6
    RULE_set = 7
    RULE_any_statement = 8
    RULE_show_statement = 9
    RULE_if_statement = 10
    RULE_if_condition = 11
    RULE_return_statement = 12

    ruleNames =  [ "program", "func", "assign_statement", "statement", "expr", 
                   "operation", "used_func", "set", "any_statement", "show_statement", 
                   "if_statement", "if_condition", "return_statement" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    EQ=4
    COMMA=5
    SEMI=6
    LPAREN=7
    RPAREN=8
    LCURLY=9
    RCURLY=10
    IF=11
    ELSE=12
    NLINE=13
    MAIN=14
    PRINT=15
    RETURN=16
    INPUT=17
    TYPE=18
    NUM=19
    ID=20
    DEF_OP=21
    EQ_OP=22
    WS=23
    STR=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(ExprParser.MAIN, 0)

        def LCURLY(self):
            return self.getToken(ExprParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(ExprParser.RCURLY, 0)

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.FuncContext)
            else:
                return self.getTypedRuleContext(ExprParser.FuncContext,i)


        def any_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Any_statementContext)
            else:
                return self.getTypedRuleContext(ExprParser.Any_statementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 26
                self.func()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(ExprParser.MAIN)
            self.state = 33
            self.match(ExprParser.LCURLY)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1411072) != 0):
                self.state = 34
                self.any_statement()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(ExprParser.RCURLY)
            self.state = 41
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.TYPE)
            else:
                return self.getToken(ExprParser.TYPE, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURLY(self):
            return self.getToken(ExprParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(ExprParser.RCURLY, 0)

        def any_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Any_statementContext)
            else:
                return self.getTypedRuleContext(ExprParser.Any_statementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ExprParser.TYPE)
            self.state = 44
            self.match(ExprParser.ID)
            self.state = 45
            self.match(ExprParser.LPAREN)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 46
                self.match(ExprParser.TYPE)
                self.state = 47
                self.match(ExprParser.ID)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 48
                    self.match(ExprParser.COMMA)
                    self.state = 49
                    self.match(ExprParser.TYPE)
                    self.state = 50
                    self.match(ExprParser.ID)
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 58
            self.match(ExprParser.RPAREN)
            self.state = 59
            self.match(ExprParser.LCURLY)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1411072) != 0):
                self.state = 60
                self.any_statement()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(ExprParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.TYPE)
            else:
                return self.getToken(ExprParser.TYPE, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_assign_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_statement" ):
                listener.enterAssign_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_statement" ):
                listener.exitAssign_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = ExprParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ExprParser.TYPE)
            self.state = 69
            self.match(ExprParser.ID)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 70
                self.match(ExprParser.COMMA)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 71
                    self.match(ExprParser.TYPE)


                self.state = 74
                self.match(ExprParser.ID)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.TYPE)
            else:
                return self.getToken(ExprParser.TYPE, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 80
                self.match(ExprParser.TYPE)


            self.state = 83
            self.match(ExprParser.ID)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 84
                self.match(ExprParser.COMMA)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 85
                    self.match(ExprParser.TYPE)


                self.state = 88
                self.match(ExprParser.ID)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(ExprParser.EQ)

            self.state = 95
            self.expr()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 96
                self.match(ExprParser.COMMA)
                self.state = 97
                self.expr()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def set_(self):
            return self.getTypedRuleContext(ExprParser.SetContext,0)


        def operation(self):
            return self.getTypedRuleContext(ExprParser.OperationContext,0)


        def used_func(self):
            return self.getTypedRuleContext(ExprParser.Used_funcContext,0)


        def INPUT(self):
            return self.getToken(ExprParser.INPUT, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def TYPE(self):
            return self.getToken(ExprParser.TYPE, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 103
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.state = 104
                self.match(ExprParser.LPAREN)
                self.state = 105
                self.match(ExprParser.TYPE)
                self.state = 106
                self.match(ExprParser.RPAREN)
                self.state = 107
                self.match(ExprParser.ID)
                pass

            elif la_ == 3:
                self.state = 108
                self.match(ExprParser.NUM)
                pass

            elif la_ == 4:
                self.state = 109
                self.set_()
                pass

            elif la_ == 5:
                self.state = 110
                self.operation()
                pass

            elif la_ == 6:
                self.state = 111
                self.used_func()
                pass

            elif la_ == 7:
                self.state = 112
                self.match(ExprParser.INPUT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def used_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Used_funcContext)
            else:
                return self.getTypedRuleContext(ExprParser.Used_funcContext,i)


        def DEF_OP(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.DEF_OP)
            else:
                return self.getToken(ExprParser.DEF_OP, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NUM)
            else:
                return self.getToken(ExprParser.NUM, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LPAREN)
            else:
                return self.getToken(ExprParser.LPAREN, i)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.TYPE)
            else:
                return self.getToken(ExprParser.TYPE, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RPAREN)
            else:
                return self.getToken(ExprParser.RPAREN, i)

        def getRuleIndex(self):
            return ExprParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = ExprParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 115
                    self.match(ExprParser.LPAREN)
                    self.state = 116
                    self.match(ExprParser.TYPE)
                    self.state = 117
                    self.match(ExprParser.RPAREN)


                self.state = 120
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 121
                    self.match(ExprParser.LPAREN)
                    self.state = 122
                    self.match(ExprParser.TYPE)
                    self.state = 123
                    self.match(ExprParser.RPAREN)


                self.state = 126
                self.match(ExprParser.NUM)
                pass

            elif la_ == 3:
                self.state = 127
                self.used_func()
                pass


            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 130
                self.match(ExprParser.DEF_OP)
                self.state = 144
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 134
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==7:
                        self.state = 131
                        self.match(ExprParser.LPAREN)
                        self.state = 132
                        self.match(ExprParser.TYPE)
                        self.state = 133
                        self.match(ExprParser.RPAREN)


                    self.state = 136
                    self.match(ExprParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 140
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==7:
                        self.state = 137
                        self.match(ExprParser.LPAREN)
                        self.state = 138
                        self.match(ExprParser.TYPE)
                        self.state = 139
                        self.match(ExprParser.RPAREN)


                    self.state = 142
                    self.match(ExprParser.NUM)
                    pass

                elif la_ == 3:
                    self.state = 143
                    self.used_func()
                    pass


                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Used_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_used_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsed_func" ):
                listener.enterUsed_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsed_func" ):
                listener.exitUsed_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsed_func" ):
                return visitor.visitUsed_func(self)
            else:
                return visitor.visitChildren(self)




    def used_func(self):

        localctx = ExprParser.Used_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_used_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ExprParser.ID)
            self.state = 152
            self.match(ExprParser.LPAREN)
            self.state = 153
            self.match(ExprParser.ID)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 154
                self.match(ExprParser.COMMA)
                self.state = 155
                self.match(ExprParser.ID)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURLY(self):
            return self.getToken(ExprParser.LCURLY, 0)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NUM)
            else:
                return self.getToken(ExprParser.NUM, i)

        def RCURLY(self):
            return self.getToken(ExprParser.RCURLY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_set

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet" ):
                listener.enterSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet" ):
                listener.exitSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet" ):
                return visitor.visitSet(self)
            else:
                return visitor.visitChildren(self)




    def set_(self):

        localctx = ExprParser.SetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_set)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(ExprParser.LCURLY)
            self.state = 164
            self.match(ExprParser.NUM)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 165
                self.match(ExprParser.COMMA)
                self.state = 166
                self.match(ExprParser.NUM)
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self.match(ExprParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)

        def assign_statement(self):
            return self.getTypedRuleContext(ExprParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ExprParser.If_statementContext,0)


        def show_statement(self):
            return self.getTypedRuleContext(ExprParser.Show_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ExprParser.Return_statementContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_any_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_statement" ):
                listener.enterAny_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_statement" ):
                listener.exitAny_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAny_statement" ):
                return visitor.visitAny_statement(self)
            else:
                return visitor.visitChildren(self)




    def any_statement(self):

        localctx = ExprParser.Any_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_any_statement)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.statement()
                self.state = 175
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.assign_statement()
                self.state = 178
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.show_statement()
                self.state = 182
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.return_statement()
                self.state = 185
                self.match(ExprParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Show_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def STR(self):
            return self.getToken(ExprParser.STR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_show_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShow_statement" ):
                listener.enterShow_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShow_statement" ):
                listener.exitShow_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShow_statement" ):
                return visitor.visitShow_statement(self)
            else:
                return visitor.visitChildren(self)




    def show_statement(self):

        localctx = ExprParser.Show_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_show_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(ExprParser.PRINT)
            self.state = 190
            self.match(ExprParser.LPAREN)
            self.state = 191
            _la = self._input.LA(1)
            if not(_la==20 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 192
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def if_condition(self):
            return self.getTypedRuleContext(ExprParser.If_conditionContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LCURLY)
            else:
                return self.getToken(ExprParser.LCURLY, i)

        def RCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RCURLY)
            else:
                return self.getToken(ExprParser.RCURLY, i)

        def any_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Any_statementContext)
            else:
                return self.getTypedRuleContext(ExprParser.Any_statementContext,i)


        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ExprParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ExprParser.IF)
            self.state = 195
            self.match(ExprParser.LPAREN)
            self.state = 196
            self.if_condition()
            self.state = 197
            self.match(ExprParser.RPAREN)
            self.state = 198
            self.match(ExprParser.LCURLY)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1411072) != 0):
                self.state = 199
                self.any_statement()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self.match(ExprParser.RCURLY)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 206
                self.match(ExprParser.ELSE)
                self.state = 207
                self.match(ExprParser.LCURLY)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1411072) != 0):
                    self.state = 208
                    self.any_statement()
                    self.state = 213
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 214
                self.match(ExprParser.RCURLY)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ_OP(self):
            return self.getToken(ExprParser.EQ_OP, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NUM)
            else:
                return self.getToken(ExprParser.NUM, i)

        def used_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Used_funcContext)
            else:
                return self.getTypedRuleContext(ExprParser.Used_funcContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_if_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_condition" ):
                listener.enterIf_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_condition" ):
                listener.exitIf_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_condition" ):
                return visitor.visitIf_condition(self)
            else:
                return visitor.visitChildren(self)




    def if_condition(self):

        localctx = ExprParser.If_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 217
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.state = 218
                self.match(ExprParser.NUM)
                pass

            elif la_ == 3:
                self.state = 219
                self.used_func()
                pass


            self.state = 222
            self.match(ExprParser.EQ_OP)
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 223
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.state = 224
                self.match(ExprParser.NUM)
                pass

            elif la_ == 3:
                self.state = 225
                self.used_func()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ExprParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(ExprParser.RETURN)
            self.state = 229
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





