// Dynamic Programming
class Solution {
    public String longestPalindrome(String s) {
        String result = "";
        int length = 1;
        int index = 0;
        int[][] dp = new int[s.length()][s.length()];
        // Initilization
        for (int i=0;i<s.length();i++) {
        		dp[i][i] = 1;
        		if (i<s.length()-1) {
        			if (s.charAt(i)==s.charAt(i+1)) {
        				dp[i][i+1] = 1;
        				length = 2;
        				index = i;
        			}
        		}
        }
        // Transform
        for (int i = 3;i<=s.length();i++) {	// Length
        		for (int j=0;j+i-1<s.length();j++) {	// Begin index
        			int k = j+i-1;					// End index
        			if (s.charAt(j)==s.charAt(k) && dp[j+1][k-1]==1) {
        				dp[j][k] = 1;
        				length = i;
        				index = j;
        			}
        		}
        }
        result = s.substring(index, index+length);
		return result;
    }
}
