# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 12:23:37 2022

@author: MuhammadAkbar
"""

from linkedlistfuncs import Node, LinkedList

llist = LinkedList()
llist.head = Node('Dushanba')
tuesday = Node('Seshanba')
wednesday = Node('Chorshanba')
llist.head.next = tuesday
tuesday.next = wednesday

llist.push('Yakshanba')
# llist.printList()

llist.insertAfter(llist.head.next, 'Dushanba kechasi')
# llist.printList()

llist.append('Payshanba')
# llist.printList()

llist.deleteNode('Yakshanba')
llist.deleteNode('Dushanba kechasi')
llist.deleteNode('Payshanba')
llist.deleteNode('Monday')
llist.printList()