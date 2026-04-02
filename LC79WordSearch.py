from typing import List

def exist(board: List[List[str]], word: str) -> bool:

    path = set()

    def search(row, col, wordChr) -> bool:
        if wordChr >= len(word):
            return True
        
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or wordChr >= len(word) or board[row][col] != word[wordChr] or (row, col) in path:
            return False

        path.add((row, col))
        res = search(row + 1, col, wordChr+1) or search(row - 1, col, wordChr+1) or search(row, col + 1, wordChr+1) or search(row, col - 1, wordChr+1)
        path.remove((row, col))
        return res



    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0] and search(row, col, 0):
                return True
    
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board, word))
