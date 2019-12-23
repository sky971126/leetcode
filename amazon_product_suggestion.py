
class TrieNode():
    def __init__ (self):
        self.children = {}
        self.end = False
    
class Trie():
    def __init__ (self):
        self.root = TrieNode()
    
    def insert(self, repo):
        for s in repo:
            cur = self.root
            for c in s:
                c = c.lower()
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.end = True
    
    def find(self, node, s):
        if not node:
            return None
        cur = node
        for c in s:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return None
        return cur
    
    def find3(self, node, res, s):
        if not node:
            return None
        if len(res) >= 3:
            return
        if node.end == True:
            res.append(s)
        for c in sorted(node.children.keys()):
            self.find3(node.children[c], res, s+c)
        

            
    
def solution(repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], customerQuery = "monger"):
    res_list = []
    trie = Trie()
    trie.insert(repository)
    cur = trie.find(trie.root, customerQuery[:2])
    res = []
    trie.find3(cur, res, customerQuery[:2])
    res_list.append(res)

    for i in range(2,len(customerQuery)):
        cur = trie.find(cur, customerQuery[i])
        res = []
        trie.find3(cur, res, customerQuery[:i+1])
        res_list.append(res)
    return res_list


print(solution())
print(solution(repository=["ps4", "ps4 slim", "ps4 pro", "xbox", "tissue",
                    "standing table", "house", "true love", "tracking device"], customerQuery="ps4"))