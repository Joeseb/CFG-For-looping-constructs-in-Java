from pydoc import doc
import While
import DoWhile
import For

# data=1
# ;

# data1='''while(condition)
# {updatingexpression;}''';

# data2='''for(initialization;condition;updatingexpression)
# {statements;}''';

# data3 = '''do
# {
#     statements;
#     updatingexpression;
# } while(condition);'''

data = open("input.txt","r").read()


print()
t = input('\n1.while \n2.for \n3.do while \n\nEnter your choice: ')
if(t=='1'):
    While.whilej(data)
    # While.whilej(data1)
elif(t=='2'):
    For.forj(data)
elif(t=='3'):
    DoWhile.doWhilej(data)
else:
    print('Invalid input')

