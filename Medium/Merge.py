class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        k = m+n-1
        i = m-1
        j = n-1
        while (i>=0 and j>=0):
            if (A[i]<B[j]):
                A[k] = B[j]
                k -= 1
                j -= 1
            else:
                A[k] = A[i]
                k -= 1
                i -= 1

        while j>=0:
            A[k] = B[j]
            k -= 1
            j -= 1