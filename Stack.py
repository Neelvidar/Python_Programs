# Q. 1 Create a Stack with following operations
#      1. Push
#      2. Pop
#      3. Display
#      4. Reverse String using Stack
#      5. Reverse Stack using another Stack


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack (top -> bottom):", end=" ")
        for i in range(len(self.items) - 1, -1, -1):
            print(self.items[i], end=" ")
        print()

    def reverse_string(self, text):
        temp = Stack()
        for ch in text:
            temp.push(ch)
        result = ""
        while not temp.is_empty():
            result += temp.pop()
        return result

    def reverse_stack(self):
        # move every element to another stack, which reverses the order
        other = Stack()
        while not self.is_empty():
            other.push(self.pop())
        self.items = other.items


def main():
    s = Stack()
    while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Reverse String using Stack")
        print("5. Reverse Stack using another Stack")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == '1':
            s.push(input("Enter element to push: "))
            print("Pushed")
        elif choice == '2':
            v = s.pop()
            if v is None:
                print("Stack Underflow: stack is empty")
            else:
                print("Popped:", v)
        elif choice == '3':
            s.display()
        elif choice == '4':
            text = input("Enter a string: ")
            print("Reversed string:", s.reverse_string(text))
        elif choice == '5':
            s.reverse_stack()
            print("Stack reversed")
            s.display()
        elif choice == '0':
            print("Bye")
            break
        else:
            print("Invalid choice")


main()