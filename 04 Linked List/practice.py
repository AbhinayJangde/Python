class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start == None
    def insertAtFirst(self,data):
        n=Node(data,self.start)
        self.start = n
    def traverse(self):
        temp=self.start
        while temp is not None:
            print(temp.data,"->", end=" ")
            temp = temp.next
        print("None")
    def insertAtLast(self,data):
        n=Node(data)
        if self.start != None:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    def search(self, item):
        temp = self.start
        if self.start != None:
            while temp is not None:
                if temp.data == item:
                    return temp
                temp = temp.next
            return None
        return None

    def delete_item(self, item):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.data == item:
                self.start = None

        else:
            temp = self.start
            if temp.data == item:
                self.start = temp.next
            else:
                while temp.next != None:
                    if temp.next.data == item:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    
    
sll = SLL()
sll.insertAtFirst(1)
sll.insertAtFirst(3)
sll.insertAtFirst(5)
sll.insertAtLast(8)
print("sll is empty",sll.is_empty())
sll.traverse()
res = sll.search(5)
print(res.data)
sll.delete_item(8)
sll.traverse()
