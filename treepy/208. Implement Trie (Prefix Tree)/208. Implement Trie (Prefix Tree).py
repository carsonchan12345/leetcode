class Node:
    def __init__(self, val:str=None):
        self.children:Dict[str, Node]={}
        self.val:Optional[str]=val
        self.end:int=0

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        tmp=self.root
        print(type(tmp.children))
        for char in word:
            if char not in tmp.children:
                tmp.children[char]=Node(char)
            tmp=tmp.children[char]
        tmp.end=1

    def search(self, word: str) -> bool:
        tmp=self.root
        for char in word:
            if char not in tmp.children:
                return False
            tmp=tmp.children[char]
        if tmp.end==1:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        tmp=self.root
        for char in prefix:
            if char not in tmp.children:
                return False
            tmp=tmp.children[char]
        return True
    

    
            
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)