class stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print("Added: ", value)
    def pop(self):
        if self.stack:
            print("Deleted:", self.stack.pop())
        else:
            print("Stack is empty")
    def peek(self):
        if self.stack:
            print("Top: ", self.stack[-1])
        else:
            print("Stack is empty")

    def display(self):
        print("Stack:", self.stack)

    def size(self):
        print("Size:", len(self.stack))


s = stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Size")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        value = input("Enter value")
        s.push(value)
    elif choice == "2":
        s.pop()

    elif choice == "3":
        s.peek()
    elif choice == "4":
        s.display()
    elif choice == "5":
        s.size()

    elif choice == "6":
        break
    else:
        print("Invalid choice")
    
