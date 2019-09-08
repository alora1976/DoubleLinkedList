# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:42:28 2019

@author: Lori
"""

class Node:#create Node class
    def __init__(self, val):#constructor contains 3 information peices to keep track of info
        self.val = val# keeps track of info inside Node
        self.next = None#keeps track of pointer to next node
        self.previous = None#keeps track of pointer to previous node


class DoubleLinkedList:#creates class for the actual Double Linekd List
    def __init__(self):#constructor 
        self.head = None#self.head is = to None if list is empty.

    def append(self, val):#function of DLL takes data creates node and adds to END of list
        if self.head is None:#checks to see if there are elements in the DLL
            new_node = Node(val)#if it is empty create node
            new_node.previous = None# since it is the first element in the list previous pointer should point to null
            self.head = new_node#since it is the first element in the list makes it the head.
        else:
            new_node = Node(val)
            current = self.head
            while current.next:#traverses list until it finds null
                current = current.next
            current.next = new_node#at end of list creates new node
            new_node.previous = current#previous node linked to new node created
            new_node.next = None#next pointer of new node points to null

    def prepend(self, val):#function of DLL creates Node and adds to FRONT of DLL
        if self.head is None:# checks to see if list is empty
            new_node = Node(val)#creates new node 
            new_node.previous = None #since it is the first element in the list previous pointer should point to null
            self.head = new_node#establishes it as the head node
        else:
            new_node = Node(val)
            self.head.previous = new_node#links 
            new_node.next = self.head#
            self.head = new_node#establishes new node as head
            new_node.previous = None#points new head to null

    def print_list(self):#function of DLL that will output info of DLL
        current = self.head
        while current:#prints value of each node until reaches null at end
            print(current.val)
            current = current.next

  

    def delete(self, key):#function takes two aparameters self since its a memeber of the DLL class and data element of node needing to be deleted.
        current = self.head#sets pointer = to head of list
        while current:#while current is not null keep moving through list
            if current.val  == key and current == self.head:#if current is head of list and = to key needing to be deleted
                #situation 1
                if not current.next:#checks if pointer is pointing to another node
                    current = None #sets current to none
                    self.head = None#sets head to none because you delted the only node in teh list and now have an empty list
                    return#done with checking situation

                #situation 2
                else:#if current.next IS pointing to another node
                    nxt = current.next#stores new node info
                    current.next = None #removes next pointer from node being deleted
                    nxt.previous = None#removes previous pointer of node being delted
                    current = None#points remaining node to null since it is the only element in the list
                    self.head = nxt#sets remaining node as head
                    return #done with checking situation

            elif current.val  == key:#checks if data elements = key needing to be deleted
                #situation 3
                if current.next:#if node has a node after it
                    nxt = current.next #stores info for new next pointer
                    previous = current.previous#stores info for new previous pointer
                    previous.next = nxt#points next pointer to next node
                    nxt.previous = previous#points previous pointer to correct previous node
                    current.next = None #sets next pointer of delted node to none
                    current.previous = None#sets prev pointer of delted node to none
                    current = None#gets rid of node needing to be deleted
                    return#done with checking situation

                #situation 4
                else:#if current.next IS None
                    previous = current.previous #stores pointer to previous
                    previous.next = None #points previous pointer to null
                    current.previous = None #gets rid of previous pointer
                    current = None #gets rid of node needing to be deleted
                    return 
            current = current.next


dllist = DoubleLinkedList()#creates double linked list object based on class
dllist.append(100)#calls DLL funtion append
dllist.append(200)#appends value
dllist.append(300)#appends value
dllist.prepend(50)
dllist.append(400)#appends value

dllist.delete(100)#calls DLL function delete


dllist.print_list()#calls DLL function print_list