# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 12:19:47 2022

@author: MuhammadAkbar
"""

class Node:
    """ Tugun = Node obyekti """
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    """ Linked List obyekti """
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def push(self, new_data):
        """List boshiga tugun qo'shish"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def insertAfter(self, prev_node, new_data):
        """Biror tugundan so'ng tugun qo'shish"""
        if prev_node is None:
            print("Tugun mavjud emas !")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def append(self, new_data):
        """Linked List ohiriga obyekt qo'shish"""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def deleteNode(self, key):
        """Obyekt o'chirish"""
        temp = self.head
        if (temp and temp.data == key):
            self.head  = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None