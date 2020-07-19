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
    int i = 0;
    public int getDecimalValue(ListNode head) {
        if (head != null)
            return getDecimalValue(head.next) + head.val * (int) Math.pow(2, i++);
        return 0;
    }
}
