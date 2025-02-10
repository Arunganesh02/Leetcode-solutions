class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for i in s:
            if i.isdigit():
                if len(st) != 0:
                    st.pop()
            else:
                st.append(i)
        return "".join(st)