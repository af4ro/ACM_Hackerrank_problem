class Node:
    next = None
    value = ''
    def __init__(self,val):
        self.value = val

    def appendToTail(self, d):
        a = self
        while a.next != None:
            a = a.next
        a.next = d

def reverse(node,ls=[]):
    if ls == []:
        temp = node.next
        node.next = None
        ls.append(node)
        return reverse(temp,ls)
    if node.next == None:
        node.next = ls[-1]
        return node
    temp = node.next
    node.next = ls[-1]
    ls.append(node)
    return reverse(temp,ls)

def printit(node):
    while node != None:
        print(node.value)
        node = node.next

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.next = b
b.next = c
c.next = d
d.next = None
printit(a)
printit(reverse(a))

