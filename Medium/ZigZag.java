class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
			return s;
		}
        String[] rows = new String[numRows];
		String result = "";

		for (int i=0;i<numRows;i++) {
			rows[i] = "";
			int j = i;
			while (j<s.length()) {
				rows[i] = rows[i] + s.substring(j, j+1);
				if (rows[i].length()%2!=0 || (i==0 || i==numRows-1)) {
					if (i ==numRows -1) {
						j = j + (numRows - 1) + (numRows - 2)+1;
					}
					else {
						j = j + (numRows- i - 1) + (numRows - i - 2) + 1;
					}
				}
				else {
					j = j + 2*i;
				}
			}
			result = result + rows[i];
		}
		return result;
    }
}
