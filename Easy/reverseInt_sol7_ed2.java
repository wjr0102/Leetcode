class Solution {
    public int reverse(int x) {
    	int result = 0;
		boolean isNeg = false;
		if (x<0) {
			isNeg = true;
			x = Math.abs(x);
            if (x<0)
            //System.out.println(x);
            		return 0;
		}
        int factor = (int) Math.pow(10, (int)Math.log10(x));

		while (x!=0) {
			if ((x%10)*factor/factor != x%10) {
				System.out.println(result);
				System.out.println(x%10);
				return 0;
			}
			result = result + (x%10)*factor;
			if (result <0 )
				return 0;
			
			x = x/10;
			factor = factor /10;
		}
		if (isNeg)
			return -result;
		else
			return result;
    }
    
}
