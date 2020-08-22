class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist2:
    def __init__(self):
        self.head = None

    def insert(self, head, data):
        new_node = node(data)
        if(head == None):
            head = new_node
            return head
        else:
            cur_node = head
            while(cur_node.next != None):
                cur_node = cur_node.next
            cur_node.next = new_node
            return head

    def display(self, head):
        elem = []
        if(head == None):
            return None
        else:
            cur_node = head
            while(cur_node != None):
                elem.append(cur_node.data)
                cur_node = cur_node.next
        print(elem)

    #Length of the Linked-List
    def length(self, head):
        total=0
        cur_node = head
        while (cur_node != None):
            total += 1
            cur_node = cur_node.next
        return total

    def mergeSort(self, head):
        if (head == None or head.next == None):
            return head
        middle = self.getMiddle(head)
        other = middle.next

        middle.next = None

        left = self.mergeSort(head)
        right = self.mergeSort(other)

        sortedList = self.sortedMerge(left, right)
        return sortedList

    def getMiddle(self, head):
        if (head == None):
            return head

        slow = head
        fast = head

        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow

    def sortedMerge(self, a, b):
        result = None
        if (a == None):
            return b
        if (b == None):
            return a

        if (a.data <= b.data):
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)

        return result

    def printMiddle(self):
        slow = self.head
        fast = self.head
        if(self.head != None):
            while(fast != None and fast.next != None):
                slow = slow.next
                fast = fast.next.next
        print(f'Middle is: {slow.data}')

    def reverse(self, head):
        if(head == None or head.next == None):
            return head
        remaining = myList.reverse(head.next)
        head.next.next = head
        head.next = None
        print(f'In {head.data}')
        myList.display(remaining)
        return remaining

    def add(self, head):
        total = 0
        if(head.next == None):
            return head.data
        total = head.data + myList.add(head.next)
        return total


if __name__ == '__main__':
        myList = linkedlist2()
        myList.head = myList.insert(myList.head, 1)
        myList.head = myList.insert(myList.head, 2)
        myList.head = myList.insert(myList.head, 3)
        # myList.head = myList.insert(myList.head, 3)
        # myList.head = myList.insert(myList.head, 5)
        myList.display(myList.head)
        # result = myList.length(myList.head)
        # print(f'Length: {result}')
        # myList.head = myList.mergeSort(myList.head)
        # myList.display(myList.head)
        # myList.printMiddle()
        # myList.head = myList.reverse(myList.head)
        result = myList.add(myList.head)
        print(f'List elements value: {result}')
        
