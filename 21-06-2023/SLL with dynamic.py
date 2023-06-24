class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_pos(self, pos, data):
        new_node = Node(data)
        if self.is_empty() or pos<=0:
            self.insert_at_beginning(data)
        else:
            current = self.head
            c=1
            while c<pos and current.next is not None:
                current=current.next
                c+=1
            new_node.next=current.next
            current.next=new_node

    def delete_node(self, data):
        if self.is_empty():
            print("Linked list is empty. Deletion failed.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print("Value not found in the linked list. Deletion failed.")

    def display(self):
        if self.is_empty():
            print("Linked list is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("NULL")

# Example usage
linked_list = LinkedList()

while True:
    print("\nSingly Linked List Operations:")
    print("1. Insert at the beginning")
    print("2. Insert at the end")
    print("3. Insert after a value")
    print("4. Delete a node")
    print("5. Display the linked list")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))
    if choice == 1:
        data = int(input("Enter the data to insert at the beginning: "))
        linked_list.insert_at_beginning(data)
        print("Node inserted at the beginning.")
    elif choice == 2:
        data = int(input("Enter the data to insert at the end: "))
        linked_list.insert_at_end(data)
        print("Node inserted at the end.")
    elif choice == 3:
        pos = int(input("Enter the position at which to insert: "))
        data = int(input("Enter the data to insert: "))
        linked_list.insert_at_pos(pos, data)
        print("Node inserted after the given value.")
    elif choice == 4:
        data = int(input("Enter the data to delete: "))
        linked_list.delete_node(data)
    elif choice == 5:
        linked_list.display()
    elif choice == 6:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
