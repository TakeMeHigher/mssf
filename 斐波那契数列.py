# -*- coding: utf-8 -*-
"""
Copyright (c) 2018,掌阅科技
All rights reserved.

摘    要: 斐波那契数列.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 16:49
"""
def fib(n):
    if n<=2 :
        return 1
    else:
        return fib(n-1)+fib(n-2)

a=0
b=1
while b < 1000:
    print(b)
    a, b = b, a+b



# 18、描述数组、链表、队列、堆栈的区别？
# 答：数组与链表是数据存储方式的概念，数组在连续的空间中存储数据，而链表
# 可以在非连续的空间中存储数据；
# 队列和堆栈是描述数据存取方式的概念，队列是先进先出，而堆栈是后进先出；
# 队列和堆栈可以用数组来实现，也可以用链表实现
