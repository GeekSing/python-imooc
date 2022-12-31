# -*- coding: utf-8 -*-
#装饰器

import time

def f1():
    print('This is a function')


#对修改是封闭，对扩展是开放的

def f2():
    print('This is a function')

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)