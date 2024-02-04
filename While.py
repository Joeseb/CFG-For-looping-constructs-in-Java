'''while(condition)
{Statement 1;Statement 2;
.
.
.
Updating expression;}'''

'''
A -> WHILE
WHILE -> CNSU|CU 
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

def p_while(p):
    '''assignment : while expr'''
    print("while accepted")

def p_expr(p):
    '''expr : openparantheses condition closeparantheses next stm'''

def p_stm(p):
    '''stm : opencurlybraces statements semicolon next updatingexpression semicolon closecurlybraces
           | opencurlybraces updatingexpression semicolon closecurlybraces'''

def p_error(p):
    print("Syntax error .");

def whilej(data):
    tokens = ['while','condition','statements','next','openparantheses','closeparantheses','opencurlybraces','closecurlybraces','semicolon','updatingexpression',]
    t_ignore = ' \t';
    t_next = ' \\n';
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









