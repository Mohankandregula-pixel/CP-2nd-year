"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    def delete(self):
        if self.head:
            del Linkedlist[0]
            return self.head

    def insert_first(self, new_element):
        self.head.append(new_element)

    def delete_first(self):
        self.head.delete()

class stack(object):
    def __init__(self,top=None):
        self.top = LinkedList(top)

    def push(self, new_element):
        #"Push (add) a new element onto the top of the stack"
        self.top.append(new_element)
        pass

    # def pop(self):
    #     #"Pop (remove) the first element off the top of the stack and return it"
    #     if self.top:
    #         return self.top.pop()
    #     else:
    #         return None
    