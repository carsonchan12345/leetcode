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
    public void reorderList(ListNode head) {

        ListNode fast = head.next;
        ListNode slow = head;
        if (fast==null)
            return;
        //find mid
        while(true)
        {
            if(fast.next==null)
            {
                break;
            }
            else if (fast.next.next==null)
            {

                slow=slow.next;
                break;
            }
            else
            {
                slow=slow.next;
                fast=fast.next.next;
            }

        }
        ListNode prev = null;
        ListNode second = slow.next;
        slow.next=null;
        while(second!=null)
        {
            ListNode tmp = second.next;
            second.next=prev;
            prev=second;
            second=tmp;
        }
        ListNode pointer1=head;
        ListNode pointer2=prev;
        ListNode tmp1,tmp2;
        while(pointer2!=null)
        {
            tmp1=pointer1.next;
            tmp2=pointer2.next;
            pointer1.next=pointer2;
            pointer2.next=tmp1;
            pointer1=tmp1;
            pointer2=tmp2;
        }

    }
}