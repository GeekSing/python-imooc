# -*- coding: utf-8 -*-
#װ����

import time

def f1():
    print('This is a function')


#���޸��Ƿ�գ�����չ�ǿ��ŵ�

def f2():
    print('This is a function')

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)