#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        if word == "":
            self.trie["end"] = True
            return
        if word[0] in self.trie:
            sub_trie = self.trie[word[0]]
        else:
            sub_trie = Trie()
            self.trie[word[0]] = sub_trie
        sub_trie.insert(word[1:])
        return
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        if word == "":
            if "end" in self.trie:
                return True
            else:
                return False 
        if word[0] in self.trie:
            return self.trie[word[0]].search(word[1:])
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if prefix == "":
            return True
        if prefix[0] in self.trie:
            return self.trie[prefix[0]].startsWith(prefix[1:])
        else:
            return False


# Your Trie object will be instantiated and called as such:
#obj = Trie()
#obj.insert("apple")
#param_2 = obj.search("apple")

