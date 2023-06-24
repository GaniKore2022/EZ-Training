class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node is not in the list.")
            return
        new_node = Node(data)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node

    def delete(self, data):
        if self.is_empty():
            print("List is empty.")
            return
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
        print("Item not found in the list.")

    def display(self):
        if self.is_empty():
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_reverse(self):
        if self.head is None:
            print("Doubly linked list is empty.")
        else:
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(current.data, end=" ")
                current = current.prev
# Example usage
dll = DoublyLinkedList()

while True:
    print("\nDoubly Linked List Operations:")
    print("1. Append")
    print("2. Prepend")
    print("3. Insert After")
    print("4. Delete")
    print("5. Display")
    print("6.Display reverse")
    print("7. Quit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        data = int(input("Enter the value to append: "))
        dll.append(data)
        print("Value appended successfully.")
    elif choice == 2:
        data = int(input("Enter the value to prepend: "))
        dll.prepend(data)
        print("Value prepended successfully.")
    elif choice == 3:
        data = int(input("Enter the value to insert: "))
        prev_node_data = int(input("Enter the value of previous node: "))
        prev_node = None
        current = dll.head
        while current:
            if current.data == prev_node_data:
                prev_node = current
                break
            current = current.next
        dll.insert_after(prev_node, data)
        print("Value inserted successfully.")
    elif choice == 4:
        data = int(input("Enter the value to delete: "))
        dll.delete(data)
        print("Value deleted successfully.")
    elif choice == 5:
        dll.display()
    elif choice == 6:
        dll.display_reverse()
    elif choice == 7:
        break
    else:
        print("Invalid choice. Try again.")
