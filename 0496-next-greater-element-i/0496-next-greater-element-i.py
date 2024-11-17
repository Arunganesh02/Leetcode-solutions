class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li = []
        st = [nums2[0]]
        d = {}
        i = 1
        while i<len(nums2):
            if st and nums2[i] > st[-1]:
                if st:
                    d[st[-1]] = nums2[i]
                    st.pop()
                else:
                    st.append(nums2[i])
                    i+=1
            else:
                st.append(nums2[i])
                i +=1
        for i in nums1:
            if i not in d:
                li.append(-1)
            else:
                li.append(d[i])

        return li