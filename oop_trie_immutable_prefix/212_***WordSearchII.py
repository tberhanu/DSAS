class Trie:
    def __init__(self):
        self.children = {}
        self.full_word = None  # store full word when ending

    def insert(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.full_word = word  # store the word at the end


class Solution:
    def findWords(self, board, words):
        root = Trie()
        for w in words:
            root.insert(w)

        result = []
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                self.dfs(board, r, c, root, set(), result)

        return result

    def dfs(self, board, r, c, cur, seen, result):
        if (r, c) in seen:
            return
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return
            
        letter = board[r][c]
        if letter not in cur.children:
            return

        seen.add((r, c))
        cur = cur.children[letter]

        if cur.full_word:
            result.append(cur.full_word)
            cur.full_word = None  # avoid duplicates

        self.dfs(board, r+1, c, cur, seen, result)
        self.dfs(board, r-1, c, cur, seen, result)
        self.dfs(board, r, c+1, cur, seen, result)
        self.dfs(board, r, c-1, cur, seen, result)

        seen.remove((r, c))


        

class Solution2: # Time Limit Exceeded
    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i, word, seen):
            if 0 > r or r >= ROWS or 0 > c or c >= COLS or (r, c) in seen:
                return False
            if i == len(word) - 1 and board[r][c] == word[i]: # Important
                return True
            if board[r][c] != word[i]:
                return False

            seen.add((r, c))

            right, up, down = False, False, False
            left = dfs(r, c - 1, i + 1, word, seen)
            if not left:
                right = dfs(r, c + 1, i + 1, word, seen)
                if not right:
                    up = dfs(r - 1, c, i + 1, word, seen)
                    if not up:
                        down = dfs(r + 1, c, i + 1, word, seen)

            seen.remove((r, c))

            return left or right or up or down

        result = []
        for i in range(len(words)):
            for r in range(ROWS):
                for c in range(COLS):
                    word, seen, index = words[i], set(), 0
                    found = False
                    if dfs(r, c, index, word, seen):
                        result.append(word)
                        found = True # Important
                        break
                if found:
                    break
        return result