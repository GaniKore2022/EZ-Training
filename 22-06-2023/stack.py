stack=[]
def push():
    element=int(input("Enter the element:"))
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed element:",e)
        print(stack)
while True:
    print('''select operations:
1.Push
2.Pop
3.Quit''')
    choice=int(input("Enter choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter the Correct Option")
