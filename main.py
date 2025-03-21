import json
from trie import Trie, TrieNode

# Load the list of bad words
nono_words = []
with open('bad_words.json', 'r') as f:
  nono_words = json.load(f)

# Sort the list of bad words by length
# This ensures that the trie is built such that any words which are
# prefixes of other words are inserted first.
nono_words.sort(key=len)

tree = Trie()

for word in nono_words:
  tree.insert(word)

new_nono_words = tree.construct_all_words()
new_nono_words_set = set(new_nono_words)
new_nono_words = list(new_nono_words_set)
new_nono_words.sort()

words = []
for word in new_nono_words:
  for second_word in new_nono_words:
    if word == second_word:
      continue
    if word in second_word:
      words.append(second_word)

for word in words:
  # print(word)
  new_nono_words.remove(word)

with open('new_bad_words.json', 'w') as f:
  json.dump(new_nono_words, f)

print(':)')

