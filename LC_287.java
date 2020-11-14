// 287. Find the Duplicate Number

class Solution {
    public int findDuplicate(int[] nums) {
        int fptr = nums[0];
        int sptr = nums[0];
        
        while (true) {
            sptr = nums[sptr];
            fptr = nums[nums[fptr]];
            if (sptr == fptr)
                break;
        }
        
        fptr = nums[0];
        while (sptr != fptr) {
            sptr = nums[sptr];
            fptr = nums[fptr];
        }
        
        return fptr;
    }
}
