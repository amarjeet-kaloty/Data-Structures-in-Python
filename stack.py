class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def push(self, head, data):
        new_node = node(data)
        if(head == None):
            head = new_node
            return head
        else:
            new_node.next = head
            head = new_node
        return head

    def display(self, head):
        elem = []
        if(head == None):
            print('Stack is empty')
        else:
            temp = head
            while(temp != None):
                elem.append(temp.data)
                temp = temp.next
            
        print(elem)

    def pop(self, head):
        if(head == None):
            return None
        else:
            temp = head
            head = head.next 
            temp = None
        return head

    def peek(self, head):
        if(head == None):
            return 0
        else:
            return head.data

    def reverse(self, head):
        if(head != None):
            temp = self.pop(head)
            self.reverse(head)
            insertAtBottom(head, temp)

    def insertAtBottom(self, head, item):
        if(head == None):
            self.push(head, item)
        else:
            temp = self.pop(head)
            insertAtBottom(head, item)
            self.push(head, temp)


if __name__ == '__main__':
    f = open('input.txt', 'r')
    myList = stack()
    while True:
        char = f.read(1)
        if(char == 'p'):
            data = int(f.read(3))
            myList.head = myList.push(myList.head, data)
        if(char == 'd'):
            myList.display(myList.head)
        if(char == 'o'):
            myList.head = myList.pop(myList.head)
        if(char == 'e'):
            result = myList.peek(myList.head)
            if(result == 0):
                print('Stack is empty')
            else:
                print(result)
        if(char == 'q'):
            break

    f.close()

    myList.head = myList.reverse(myList.head)
    myList.display(myList.head)
        