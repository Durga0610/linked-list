   class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class Circularlist:
    def _init_(self):
        self.head=None
        self.temp=None
        self.tail=None
    def create(self):
        size=int(input("Enter the Size of the List:"))
        for i in range(size):
            value=int(input("Enter the Value:"))
            newnode=Node(value)
            if self.head is None:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
            self.tail.next=self.head
    def display(self):
        self.temp=self.head
        while self.temp.next is not self.head:
            print(self.temp.data)
            self.temp=self.temp.next
        print(self.temp.data)
    def insertfront(self):
        value=int(input("Enter the Value:"))
        newnode=Node(value)
        newnode.next=self.head
        self.head=newnode
        self.tail.next=self.head
obj=Circularlist()
obj.create()
obj.insertfront()
obj.display()
