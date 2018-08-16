package Medium;

public class WaterContainer {
	
	public static int maxArea(int[] height) {
		int max = 0;
		for (int i=0;i<height.length;i++) {
			for (int j=i+1;j<height.length;j++) {
				int width = height[i];
				if (width > height[j]) {
					width = height[j];
				}
				int area = width * (j-i);
				if (area > max) {
					max = area;
				}
			}
		}
		return max;
	}
	
	public static int maxArea_f(int[] height) {
		int max = 0;
		int l = 0;
		int r = height.length - 1;
		while(l<r) {
			int width = Math.min(height[l], height[r]);
			int current = width * (r-l);
			if (max < current) {
				max = current;
			}
			while (height[l]<= width && l<r ) l++;
			while (height[r]<= width && l<r) r--;
		}
		return max;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] height = {1,8,6,2,5,4,8,3,7};
		System.out.println(maxArea_f(height));
	}

}

