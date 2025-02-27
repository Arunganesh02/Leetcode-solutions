class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lo = False
        def backtrack(li ,poin, istart , jstart, seen):
            nonlocal lo

            if [istart , jstart] in seen:
                return 

            elif li == word:
                lo = True
                return True

            elif li and li[-1] != word[poin-1]:
                return

            elif poin>=len(word):
                return

            elif jstart == len(board[0]) or jstart < 0 or istart == len(board) or istart < 0:
                return

            return backtrack(li+board[istart][jstart] , poin+1 , istart , jstart +1 , seen + [[istart , jstart]])  or backtrack(li+board[istart][jstart] , poin+1 , istart+1 , jstart , seen + [[istart , jstart]]) or backtrack(li+board[istart][jstart] , poin+1 , istart , jstart-1 , seen + [[istart , jstart]]) or backtrack(li+board[istart][jstart] , poin+1 , istart-1 ,jstart , seen + [[istart , jstart]])
            
        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)
        
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (backtrack("",0,i , j , [] )):
                    return True

        return lo