class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length = 0;
        int max = length;
        ArrayList<Character> repeat = new ArrayList<Character>();
        for (int i=0;i< s.length();i++){
            char c = s.charAt(i);
            int index = repeat.indexOf(c);
            if (index == -1) {
                length++;
                repeat.add(c);
            }
            else{
                if (length > max) {
                		max = length;
                }
                	for (int j=0;j<=index;j++) {
                		repeat.remove(0);
                	}
                	repeat.add(c);
                	length = repeat.size();
            }
        
        }
        if (length>max){
            max = length;
        }
        return max;
    }
}
