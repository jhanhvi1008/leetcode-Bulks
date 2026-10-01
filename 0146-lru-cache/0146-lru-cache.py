class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node()   # Least Recently Used side
        self.right = Node()  # Most Recently Used side

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert node just before the right dummy node
    # This means it becomes Most Recently Used
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        node.prev = prev_node

        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # This key was just used, so make it Most Recently Used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:
            node = self.cache[key]

            # Remove old node
            self.remove(node)

            # Update value
            node.value = value

            # Move to Most Recently Used position
            self.insert(node)

        else:
            # Create new node
            node = Node(key, value)

            # Add to hashmap
            self.cache[key] = node

            # Add to Most Recently Used position
            self.insert(node)

            # Capacity exceeded
            if len(self.cache) > self.capacity:

                # Least Recently Used node
                lru = self.left.next

                # Remove from linked list
                self.remove(lru)

                # Remove from hashmap
                del self.cache[lru.key]