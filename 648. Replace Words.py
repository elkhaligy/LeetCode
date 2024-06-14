def replaceWords_bruteforce(dictionary: list[str], sentence: str) -> str:
    sentence = sentence.split()
    for root in dictionary:
        for i, word in enumerate(sentence):
            found = word.find(root)
            if found == 0:
                sentence[i] = root
    
    return ' '.join(sentence)

def replaceWords_bruteforce_2(dictionary: list[str], sentence: str) -> str:
    dct = {}
    sentence = sentence.split()
    dictionary.sort(key=lambda a: len(a))
    for root in dictionary:
        if root[0] in dct:
            dct[root[0]].append(root)
        else:
            dct[root[0]] = []
            dct[root[0]].append(root)

    for ind, word in enumerate(sentence):
        if word[0] in dct:
            for words in dct[word[0]]:
                if word.find(words) == 0:
                    sentence[ind] = words
                    break
    return ' '.join(sentence)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete_child = _delete(node.children[char], word, depth + 1)
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0
            return False
        _delete(self.root, word, 0)

# Example usage:


def replaceWords_opt(dictionary: list[str], sentence: str) -> str:
    trie = Trie()
    for root in dictionary:
        trie.insert(root)

    sentence = sentence.split()
    for word in sentence:
        
    # trie.insert("hello")
    # trie.insert("helium")

    # print(trie.search("hello"))  # Output: True
    # print(trie.search("helix"))  # Output: False
    # print(trie.starts_with("hel"))  # Output: True

    # trie.delete("hello")
    # print(trie.search("hello"))  # Output: False

    
print(replaceWords_opt(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
