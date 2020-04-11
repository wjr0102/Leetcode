class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k==len(arr):
            return arr
        if k==0:
            return []
        if k==1:
            return [min(arr)]


        def q_sort(l,r):
            print("left = %d\tright=%d"%(l,r))
            i = l
            j = r
            x = arr[i]
            while i<j:
                while i<j and arr[j]>=x:
                    j -= 1
                if i<j:
                    arr[i] = arr[j]
                while i<j and arr[i]<x:
                    i += 1
                if i<j:
                    arr[j] = arr[i]
            arr[i] = x
            print(arr,i)
            if i+1==k:
                return arr[:k]
            elif i+1<k:
                return q_sort(i+1,r)
            else:
                return q_sort(l,i-1)

        return q_sort(0,len(arr)-1)
        
