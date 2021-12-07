// 264. Ugly Number II

class Solution {
    public int nthUglyNumber(int n) {
        int[] uglyNumbers = new int[n];
        uglyNumbers[0] = 1;
        
        int i2 = 0, i3 = 0, i5 = 0;
        
        for (int i = 1; i < n; i++) {
            int ugly2 = 2 * uglyNumbers[i2];
            int ugly3 = 3 * uglyNumbers[i3];
            int ugly5 = 5 * uglyNumbers[i5];
            int nextUglyNumber = Math.min(Math.min(ugly2, ugly3), ugly5);
            
            if (nextUglyNumber == ugly2)
                i2++;
            if (nextUglyNumber == ugly3)
                i3++;
            if (nextUglyNumber == ugly5)
                i5++;
            uglyNumbers[i] = nextUglyNumber;
        }
        return uglyNumbers[n - 1];
    }
}
