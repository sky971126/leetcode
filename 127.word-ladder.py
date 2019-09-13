#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
from collections import defaultdict
from queue import Queue
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if not wordList or endWord not in wordList:
            return 0
        WORDS = defaultdict(list)
        L = len(wordList[0])
        for word in wordList:
            for i in range(L):
                WORDS[word[:i] + "*" + word[i+1:]].append(word)
        que = Queue()
        VISITED = set()
        que.put((beginWord, 1))
        while not que.empty():
            word, length = que.get()
            for i in range(L):
                word_star = word[:i] + "*" + word[i+1:]
                if word_star in WORDS:
                    for w in WORDS[word_star]:
                        if w == endWord:
                            return length + 1
                        if w in VISITED:
                            continue
                        else:
                            VISITED.add(w)
                        que.put((w, length+1))
        return 0

