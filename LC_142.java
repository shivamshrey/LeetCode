/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        
        ListNode fptr = head;
        ListNode sptr = head;
        
        while (sptr != null && fptr != null && fptr.next != null) {
            sptr = sptr.next;
            fptr = fptr.next.next;
            if (fptr == sptr) {
                while (head != sptr) {
                    head = head.next;
                    sptr = sptr.next;
                }
                return head;
            }
        }
            
        return null;
    }
}