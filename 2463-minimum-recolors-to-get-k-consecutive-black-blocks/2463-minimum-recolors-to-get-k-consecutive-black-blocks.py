class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # k = k-1
        mini = 10000
        for i in range(len(blocks)):
            if i+k <= len(blocks):
                s = blocks[i:i+k].count("W")
            mini = min(mini , s)
        return mini
