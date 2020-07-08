class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # given a string of just parentheses
        # go through the string
        # keep track if something is the correct closing parentheses
        # O(N) where n is length of the string
        # {[]}
        stack = []
        par_mapping = {"}": "{", "]": "[", ")": "("}
        for p in s:
            if p in par_mapping:
                if len(stack) == 0:
                    return False
                most_recent = stack.pop()
                if par_mapping[p] != most_recent:
                    return False
            else:
                stack.append(p)
        if len(stack) != 0:
            return False
        return True

    # DAY TWO LECTURE CODE

    hash_table = [None] * 8   # 8 slots, all initiailized to None


def my_hash(s):
    sb = s.encode()  # Get the UTF-8 bytes for the string
    total = 0
    for b in sb:
        total += b
        total &= 0xffffffff  # clamp to 32 bits
    return total


def hash_index(key):
    h = my_hash(key)
    return h % len(hash_table)


def put(key, val):
    i = hash_index(key)
    if hash_table[i] != None:
        print(f"Collision! Overwriting {repr(hash_table[i])}!")
    hash_table[i] = val


def get(key):
    i = hash_index(key)
    return hash_table[i]


def delete(key):
    i = hash_index(key)
    hash_table[i] = None


put("Hello", "Hello Value")
put("World", "World Value")


#####
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
      # start at the head
      # loop through the list
      # find value
      # return the node

    def delete(self, value):
      return None

    def insert_at_head(self, node):
      return None

  #####
  class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def find(self, value):
      # start at the head
      # loop through the list
      # find value
      # return the node
      cur = self.head
      while cur is not None:
        if cur.value == value:
          return cur
        cur = cur.next
      return None
    def delete(self, value):
      cur = self.head
      if cur.value == value:
        self.head = cur.next
        return cur
      prev = cur
      cur = cur.next
      while cur is not None:
        if cur.value == value:
          prev.next = cur.next
          return cur
        else:
          prev = cur
          cur = cur.next
      return None
    def insert_at_head(self, node):
      node.next = self.head
      self.head = node
