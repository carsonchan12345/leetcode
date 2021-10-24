class Node:
    
    def __init__(self,val:str = None):
        self.children:Dict[str, Node]={}
        self.val:Optional[int]=val
        self.end=0
    


class WordDictionary:

    def __init__(self):
        self.root:Node=Node()

    def addWord(self, word: str) -> None:
        tmp=self.root
        
        for char in word:
            if char not in tmp.children:
                tmp.children[char]=Node(char)
            tmp=tmp.children[char]
        tmp.end=1

    def search(self, word: str) -> bool:
        return self.wildcardSearch(word, self.root)
                
    def wildcardSearch(self, word: str, node: Node) -> bool:
        tmp = node
        res:bool=False
        i=1
        for char in word:
            if char=='.' :
                print(word,i,len(word),i!=len(word))
                if i!=len(word):
                    for n in tmp.children:
                        res=self.wildcardSearch(word[i:len(word)], tmp.children[n]) or res
                    return res
                else:
                    if len(tmp.children)==0:
                        return False
                    else:
                        for n in tmp.children:
                            if tmp.children[n].end==1 :
                                print("hi")
                                return True
            else:
                if char in tmp.children:
                    tmp=tmp.children[char]
                else: 
                    return False
            i+=1
        if tmp.end==1:
            return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)