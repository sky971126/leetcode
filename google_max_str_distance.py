

class TrieNode(): 
    
    #binary
    def __init__(self, length, end):
        self.children = [None, None]
        self.length = length
        self.end = end
    
    # 0 add to left, 1 add to right
    def add(self, index, length, end):
        self.children.append(TrieNode(self.length+1, end=False))
    
    def 

