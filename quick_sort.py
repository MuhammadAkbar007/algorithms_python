# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 18:29:24 2022

@author: MuhammadAkbar
"""

from random import randrange

def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(randrange(len(arr)))
        print("pivot = ", pivot)
        kichik = [i for i in arr if i <= pivot]
        katta = [i for i in arr if i > pivot]
        print(f"{kichik} + [{pivot}] + {katta}")
        return qsort(kichik) + [pivot] + qsort(katta)

print(qsort([1, 5, 12, 0, -5, 66]))