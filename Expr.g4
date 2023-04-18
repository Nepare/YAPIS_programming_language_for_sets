grammar Expr;

program: func* 'main' '{' (any_statement)* '}' EOF;

func: TYPE ID '(' (TYPE ID (',' TYPE ID)*)? ')'
'{' (any_statement)* '}';

assign_statement: TYPE ID (',' TYPE? ID)*;
statement: TYPE? ID (',' TYPE? ID)* '=' (expr (',' expr)*);

expr: (ID
| ('(' TYPE ')' ID)
| NUM
| set
| operation
| used_func
| INPUT);

operation: ((('(' TYPE ')')? ID)
| (('(' TYPE ')')? NUM)
| used_func)
(DEF_OP ((('(' TYPE ')')? ID)
| (('(' TYPE ')')? NUM)
| used_func))*;
used_func: ID '(' ID (',' ID)* ')';

set: '{' NUM (',' NUM)* '}';
any_statement:
  statement';'
| assign_statement';'
| if_statement
| show_statement';'
| return_statement';';

show_statement: 'print' '(' (ID | STR) ')';
if_statement: 'if' '(' if_condition ')'
'{' (any_statement)* '}'
('else' '{' (any_statement)* '}')?;
if_condition: (ID | NUM | used_func) EQ_OP (ID | NUM | used_func);
return_statement: 'return' ID;







AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;
EQ : '=' ;
COMMA : ',' ;
SEMI : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;

IF: 'if' ;
ELSE: 'else' ;
NLINE: '\n' ;
MAIN: 'main';
PRINT: 'print';
RETURN: 'return';
INPUT: 'input()';

TYPE: 'element' | 'set';
NUM: '0' | ( '-'? [1-9][0-9]* );
ID: [a-zA-Z][a-zA-Z_0-9]*;
DEF_OP: '+' | '-' | '*' | '/';
EQ_OP: '==';
WS : [ \n\t\r\f]+ -> skip ;
STR: '\'' [a-zA-Z ]* '\'' |
'"' [a-zA-Z ]* '"';