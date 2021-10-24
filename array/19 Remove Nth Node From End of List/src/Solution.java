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

    int i=0;
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode();
        dummy.next=head;
        recur(dummy,n);
        return dummy.next;
    }

    private ListNode recur(ListNode head,int n){
        if (head.next==null)
        {
            i+=1;
            return head;
        }
        else
        {
            recur(head.next,n);
            if (i==n)
            {
                head.next=head.next.next;
            }
            i+=1;
            return head;
        }
    }
}