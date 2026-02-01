class Stack:

    def __init__(self):
        self.the_list = []

    def is_empty(self):
        if len(self.the_list) == 0:
            return True
        return False

    def push(self, element):
        self.the_list.append(element)

    def pop(self):
        if self.is_empty():
            return None
        element = self.the_list.pop()
        return element

    def peek(self):
        if self.is_empty():
            return None
        return self.the_list[-1]

    def size(self):
        return len(self.the_list)