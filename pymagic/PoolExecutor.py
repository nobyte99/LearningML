# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import random

def fib(n, test_arg):
    if n > 30:
        raise Exception('can not > 30, now %s' % n)
    if n <= 2:
        return 1
    return fib(n-1, test_arg) + fib(n-2, test_arg)

def use_map():
    nums = [random.randint(0, 33) for _ in range(0, 10)]
    with ProcessPoolExecutor() as executor:
        try:
            results = executor.map(fib, nums, nums)
            for num, result in zip(nums, results):
                print('fib(%s) result is %s.' % (num, result))
        except Exception as e:
            print(e)

def use_submit():
    nums = [random.randint(0, 33) for _ in range(0, 10)]
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(fib, n, n): n for n in nums}
        for f in as_completed(futures):
            try:
                print('fib(%s) result is %s.' % (futures[f], f.result()))
            except Exception as e:
                print(e)
                
if __name__ == '__main__':
    use_submit()