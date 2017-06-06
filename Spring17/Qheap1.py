import queue
class Node:
    val = ''
    right = ''
    left = ''

    def __init__(self,val):
        self.val = val

def add_element(node, to_add):
    if node.val == '':
        node = to_add
        return
    if int(to_add.val) > int(node.val):
        add_element(node.right,to_add)
    else:
        add_element(node.left, to_add)

def delete_element(node, to_delete):
    if node.val == '':
        return False
    if node.val
    if int(to_delete) > int(node.val):
        delete_element(node.right,to_delete)
    else:
        delete_element(node.left, to_delete)

n = int(input())
main_node = queue.PriorityQueue()
for i in range(n):
    temp = input().split()
    if temp[0] == '1':
        main_node.put(temp[1])
    elif temp[0] == '2':
        temp = list(main_node)
        temp .remove(temp[1])
        main_node = queue.PriorityQueue(temp)
    else:
        temp = list(main_node)
        print(temp[0])


