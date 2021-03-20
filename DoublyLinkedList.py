

class Node:
  def __init__(self, value, next_node=None, previous_node=None):
      self.value = value
      self.next_node = next_node
      self.previous_node = previous_node

class DoublyLinkedList:
  def __init__(self, first_node: Node, last_node: Node):
      self.first_node = first_node
      self.last_node = last_node

  def read_last(self):
      return self.last_node.value

  def print_all_from_beginning(self):
      current_node = self.first_node
      arr = []
      while current_node != self.last_node:
          arr.append(current_node.value)
          current_node = current_node.next_node
      arr.append(current_node.value)
      return arr

  def print_all_from_end(self):
      current_node = self.last_node
      arr = []
      while current_node.previous_node is not None:
          arr.append(current_node.value)
          current_node = current_node.previous_node
      arr.append(current_node.value)
      return arr

  def read(self, idx):
      current_node = self.first_node
      for i in range(idx+1):
          if i == idx:
              return current_node
          else:
              if current_node.next_node is None:
                  return 'Aint here, sorry'
              current_node = current_node.next_node

  def insert_at_start(self, val):
      new_node = Node(value=val, next_node=self.first_node)
      self.first_node.previous_node = new_node
      self.first_node = new_node

  def insert_at_end(self, val):
      new_node = Node(value=val, previous_node=self.last_node)
      self.last_node.next_node = new_node
      self.last_node = new_node

  def insert_at_any(self, idx, val):
      # check that we're not dealing
      # with the first OR last node of the DLL
      if self.read(idx) == self.last_node:
          self.insert_at_end(val)
      elif self.read(idx) == self.first_node:
          self.insert_at_start(val)
      else:
          # otherwise, insert:
          _new_node = Node(value=val)
          _prev_node = self.read(idx-1)
          _next_node = self.read(idx)
          _prev_node.next_node = _new_node
          _new_node.next_node = _next_node
          _next_node.previous_node = _new_node
          _new_node.previous_node = _prev_node

  def search(self, val):
      current_node = self.first_node
      index = 0
      while current_node.value != val:
          index += 1
          if current_node.next_node is None:
              return 'Aint here, sorry'
          current_node = current_node.next_node
      return index

  def delete_last(self):
      second_to_last = self.last_node.previous_node
      second_to_last.next_node = None
      self.last_node = second_to_last

node_1, node_2, node_3, node_4, node_5, node_6 = \
  Node(value='I'), Node(value='am'), Node(value='happy'), \
  Node(value='to'), Node(value='go'), Node(value='home')

DLL = DoublyLinkedList(first_node=node_1, last_node=node_6)

node_1.next_node = node_2
node_2.previous_node, node_2.next_node = node_1, node_3
node_3.previous_node, node_3.next_node = node_2, node_4
node_4.previous_node, node_4.next_node = node_3, node_5
node_5.previous_node, node_5.next_node = node_4, node_6
node_6.previous_node = node_5

# reading stuff
assert DLL.read_last() == 'home'
assert DLL.print_all_from_beginning() == \
      ['I', 'am', 'happy', 'to', 'go', 'home']
assert DLL.print_all_from_end() == \
      ['home', 'go', 'to', 'happy', 'am', 'I']
assert DLL.read(2).value == 'happy'
assert DLL.read(999) == 'Aint here, sorry'

# inserting at beginning
DLL.insert_at_start(val='Hey!!')
assert DLL.read(0).value == 'Hey!!'
assert DLL.print_all_from_beginning() == \
     ['Hey!!', 'I', 'am', 'happy', 'to', 'go', 'home']
assert DLL.read(0).value == 'Hey!!'

# inserting at end
DLL.insert_at_end(val='today')
assert DLL.read_last() == 'today'
assert DLL.print_all_from_beginning() == \
     ['Hey!!', 'I', 'am', 'happy', 'to', 'go', 'home', 'today']
assert DLL.read(7).value == 'today'

# inserting at any index
DLL.insert_at_any(6, 'back')
assert DLL.print_all_from_beginning() == \
     ['Hey!!', 'I', 'am', 'happy',
     'to', 'go', 'back', 'home', 'today']
assert DLL.read(6).next_node == DLL.read(7)
assert DLL.read(6).previous_node == DLL.read(5)
assert DLL.read(5).next_node == DLL.read(6)
assert DLL.read(7).previous_node == DLL.read(6)
DLL.insert_at_any(0, 'START')
assert DLL.print_all_from_beginning() == \
     ['START', 'Hey!!', 'I', 'am', 'happy',
     'to', 'go', 'back', 'home', 'today']
DLL.insert_at_any(9, 'END')
assert DLL.print_all_from_beginning() == \
     ['START', 'Hey!!', 'I', 'am', 'happy',
     'to', 'go', 'back', 'home', 'today', 'END']

# searching
assert DLL.search('back') == 7
assert DLL.search('today') == 9
assert DLL.search('TEST-TEST') == 'Aint here, sorry'

# deleting
assert DLL.print_all_from_beginning() == \
     ['START', 'Hey!!', 'I', 'am', 'happy',
     'to', 'go', 'back', 'home', 'today', 'END']
DLL.delete_last()
assert DLL.print_all_from_beginning() == \
     ['START', 'Hey!!', 'I', 'am', 'happy',
     'to', 'go', 'back', 'home', 'today']
DLL.delete_last()
assert DLL.print_all_from_beginning() == \
     ['START', 'Hey!!', 'I', 'am', 'happy',
     'to', 'go', 'back', 'home']
assert DLL.read(8).next_node is None
assert DLL.read(8).previous_node.value == 'back'
assert DLL.read(7).next_node.value == 'home'
assert DLL.read(7).previous_node.value == 'go'