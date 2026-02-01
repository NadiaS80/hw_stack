class Stack:
    """
    Simple stack data structure implementation (LIFO).
    Provides basic stack operations: push, pop, peek, size and empty check.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.the_list = []

    def is_empty(self):
        """
        Check whether the stack is empty.
        :return: True if the stack is empty, False otherwise.
        """
        if len(self.the_list) == 0:
            return True
        return False

    def push(self, element):
        """
        Push an element onto the top of the stack.
        :param item: Element to be added to the stack.
        :return: None
        """
        self.the_list.append(element)

    def pop(self):
        """
        Remove and return the top element of the stack.
        :return: Top element of the stack.
        :return None: If the stack is empty.
        """
        if self.is_empty():
            return None
        element = self.the_list.pop()
        return element

    def peek(self):
        """
        Return the top element of the stack without removing it.
        :return: Top element of the stack.
        :return None: If the stack is empty.
        """
        if self.is_empty():
            return None
        return self.the_list[-1]

    def size(self):
        """
        Return the number of elements in the stack.
        :return: Stack size as an integer.
        """
        return len(self.the_list)