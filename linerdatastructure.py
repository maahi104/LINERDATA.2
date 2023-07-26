# # QUESTION 3

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def merge_alternate(self, other):
        curr1 = self.head
        curr2 = other.head
        while curr1 and curr2:
            temp = curr1.next
            curr1.next = curr2
            curr2 = curr2.next
            curr1.next.next = temp
            curr1 = temp

        other.head = curr2

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next

# Example usage
l1 = LinkedList()
l2 = LinkedList()

l1.insert(1)
l1.insert(3)
l1.insert(5)
l2.insert(2)
l2.insert(4)
l2.insert(6)

l1.merge_alternate(l2)
l1.display()

#  QUESTION 4

def count_pairs(arr, target):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                count += 1
    return count


arr = [1, 5, 3, 7, 2]
target = 8
print(count_pairs(arr, target))
