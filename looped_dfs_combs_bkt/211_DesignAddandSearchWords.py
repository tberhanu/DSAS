
class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class WordDictionary:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                cur.children[w] = Node()
                cur = cur.children[w]
        cur.is_end = True

    def search(self, word: str) -> bool:
        j, cur = 0, self.root
        def dfs(j, cur):
            for i in range(j, len(word)):
                w = word[i]
                if w != ".":
                    if w not in cur.children.keys():
                        return False
                    cur = cur.children[w]
                else:
                    for char in cur.children.keys():
                        child = cur.children[char]
                        if dfs(i + 1, child):
                            return True
                    return False

            return cur.is_end

        return dfs(j, cur)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)