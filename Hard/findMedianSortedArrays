class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int i = 0;
        int j = 0;
        int[] nums = new int[nums1.length+nums2.length];
        double result = 0;
        int m = (nums1.length+nums2.length)/2;
        //System.out.println("m="+m);
        while (i+j<=m) {
        		if (i==nums1.length) {
        			// nums1 all in nums
        			for (int k=j;k+i<=m;k++) {
        				nums[k+i] = nums2[k];
        			}
        			break;
        		}
        		if (j==nums2.length) {
        			// nums2 all in nums
        			for (int k=i;k+j<=m;k++) {
        				nums[k+j] = nums1[k];
        			}
        			break;
        		}
        		if (nums1[i]<nums2[j]) {
        			nums[i+j] = nums1[i];
        			if (i<nums1.length)
        				i++;
        		}
        		else {
        			nums[i+j] = nums2[j];
        			if (j<nums2.length)
        				j++;
        		}
        }

        if ((nums1.length+nums2.length)%2==0) {
        		// even
        		result = ((double)nums[m] + nums[m-1])/2;
        }
        else {
        		// odd
        		result = nums[m];
        }
        //System.out.println(result);
        	return result;
    
    }
}
