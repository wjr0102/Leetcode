class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        a = sum(A)
        if a%3 != 0:
            return False
        a = a//3
        # print(a)
        
        def get_part(index,n=3):
            # print(index,n)
            if n==0:
                return True
            if index>=len(A):
                return False
            ans = 0
            is_ok = False
            for i in range(index,len(A)):
                ans += A[i]
                if ans == a:
                    is_ok = get_part(i+1,n-1)
                    if is_ok:
                        return True
            return False

        return get_part(0)