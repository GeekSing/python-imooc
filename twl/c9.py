import time

def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(func_name):
    print('This is a function named' + func_name)

@decorator
def f2(func_name1,func_name2):
    print('This is a function named' + func_name1)
    print('This is a function named' + func_name2)

@decorator
def f3(func_name1,func_name2,**kw):
    print('This is a function named' + func_name1)
    print('This is a function named' + func_name2)
    print(kw)



f3('test fun1','test fun2',a=1,b=2,c='2')

f1('test fun')
f2('test fun1','test fun2')
