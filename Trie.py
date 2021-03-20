
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, value):
        current_node = self.root
        for char in value:
            if char in current_node:
                current_node = current_node[char]
            else:
                current_node[char] = {}
                current_node = current_node[char]
        current_node['*'] = None

    def search(self, value):
        current_node = self.root
        for char in value:
            if char in current_node:
                current_node = current_node[char]
            else:
                return 'not found'
        return current_node

    def collectWords(self, root, words=[], current_word=''):
        for k, child in root.items():
            if k == '*':
                words.append(current_word)
            else:
                self.collectWords(
                  child,
                  words=words,
                  current_word=current_word+k
                )
        return words

    def autocomplete(self, value):
        root = self.search(value)
        if root is None:
            return 'not found'
        return self.collectWords(root, words=[], current_word=value)

myTrie = Trie()

# inserting
myTrie.insert('hey')
assert myTrie.root == {'h': {'e': {'y': {'*': None}}}}

myTrie.insert('cat')
myTrie.insert('cattie')
myTrie.insert('catbob')
myTrie.insert('car')
myTrie.insert('close')

# searching
assert myTrie.search('test') == 'not found'
assert myTrie.search('cat') == {
    '*': None,
    't': {'i': {'e': {'*': None}}},
    'b': {'o': {'b': {'*': None}}}
}

# autocomplete
assert myTrie.autocomplete('cat') == ['cat', 'cattie', 'catbob']