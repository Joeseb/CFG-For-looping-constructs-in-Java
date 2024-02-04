'''
A -> for
For ->(I;C;U)NS
N  ->New Line
S  ->Statements
C -> Condition
U->Updating Expression
I->initialize 

'''



import ply.lex as lex
import ply.yacc as yacc



def t_error(t):
    t.lexer.skip(1)

def p_for(p):
    '''assignment : for expr'''
    print("for accepted")

def p_expr(p):
    '''expr : openparantheses initialization semicolon condition semicolon updatingexpression closeparantheses next stm'''

def p_stm(p):
    '''stm : opencurlybraces statements semicolon closecurlybraces'''


def p_error(p):
    print("Syntax error !");

def forj(data):
    tokens = ['for','initialization','condition','statements','next','openparantheses','closeparantheses','opencurlybraces','closecurlybraces','semicolon','updatingexpression',]
    t_ignore = ' \t';
    t_next = ' \\n';
    t_for = r'for'
    t_openparantheses = r'\(';
    t_closeparantheses = r'\)';
    t_opencurlybraces = r'\{';
    t_closecurlybraces = r'\}';
    t_semicolon = r';';
    t_updatingexpression = r'updatingexpression';
    t_condition = r'condition'
    t_statements = r'statements'
    t_initialization = r'initialization'
    lex.lex();
    yacc.yacc();
    yacc.parse(data)







