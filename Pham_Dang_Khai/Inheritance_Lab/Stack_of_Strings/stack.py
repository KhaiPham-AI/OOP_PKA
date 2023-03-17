class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        if isinstance(item, str):
            self.data.append(item)
        else:
            raise ValueError("Stack can only store strings")

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)
