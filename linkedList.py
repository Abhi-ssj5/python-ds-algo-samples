class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            
            temp.next = Node(value)
    
    def remove(self, value):
        temp = self.head

        if temp == None:
            return
        elif temp.value == value:
            temp = temp.next
            return
        
        # prev = None
        # while temp != None and temp.value != value:
        #     prev = temp
        #     temp = temp.next

        # if temp.value == value:
        #     prev.next = temp.next            

    
    def __str__(self):
        temp = self.head
        stringValue = ""

        while temp != None:
            stringValue = stringValue + str(temp.value) + " "
            temp = temp.next
        
        return stringValue

def main():
    linkedList = LinkedList()
    linkedList.append(2)
    linkedList.append(4)
    linkedList.append(4)
    linkedList.append(0)
    linkedList.append(1)

    print(linkedList)

    linkedList.remove(5)

    print(linkedList)


if __name__ == "__main__":
    main()