from pickle import TRUE


def say_hello(who):
    print(f'hello {who}')
    
def plus(a,b):
    re = a+b
    print(f'{a} + {b} = {re}')
    return (a, b, re)

def typetest(in_v, in_type):
    if type(in_v) == in_type:
        return True
    if in_type == str or in_type == list :
        print("I don't like this type")
    return False     
    
tu = plus(b = 5, a = 1)
print(tu)
b = typetest(tu, list)
print(f'type test : {b}')
b = typetest(tu, tuple)
print(f'type test : {b}')
    
workdays = {'mon', 'tue', 'wed', 'thu', 'fri'}
for d in workdays:
    print(d)
    if d == 'wed':
        break;