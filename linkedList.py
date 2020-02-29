class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head = node()

    #Insert new node in the Linked-List
    def append(self, data):
        new_node = node(data)
        cur_node = self.head
        while (cur_node.next != None):
            cur_node = cur_node.next
        cur_node.next = new_node

    #Display the Linked-List
    def display(self):
        elems = [] 
        cur_node = self.head
        while (cur_node.next != None):
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    #Length of the Linked-List
    def length(self):
        total=0
        cur_node = self.head
        while (cur_node.next != None):
            cur_node = cur_node.next
            total+=1
        return total
    
    #Delete the last node
    def delete(self):
        if(self.head.next == None):
            return None

        cur_node = self.head
        while(cur_node.next.next != None):
            cur_node = cur_node.next
        cur_node.next = None
        return cur_node

myList = linkedList()
myList.delete()
myList.display()
myList.append(40)
myList.display()
myList.delete()
myList.display()

    
   