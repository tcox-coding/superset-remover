# Load words into trie.
class TrieNode:
  def __init__(self, char: str, word: str = ''):
    self.char = char
    self.children = {}
    self.is_end_of_word = False
    self.word = word + char
  
# Trie data structure
class Trie:
  def __init__(self):
    self.root = TrieNode('')

  def insert(self, word: str):
    node = self.root
    for char in word:
      # Check if the character is not in the children of the node
      # and the node is not the end of a word.
      if char not in node.children and node.is_end_of_word == False:
        node.children[char] = TrieNode(char, node.word)
      elif node.is_end_of_word == True:
        return False
      node = node.children[char]
    node.is_end_of_word = True
    return True

  def construct_all_words(self):
    words = []
    stack = [self.root]
    while stack:
      node = stack.pop()
      if node.is_end_of_word:
        words.append(node.word)
      for child in node.children.values():
        stack.append(child)
    return words
