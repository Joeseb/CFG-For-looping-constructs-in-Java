'''
A -> do
do -> NSW 
W -> whileC
U -> updating expression
N  ->New Line
S  ->Statements
C -> Condition
'''
import ply.lex as lex
import ply.yacc as yacc



def t_error(t):
    #print("Illegal character ")
    t.lexer.skip(1)

def p_do(p):
    '''assignment : do next stm'''
    print("do while accepted")

# def p_expr(p):
#     '''expr : opencurlybraces next statements closecurlybraces '''

def p_stm(p):
    '''stm : opencurlybraces next statements semicolon next updatingexpression semicolon next closecurlybraces while expr'''

def p_expr(p):
    '''expr : openparantheses condition closeparantheses semicolon'''

def p_error(p):
    print("Syntax error .");

def doWhilej(data):
    tokens = ['do','while','condition','statements','next','openparantheses','closeparantheses','opencurlybraces','closecurlybraces','semicolon','updatingexpression',]

    t_ignore = ' \t';
    t_next = ' \\n';
    t_do = r'do'
    t_while = r'while'
    t_openparantheses = r'\(';
    t_closeparantheses = r'\)';
    t_opencurlybraces = r'\{';
    t_closecurlybraces = r'\}';
    t_semicolon = r';';
    t_updatingexpression = r'updatingexpression';
    t_condition = r'condition'
    t_statements = r'statements'

    lex.lex();
    yacc.yacc();
    yacc.parse(data)