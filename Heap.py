
class Heap:

  def __init__(self):
      self.tree = []

  def __find_parent_node_index(self, idx):
      return (idx-1) // 2

  def __find_left_child(self, idx):
      return (idx*2) + 1

  def __find_right_child(self, idx):
      return (idx*2) + 2

  def __find_biggest_child_idx(self, idx):
      left_child_idx = self.__find_left_child(idx)
      right_child_idx = self.__find_right_child(idx)
      if self.tree[left_child_idx] > self.tree[right_child_idx]:
          return left_child_idx
      else:
          return right_child_idx

  def insert_(self, value):
      self.tree.append(value)
      last_idx = len(self.tree)-1
      parent_idx = self.__find_parent_node_index(last_idx)
      while value > self.tree[parent_idx]:
          self.tree[last_idx], self.tree[parent_idx] = self.tree[parent_idx], self.tree[last_idx]
          last_idx = parent_idx
          parent_idx = self.__find_parent_node_index(last_idx)
          if parent_idx < 0:
              break

  def delete_(self):
      # swap
      self.tree[0] = self.tree[-1]
      del self.tree[-1]

      # trickle down
      root_node_idx = 0
      highest_child_idx = self.__find_biggest_child_idx(root_node_idx)
      while self.tree[root_node_idx] < self.tree[highest_child_idx]:
          # swap
          self.tree[root_node_idx], self.tree[highest_child_idx] = self.tree[highest_child_idx], self.tree[root_node_idx]
          root_node_idx = highest_child_idx
          # find next children.
          try:
              highest_child_idx = self.__find_biggest_child_idx(root_node_idx)
          except IndexError:
              # IndexError means we reached the bottom of the tree
              return

myHeap = Heap()

# insertion
myHeap.insert_(2), myHeap.insert_(88), myHeap.insert_(25)
myHeap.insert_(1000), myHeap.insert_(87), myHeap.insert_(16)
assert myHeap.tree == [1000, 88, 25, 2, 87, 16]

# deletion
myHeap.delete_()
assert myHeap.tree == [88, 87, 25, 2, 16]

# insertion at very bottom
myHeap.insert_(1)
assert myHeap.tree == [88, 87, 25, 2, 16, 1]

# insertion at top
myHeap.insert_(9999)
assert myHeap.tree == [9999, 87, 88, 2, 16, 1, 25]

# triple deletion
myHeap.delete_(), myHeap.delete_(), myHeap.delete_()
assert myHeap.tree == [25, 16, 1, 2]