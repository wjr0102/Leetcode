class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # len(str1)>len(str2)
        if len(str2)>len(str1):
            temp = str2
            str2 = str1
            str1 = temp
        
        num1 = len(str1)
        num2 = len(str2)

        def gcd(a,b):
            if a==0:
                return b
            return gcd(b%a,a)
        
        x = gcd(num2,num1)
        factors = [x]

        for i in range(x-1,0,-1):
            if num2%i==0 and num1%i==0:
                factors.append(i)
        
        for factor in factors:
            str2_ok = True
            str1_ok = True
            is_ok = True
            # Check str2
            for i in range(num2-factor):
                if str2[i]!=str2[i+factor]:
                    str2_ok = False
                    break
            # Check str1
            for i in range(num1-factor):
                if str1[i]!=str1[i+factor]:
                    str1_ok = False
                    break
            # Check str1 and str2:
            if str1[:factor] != str2[:factor]:
                is_ok = False
            if str2_ok and str1_ok and is_ok:
                return str1[:factor]
        return ""

        if str1+str2 != str2 + str1:
            return ""

        def gcd(a,b):
            if a==0:
                return b
            return gcd(b%a,a)
        
        if len(str1)<len(str2):
            temp = str1
            str1 = str2
            str2 = temp
            
        x = gcd(len(str2),len(str1))
        return str1[:x]
