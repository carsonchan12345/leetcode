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
// paste it to leetcode
class Solution {

    ListNode newhead;

    public ListNode reverseList(ListNode head){
        if (head==null)
            return head;
        ListNode res = loop(head);
        head.next=null;


        return newhead;

    }

    private ListNode loop(ListNode head){

        if (head.next==null)
        {
            newhead=head;
            return head;
        }
        else
        {
            ListNode tmp = loop(head.next);
            tmp.next = head;
            return tmp.next;
        }


    }
}