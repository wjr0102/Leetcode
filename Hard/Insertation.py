class Solution:
    def intersection(self, start1, end1, start2, end2):
        k1,k2,b1,b2 = 0,0,0,0
        cal_l1 = False
        cal_l2 = False
        # line1垂直
        if start1[0] == end1[0]:
            print("line1垂直")
            l11 = min(end1[1],start1[1])
            l12 = max(start1[1],end1[1])
            l21 = min(end2[1],start2[1])
            l22 = max(start2[1],end2[1])
            # line2 垂直:
            if start2[0] == end2[0]:
                print("line2垂直")
                if start1[0] == start2[0]:
                    if l11>l22 or l21>l12:
                        return []
                    else:
                        y = 0
                        if l11<l22:
                            y = l22
                        else:
                            y =  l12
                        return [start1[0],y]
                else:
                    return []
            # l2 不垂直
            else:
                print("line2不垂直")
                k2 = (start2[1]-end2[1])/(start2[0]-end2[0])
                b2 = start2[1]-k2*start2[0]
                cal_l2 = True
                y = k2*start1[0]+b2
                if y>=l11 and y<=l12:
                    return [start1[0],y]
                else:
                    return []
        # line2垂直
        if start2[0] == end2[0]:
            l21 = min(end2[1],start2[1])
            l22 = max(start2[1],end2[1])
            # l1 不垂直
            k1 = (start1[1]-end1[1])/(start1[0]-end1[0])
            b1 = start1[1]-k1*start1[0]
            cal_l2 = True
            y = k1*start2[0]+b1
            if y>=l21 and y<=l22:
                return [start2[0],y]
            else:
                return []    

        if not cal_l2:
            k2 = (start2[1]-end2[1])/(start2[0]-end2[0])
            b2 = start2[1]-k2*start2[0]
        if not cal_l1:
            k1 = (start1[1]-end1[1])/(start1[0]-end1[0])
            b1 = start1[1]-k1*start1[0]

        l11 = min(end1[0],start1[0])
        l12 = max(start1[0],end1[0])
        l21 = min(end2[0],start2[0])
        l22 = max(start2[0],end2[0])

        if k1==k2:
            # 平行
            if b1!=b2:
                return []
            # 重叠
            if l11 > l22 or l21 > l12:
                return []
            else:
                x = 0
                if l11<l22:
                    x = l22
                else:
                    x =  l12
                return [x,k2*x+b2]

        # 不平行
        x = (b2-b1)/(k1-k2)
        if x>=l11 and x<=l12 and x>=l21 and x<=l22:
            return [x,k2*x+b2]
        else:
            return []

if __name__ == "__main__":
    s = Solution()
    start1 = [0,0]
    end1 = [0,1]
    start2 = [1,0]
    end2 = [1,1]
    print(s.intersection(start1,end1,start2,end2))
