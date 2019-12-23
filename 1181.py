import collections

class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        res = set()
        def get_head(s):
            head = ""
            for i in range(len(s)):
                if s[i] == " ":
                    return head, i+1
                else:
                    head += s[i]
            return head, i+1
        
        def get_tail(s):
            tail = ""
            for i in range(len(s)-1, -1, -1):
                if s[i] == " ":
                    return tail, i-1
                else:
                    tail = s[i] + tail
            return tail, i-1
        heads = collections.defaultdict(list)
        tails = collections.defaultdict(list)
        for i, phrase in enumerate(phrases):
            head, begin = get_head(phrase)
            tail, end = get_tail(phrase)
            if head in tails:
                for j in tails[head]:
                    if phrase[begin:]:
                        res.add(phrases[j] + " " + phrase[begin:])
                    else:
                        res.add(phrases[j])
            if tail in heads:
                for j in heads[tail]:
                    if phrase[:end+1]:
                        res.add(phrase[:end+1] + " " + phrases[j])
                    else:
                        res.add(phrases[j])
            heads[head].append(i)
            tails[tail].append(i)
        return sorted(list(res))


