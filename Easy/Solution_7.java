package Easy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Solution {
    public int reverse(int x) {
        boolean isNeg = false;
        int input = x;
        System.out.println(x);
        int[] MAX = {2,1,4,7,4,8,3,6,4,7};
        if (x<0){
            isNeg = true;
            x = Math.abs(x);
            if (x<0)
            //System.out.println(x);
            		return 0;
        }
        if (x/10==0){
            if (isNeg)
                return x*(-1);
            else
                return x;
        }
        ArrayList<Integer> array = new ArrayList<Integer>();
        while (x!=0){
            array.add(x%10);
            x = x/10;
        }
        
        for (int i=0;i<array.size();i++){
            System.out.print(array.get(i));
        }
        System.out.println();
        if (array.size()>10) // 溢出
            return 0;
        else if(array.size()==10){
            int index = 0;
            if (isNeg)
                MAX[array.size()-1] = MAX[array.size()-1] + 1;
            while (index<array.size() && MAX[index]==array.get(index)){
                index ++;
            }
            if (index<array.size()){
                if(MAX[index]<array.get(index))
                    return 0;
            }
        }

        int length = array.size();
        int answer = 0;
        for (int i=0;i<length;i++){
            answer = answer + array.get(i)*power(length-i-1);
        }
        if (isNeg){
            return answer*-1;
        }
        else{
            return answer;
        }
    }
    
    public int power(int x){
        int result = 1;
        for (int i=1;i<=x;i++){
            result = result*10;
        }
        return result;
    }
}


public class Solution_7 {
	
	
	    public static void main(String[] args) throws IOException {
	        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	        String line;
	        while ((line = in.readLine()) != null) {
	            int x = Integer.parseInt(line);
	           // System.out.println(x);
	            //System.out.println(-x);
	            //Solution_7 r = new Solution_7();
	            
	            int ret = new Solution().reverse(x);
	            
	            String out = String.valueOf(ret);
	            
	            System.out.print(out);
	        }
	    }
	

}
