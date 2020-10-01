class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.get_head():
            return False

        return True

    def insert_at_head(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            return self.head

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return self.head

    def print_list(self):
        if self.is_empty():
            print("List is empty")
            return False

        temp_node = self.head
        while temp_node.next:
            print(temp_node.data, end=" -> ")
            temp_node = temp_node.next

        print(temp_node.data, end="-> None")
        return True

    def delete(self, value):
        deleted = False

        if self.is_empty():
            print("List is empty")
            return deleted

        curr_node = self.get_head()

        if curr_node.data is value:
            self.head = curr_node.next
            curr_node.next.prev = None
            deleted = True
            print(f"{str(curr_node.data)} is deleted!")
            return deleted

        while curr_node:
            if curr_node.data is value:
                if curr_node.next:
                    prev = curr_node.prev
                    next_node = curr_node.next
                    prev.next = next_node
                    next_node.prev = prev

                else:
                    curr_node.prev.next = None

                deleted = True
                break

            curr_node = curr_node.next

        if deleted:
            print(f"\n{str(value)} is deleted!")
        else:
            print(f"\n{str(value)} is not in the list!")

        return deleted


dlst = DoublyLinkedList()
for i in range(11):
    dlst.insert_at_head(i)

dlst.print_list()
dlst.delete(7)

dlst.print_list()
dlst.delete(2)

dlst.print_list()

dlst.delete(21)
dlst.print_list()
