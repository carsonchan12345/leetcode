
from typing import Dict, List

class TrieTree:
    def __init__(self) -> None:
        self.children={}
        self.isEnd=False

    def addWord(self, word:str):
        tmp= self
        for w in word:
            if w not in tmp.children:
                tmp.children[w]=TrieTree()
            tmp=tmp.children[w]
        tmp.isEnd=True


class Solution:

    def __init__(self) -> None:
        self.root=TrieTree()
        self.rowLimit, self.colLimit=int(), int()
        self.res, self.visit =set(), set()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.root.addWord(word)
        self.rowLimit=len(board)
        self.colLimit=len(board[0])

        def dfs(row:int, col:int, node:TrieTree, word:str):
            if (row<0 or col<0 or row>=self.rowLimit or col>=self.colLimit or (row,col) in self.visit or board[row][col] not in node.children):
                return
            
            self.visit.add((row,col))
            node=node.children[board[row][col]]
            word+=board[row][col]
            if (node.isEnd):
                self.res.add(word)
            dfs(row+1,col,node,word)
            dfs(row-1,col,node,word)
            dfs(row,col+1,node,word)
            dfs(row,col-1,node,word)
            self.visit.remove((row,col))

        for c in range(self.colLimit):
            for r in range(self.rowLimit):
                dfs(r,c,self.root,"")

        return list(self.res)

