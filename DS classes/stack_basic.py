class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        return self.stack_list.append(value)  # O(1)

    def pop(self):
        if self.is_empty():
            return None

        return self.stack_list.pop()  # O(1)

    # helper function
    def is_empty(self):
        return self.size() == 0  # O(1)

    # helper function
    def top(self):
        if self.is_empty():
            return None

        return self.stack_list[-1]  # O(1)

    # helper function
    def size(self):
        return len(self.stack_list)  # O(1)


stack = Stack()

for i in range(5):
    stack.push(i)

print(f"Top = {str(stack.top())}")

for x in range(5):
    print(stack.pop())

print(f"Is the stack empty? : {str(stack.is_empty())}")
