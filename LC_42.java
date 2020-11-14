// 42. Trapping Rain Water

class Solution {
    public int trap(int[] height) {
        if (height.length < 3)
            return 0;
        int i = 0;
        int j = height.length - 1;
        int lMax = height[i];
        int rMax = height[j];
        int total_water = 0;
        
        while (i <= j) {
            lMax = Math.max(lMax, height[i]);
            rMax = Math.max(rMax, height[j]);
            if (lMax <= rMax) {
                total_water += lMax - height[i];
                i++;
            } else {
                total_water += rMax - height[j];
                j--;
            }
        }
        return total_water;
    }
}
