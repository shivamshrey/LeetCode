// 201. Bitwise AND of Numbers Range

class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        int zeroBits = 0;   // no. of bits on the right 
                            // that will be 0 in the answer
        
        while (left != right) {
            left >>= 1;
            right >>= 1;
            zeroBits++;
        }
        
        return left << zeroBits;
    }
}
