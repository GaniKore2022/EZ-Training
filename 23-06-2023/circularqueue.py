class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return

        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
        else:
            data = self.head.data
            self.tail.next = self.head.next
            self.head = self.head.next

        return data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()


# Example usage
queue = CircularQueue()

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element to enqueue: "))
        queue.enqueue(data)
    elif choice == 2:
        data = queue.dequeue()
        if data is not None:
            print("Dequeued element:", data)
    elif choice == 3:
        queue.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")