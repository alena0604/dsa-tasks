class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def enqueue(self, value):
        self.items.append(value)
        return "added at the end"

    def dequeue(self):
        if self.is_empty():
            return "Empty"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Empty"
        else:
            return self.items[0]

    def delete(self):
        self.items = None