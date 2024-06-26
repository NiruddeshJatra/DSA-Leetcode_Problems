class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:
            num = self.queue[0]
            self.queue = self.queue[1:]
            return num
        return -1

    def peek(self) -> int:
        if self.queue:
            num = self.queue[0]
            return num
        return -1

    def empty(self) -> bool:
        if self.queue:
            return 0
        return 1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
