# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 13:38:43 2022

@author: MuhammadAkbar
"""

class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)
        return True
    
    def pop(self):
        if self.isEmpty(): return "Stack is empty !"
        else: return self.stack.pop()
        
    def peek(self):
        """Eng ustki elementni ko'rish"""
        if self.isEmpty(): return "Stack is empty !"
        else: return self.stack[-1]
        
stack = Stack()