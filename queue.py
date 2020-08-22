class node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.back = None
    
    def enqueue(self, data):
        new_node = node(data)
        if(self.front == None and self.back == None):
            self.front = self.back = new_node
            return self.front
        self.back.next = new_node
        self.back = new_node
        return self.front
    
    def display(self):
        if(self.front == None and self.back == None):
            return 
        elem = []
        temp = self.front
        while(temp != None):
            elem.append(temp.data)
            temp = temp.next
        print(elem)

    def deque(self):
        if(self.front == None and self.back == None):
            return None
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return self.front

if __name__ == '__main__':
    f = open('input.txt', 'r')
    myList = queue()
    while True:
        char = f.read(1)
        if(char == 'e'):
            data = int(f.read(3))
            myList.front = myList.enqueue(data)
        if(char == 'd'):
            myList.display()
        if(char == 'u'):
            myList.front = myList.deque()
        # if(char == 'e'):
        #     result = myList.peek(myList.head)
        #     if(result == 0):
        #         print('Stack is empty')
        #     else:
        #         print(result)
        if(char == 'q'):
            break

    f.close()
        