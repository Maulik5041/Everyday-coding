class Queue:
    def __init__(self):
        self.queue_list = []

    def size(self):
        return len(self.queue_list)  # O(1)

    def is_empty(self):
        return self.size() == 0  # O(1)

    def enqueue(self, value):
        return self.queue_list.append(value)  # O(1)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(front)
        return front  # O(1)

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]  # O(1)

    def back(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]  # O(1)


queue = Queue()

for i in range(5):
    queue.enqueue(i)
    print(f"Front = {str(queue.front())}; Back = {str(queue.back())}")

print(f"Size of queue = {str(queue.size())}")

for j in range(5):
    print(f"Front = {str(queue.front())}; Back = {str(queue.back())}")
    queue.dequeue()

print(f"Is the queue empty? : {str(queue.is_empty())}")
