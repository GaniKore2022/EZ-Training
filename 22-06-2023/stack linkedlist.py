class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Pushed {data} to the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
            return None

        popped_value = self.head.data
        self.head = self.head.next
        print(f"Popped {popped_value} from the stack.")
        return popped_value

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None

        return self.head.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        current = self.head
        print("Stack elements:")
        while current:
            print(current.data)
            current = current.next


# Creating an empty stack
stack = Stack()

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        data = input("Enter the value to push: ")
        stack.push(data)
    elif choice == '2':
        popped_value = stack.pop()
        if popped_value is not None:
            print("Popped value:", popped_value)
    elif choice == '3':
        top_value = stack.peek()
        if top_value is not None:
            print("Top value:", top_value)
    elif choice == '4':
        stack.display()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
