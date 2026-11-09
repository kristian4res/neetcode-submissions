class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        # Helper function for recursion/DFS
        def dfs(index, curr_node):
            for i in range(index, len(word)):
                char = word[i]
                
                if char == ".":
                    for child in curr_node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr_node.children:
                        return False
                    curr_node = curr_node.children[char]

            return curr_node.is_word

        return dfs(0, self.root)

