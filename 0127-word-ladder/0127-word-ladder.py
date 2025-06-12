class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        li = []
        heapq.heapify(li)
        heapq.heappush(li, [1, beginWord])
        setword = set(wordList)
        while li:
            wei, node = heapq.heappop(li)
            if node == endWord : return wei
            node = list(node)
            orig = node[:]
            for i in range(len(node)):
                for j in range(97 , 123):
                    node[i] = chr(j)
                    wor = "".join(node)
                    if wor in setword:
                        heapq.heappush(li , [wei+1 ,wor])
                        setword.remove(wor)
                node = orig[:]
        return 0


            

