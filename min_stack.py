class min_stack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, item):
        if item < self.min:
            self.min = item
            self.stack.append([item, self.min])
        else:
            self.stack.append([item, self.min])

    def pop(self):
        self.stack.pop()

    def get_min(self):
        return self.stack[-1][1]
