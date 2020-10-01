class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    # helper function
    def get_head(self):
        return self.head_node  # O(1)

    # supplementary print function
    def print_list(self):
        if self.is_empty():
            print("List is empty")
            return False

        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element

        print(temp.data, end="-> None")
        return True

    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.get_head() is None:
            self.head_node = new_node
            return

        temp = self.get_head()

        while temp.next_element:
            temp = temp.next_element

        temp.next_element = new_node
        return  # O(N)

    def insert_at_head(self, data):
        temp_node = Node(data)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node  # O(1)

    def delete(self, value):
        deleted = False

        if self.is_empty():
            print("List is empty")
            return deleted

        curr_node = self.get_head()
        prev_node = None

        if curr_node.data is value:
            self.delete_at_head()
            deleted = True
            return deleted

        while curr_node:
            if curr_node.data is value:
                prev_node.next_element = curr_node.next_element
                curr_node.next = None
                deleted = True
                break

            prev_node = curr_node
            curr_node = curr_node.next_element

        if deleted:
            print(f"{str(value)} is deleted!")

        else:
            print(f"{str(value)} is not in the list!")

        return deleted  # O(N)

    def delete_at_head(self):
        first_element = self.get_head()

        if first_element:
            self.head_node = first_element.next_element

        return  # O(1)

    def search(self, value):
        if self.is_empty():
            return False

        curr_node = self.head_node

        while curr_node:
            if curr_node.data is value:
                return True

            curr_node = curr_node.next_element

        return False  # O(N) --> both recursive and iterative

    # helper function
    def is_empty(self):
        if self.head_node is None:
            return True  # O(1)

        return False  # O(1)
