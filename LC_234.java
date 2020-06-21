/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        
        ListNode fptr = head;
        ListNode sptr = head;
        
        while (fptr != null && fptr.next != null) {
            fptr = fptr.next.next;
            sptr = sptr.next;
        }

        sptr = reverse(sptr);
        fptr = head;
        
        while (sptr != null) {
            if (fptr.val != sptr.val)
                return false;
            sptr = sptr.next;
            fptr = fptr.next;
        }
        
        return true;    
    }
    
    public ListNode reverse(ListNode head) {
        
        ListNode prev = null;
        ListNode cur = head;
        ListNode next = null;
        
        while (cur != null) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        
        return prev;
    }
}
